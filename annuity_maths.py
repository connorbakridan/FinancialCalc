"""
annuity_maths.py
----------------
Pure calculation functions for compound interest and annuity values
(standard actuarial notation, as used in Financial Mathematics 1 /
the IFoA Formulae and Tables).

No input()/print() here on purpose, these functions just compute
numbers, so they can be tested and reused without needing a live
interactive session.
"""

import math


# ---------------------------------------------------------------------
# Interest rate conversions
# ---------------------------------------------------------------------

def d_from_i(i):
    """Effective discount rate d, from effective interest rate i."""
    return i / (1 + i)


def i_from_d(d):
    """Effective interest rate i, from effective discount rate d."""
    return ((1 - d) ** -1) - 1


def force_from_i(i):
    """Force of interest, delta = ln(1 + i)."""
    return math.log(1 + i)


def i_from_force(f):
    """Effective interest rate i, from force of interest delta."""
    return math.exp(f) - 1


def d_from_force(f):
    """Effective discount rate d, from force of interest delta."""
    return 1 - math.exp(-f)


def force_from_d(d):
    """Force of interest delta, from effective discount rate d."""
    return -math.log(1 - d)


def ip_from_i(i, p):
    """Nominal interest rate payable p-thly, from effective i."""
    return p * (((1 + i) ** (1 / p)) - 1)


def i_from_ip(ip, p):
    """Effective interest rate i, from nominal i^(p)."""
    return ((1 + ip / p) ** p) - 1


def dp_from_i(i, p):
    """Nominal discount rate payable p-thly, from effective i."""
    v = 1 / (1 + i)
    return p * (1 - v ** (1 / p))


def i_from_dp(dp, p):
    """Effective interest rate i, from nominal d^(p)."""
    return ((1 - dp / p) ** -p) - 1


# ---------------------------------------------------------------------
# Annuity values (annual and continuous payment, non-p-thly)
# ---------------------------------------------------------------------

def compute_annuities(i, t):
    """
    Returns a dict of all annuity values for a given effective interest
    rate i and time t, matching standard actuarial notation:
      at, vt              - accumulation and discount factors
      an, andue, anf       - level annuity (immediate / due / continuous)
      sn, sndue, snf        - accumulated value versions of the above
      Ian, Iandue, Ianf, Ianff       - increasing annuity variants
      SIan, SIandue, SIanf, SIanff   - accumulated value of increasing annuity
      Dan, Dandue, Danf, Danff       - decreasing annuity variants
      SDan, SDandue, SDanf, SDanff   - accumulated value of decreasing annuity
    """
    d = d_from_i(i)
    f = force_from_i(i)  # force of interest, delta = ln(1+i)

    at = (1 + i) ** t
    vt = at ** -1

    an = (1 - vt) / i
    andue = an * (i / d)
    anf = an * (i / f)

    sn = an * at
    sndue = andue * at
    snf = anf * at

    Ian = (andue - (t * vt)) / i
    Iandue = Ian * (i / d)
    Ianf = Ian * (i / f)
    Ianff = (anf - (t * vt)) / f

    SIan = Ian * at
    SIandue = Iandue * at
    SIanf = Ianf * at
    SIanff = Ianff * at

    Dan = (t - an) / i
    Dandue = Dan * (i / d)
    Danf = Dan * (i / f)
    Danff = (t - anf) / f

    SDan = Dan * at
    SDandue = Dandue * at
    SDanf = Danf * at
    SDanff = Danff * at

    return {
        "AT": at, "VT": vt,
        "AN": an, "ANDUE": andue, "ANF": anf,
        "SN": sn, "SNDUE": sndue, "SNF": snf,
        "IAN": Ian, "IANDUE": Iandue, "IANF": Ianf, "IANFF": Ianff,
        "SIAN": SIan, "SIANDUE": SIandue, "SIANF": SIanf, "SIANFF": SIanff,
        "DAN": Dan, "DANDUE": Dandue, "DANF": Danf, "DANFF": Danff,
        "SDAN": SDan, "SDANDUE": SDandue, "SDANF": SDanf, "SDANFF": SDanff,
    }


def compute_annuities_pthly(i, t, p):
    """
    Returns a dict of p-thly payable annuity values, given effective
    interest rate i, time t, and payment frequency p (e.g. p=12 for
    monthly). Matches the *P suffix notation (ANP, ANDUEP, etc.)
    """
    d = d_from_i(i)
    ip = ip_from_i(i, p)
    dp = dp_from_i(i, p)

    at = (1 + i) ** t
    vt = at ** -1

    an = (1 - vt) / i
    anp = an * (i / ip)
    anduep = an * (i / dp)

    snp = anp * at
    snduep = anduep * at

    andue = an * (i / d)
    Ian = (andue - (t * vt)) / i
    Ianp = Ian * (i / ip)
    Ianduep = Ian * (i / dp)

    SIanp = Ianp * at
    SIanduep = Ianduep * at

    Dan = (t - an) / i
    Danp = Dan * (i / ip)
    Danduep = Dan * (i / dp)

    SDanp = Danp * at
    SDanduep = Danduep * at

    return {
        "ANP": anp, "ANDUEP": anduep,
        "SNP": snp, "SNDUEP": snduep,
        "IANP": Ianp, "IANDUEP": Ianduep,
        "SIANP": SIanp, "SIANDUEP": SIanduep,
        "DANP": Danp, "DANDUEP": Danduep,
        "SDANP": SDanp, "SDANDUEP": SDanduep,
    }
