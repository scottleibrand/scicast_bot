"""lmsrutils.py

Functions for calculating LMSR gains, costs, probs/prices, and trade limits.

"""
import logging

import numpy as np


def isprob(p: np.array, tol=1e-4) -> bool:
    '''Is p a valid probability? Ask Kolmogorov!'''
    if any(p < 0) or any(p > 1):
        return False
    if 1 - tol < sum(p) < 1 + tol:
        return True
    return False


def gain(p: np.array, q: np.array, b: float = 100.0) -> np.array:
    '''Core LMSR equation. Return b log2 (q / p). p = old probs, q = new probs'''
    if isprob(q) and isprob(p) and (b > 0):
        return b * np.log2(q / p)
    raise ValueError('p, q must be prob vectors; b>0')


def cost_to_probs(p: np.array, cost: float, focus, buy=True,
                  b: float = 100) -> np.array:
    '''Return new_p given p, cost, focus, and buy/sell.

        - p: original probability vector
        - cost: how much to spend -- abs value
        - focus: index of focus prob to buy/sell (others move proportionally)
        - buy: True or 'buy' will BUY the focus
               False or 'sell' will SELL the focus
        - b: LMSR liquidity

       Because we lack the full gain array, we must SPECIFY buy/sell.
       (We *could* encode that in sign(cost), but that's opaque.)

    '''
    logging.debug(f'cost_to_probs: p={p}, cost=${cost:.2f}, focus={focus}, buy={buy}')
    cost = -abs(cost)
    ones = np.ones(len(p))
    if buy in [True, 'buy', 'BUY']:
        c = cost * ones
        q = 2 ** (c / b) * p
        q[focus] = 0
        q[focus] = 1 - sum(q)
    elif buy in [False, 'sell', 'SELL']:
        # Convert to binary and buy non-focus.
        p_bin = np.array([p[focus], 1 - p[focus]])  # focus, non-focus
        q_bin = cost_to_probs(p_bin, cost, 1)  # focus on the non-focus (Recursive, once)
        g_bin = gain(p_bin, q_bin)  # actual binary gains
        logging.debug(f'\tq_bin: {q_bin}\n\tg_bin: {g_bin}')
        c = np.ones(len(p)) * g_bin[1]  # Everything else goes up by non-focus ratio
        c[focus] = g_bin[0]  # Re-assert focus cost
        assert np.isclose(g_bin[0], cost)
        q = 2 ** (c / b) * p  # Re-calculate q
    else:
        raise ValueError('"buy" should be in {True, False, "buy", "sell"}')

    logging.debug(f'q={q}')
    assert isprob(q)
    return q


def trade_limits(p: np.array, cost: float, focus, b: float = 100) -> np.array:
    """Determine [min,max] limits for changing p[focus] for cost."""
    q_max = cost_to_probs(p, cost, focus, 'buy')[focus]
    q_min = cost_to_probs(p, cost, focus, 'sell')[focus]
    try:
        assert q_min <= p[focus] <= q_max
    except AssertionError:
        logging.error(f"ERR: Should have: {q_min:.3f} ≤ {p[focus]:.3f} ≤ {q_max:.3f}")
        raise AssertionError
    return q_min, q_max



def probs_from_shares(probs: np.array, shares: float, focus: int,
                      b: float = 100) -> float:
    '''Get new_p given p, focus, and shares to buy (negative if selling).'''
    logging.debug('s2p:', probs, shares, focus)
    p_d = probs[focus]
    q_d = -p_d / (p_d * 2 ** (-shares / b) - 2 ** (-shares / b) - p_d)
    ones = np.ones(len(probs))

    if len(probs) == 2:
        # We're done. Return q_d & 1-q_d such that q_d is in spot d.
        q = ones * (1 - q_d)
        q[focus] = q_d
        return q

    # Nonbinary world.
    # 1. Solve gain() for equivalent binary.
    p_bin = np.array([p_d, 1 - p_d])  # Faux binary p
    q_bin = np.array([q_d, 1 - q_d])  # Faux binary q
    g_bin = gain(p_bin, q_bin)  # Calc faux binary gain
    s_bin = sum(abs(g_bin))  # Faux binary shares - should match

    # 2. Sanity checks
    logging.debug(f"""
        q_d  : {q_d:.2f}
        p_bin: {p_bin}
        q_bin: {q_bin}
        g_bin: {g_bin}, ∑={s_bin:.2f}""")
    assert np.isclose(s_bin, abs(shares))

    # 3. Build true gain vector using binary nonfocus gain, except in focus of course.
    g = ones * g_bin[1]
    g[focus] = g_bin[0]

    # 4. Solve for q using true gain vector.
    # If we drop probs_from_gains, just figure out whether we're buying or selling the focus can use cost version.
    q = probs_from_gains(probs, g, focus)
    assert np.isclose(q[focus], q_d)
    return q
