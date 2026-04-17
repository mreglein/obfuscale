"""Minimal Jensen–Shannon divergence placeholder (prob dists expected)."""

import math


def _kl(p, q):
    return sum(
        pi * math.log2(pi / q[i]) for i, pi in enumerate(p) if pi > 0 and q[i] > 0
    )


def jsd(p, q):
    m = [(pi + qi) / 2 for pi, qi in zip(p, q)]
    return 0.5 * _kl(p, m) + 0.5 * _kl(q, m)
