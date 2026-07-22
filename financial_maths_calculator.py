"""
financial_maths_calculator.py
------------------------------
Interactive command-line financial mathematics calculator: converts
between interest rate types, and calculates annuity values (PV/AV of
level, increasing and decreasing annuities, annual or p-thly payable).

This is a refactor of an earlier version that duplicated the same
calculation and menu-display logic separately for each interest rate
type (~2000+ lines). The maths itself lives in annuity_maths.py as
plain functions; this file only handles user interaction.
"""

import sys
from annuity_maths import (
    d_from_i, i_from_d, force_from_i, i_from_force, d_from_force, force_from_d,
    ip_from_i, i_from_ip, dp_from_i, i_from_dp,
    compute_annuities, compute_annuities_pthly,
)

# Aliases accepted for each interest rate type, so users can type either
# the short code or a full description.
INTEREST_ALIASES = {
    "I": ["I", "EFFECTIVE RATE OF INTEREST PER ANNUM", "EFFECTIVE RATE OF INTEREST",
          "EFFECTIVE INTEREST RATE", "EFFECTIVE", "EFFECTIVE INTEREST",
          "INTEREST EFFECTIVE", "RATE OF INT"],
    "D": ["D", "EFFECTIVE RATE OF DISCOUNT PER ANNUM", "EFFECTIVE RATE OF DISCOUNT",
          "EFFECTIVE DISCOUNT RATE", "DISCOUNT EFF", "EFFECTIVE DISCOUNT",
          "DISCOUNT EFFECTIVE", "RATE OF DIS"],
    "IP": ["IP", "NOMINAL RATE OF INTEREST", "NOMINAL RATE OF INTEREST PER ANNUM",
           "NOMINAL INTEREST RATE", "NOMINAL INTEREST", "INTEREST NOMINAL",
           "RATE OF INT PTHLY"],
    "DP": ["DP", "NOMINAL RATE OF DISCOUNT", "NOMINAL RATE OF DISCOUNT PER ANNUM",
           "NOMINAL DISCOUNT RATE", "NOMINAL DISCOUNT", "DISCOUNT NOMINAL",
           "RATE OF DIS PTHLY"],
    "F": ["F", "FORCE OF INTEREST PER ANNUM", "FORCE OF INTEREST", "FORCE",
          "FORCE PER ANNUM", "INTEREST FORCE"],
}

# Human-readable labels and the print description for each annuity function.

ANNUITY_DESCRIPTIONS = {
    "AT": "the accumulated value",
    "VT": "the discounted (present) value",
    "AN": "the PV of an annuity-immediate (paid in arrears)",
    "ANDUE": "the PV of an annuity-due (paid in advance)",
    "ANF": "the PV of a continuously-paid annuity",
    "SN": "the accumulated value of an annuity-immediate",
    "SNDUE": "the accumulated value of an annuity-due",
    "SNF": "the accumulated value of a continuously-paid annuity",
    "IAN": "the PV of an increasing annuity-immediate",
    "IANDUE": "the PV of an increasing annuity-due",
    "IANF": "the PV of a continuously-paid increasing annuity",
    "IANFF": "the PV of a continuously-paid, continuously-increasing annuity",
    "SIAN": "the accumulated value of an increasing annuity-immediate",
    "SIANDUE": "the accumulated value of an increasing annuity-due",
    "SIANF": "the accumulated value of a continuously-paid increasing annuity",
    "SIANFF": "the accumulated value of a continuously-paid, continuously-increasing annuity",
    "DAN": "the PV of a decreasing annuity-immediate",
    "DANDUE": "the PV of a decreasing annuity-due",
    "DANF": "the PV of a continuously-paid decreasing annuity",
    "DANFF": "the PV of a continuously-paid, continuously-decreasing annuity",
    "SDAN": "the accumulated value of a decreasing annuity-immediate",
    "SDANDUE": "the accumulated value of a decreasing annuity-due",
    "SDANF": "the accumulated value of a continuously-paid decreasing annuity",
    "SDANFF": "the accumulated value of a continuously-paid, continuously-decreasing annuity",
}

PTHLY_DESCRIPTIONS = {
    "ANP": "the PV of a p-thly annuity-immediate",
    "ANDUEP": "the PV of a p-thly annuity-due",
    "SNP": "the accumulated value of a p-thly annuity-immediate",
    "SNDUEP": "the accumulated value of a p-thly annuity-due",
    "IANP": "the PV of a p-thly increasing annuity-immediate",
    "IANDUEP": "the PV of a p-thly increasing annuity-due",
    "SIANP": "the accumulated value of a p-thly increasing annuity-immediate",
    "SIANDUEP": "the accumulated value of a p-thly increasing annuity-due",
    "DANP": "the PV of a p-thly decreasing annuity-immediate",
    "DANDUEP": "the PV of a p-thly decreasing annuity-due",
    "SDANP": "the accumulated value of a p-thly decreasing annuity-immediate",
    "SDANDUEP": "the accumulated value of a p-thly decreasing annuity-due",
}

DIVIDER = "-" * 76


def normalise_interest_type():
    """Build a lookup: any accepted alias (upper-cased) -> canonical code."""
    lookup = {}
    for code, aliases in INTEREST_ALIASES.items():
        for alias in aliases:
            lookup[alias] = code
    return lookup


ALIAS_LOOKUP = normalise_interest_type()


def get_float(prompt, forbid_zero=True, forbid_negative=False):
    """Prompt repeatedly until a valid float is entered."""
    while True:
        try:
            value = round(float(input(prompt)), 6)
        except ValueError:
            print("Please enter a number.")
            continue
        if forbid_zero and value == 0:
            print("This value can't be zero, try again.")
            continue
        if forbid_negative and value < 0:
            print("This value can't be negative, try again.")
            continue
        return value


def get_effective_i():
    """
    Ask which interest rate type the user has, get its value, and return
    the equivalent effective annual interest rate i.
    """
    while True:
        raw = input("Choose the interest type you're working in "
                     "(I, D, IP, DP, or F): ").upper()
        code = ALIAS_LOOKUP.get(raw)
        if code is None:
            print(f"'{raw}' isn't a recognised interest rate type, try again.")
            continue
        break

    if code == "I":
        i = get_float("Enter the effective rate of interest per annum, as a percent: ")
        return i / 100

    if code == "D":
        d = get_float("Enter the effective rate of discount per annum, as a percent: ")
        return i_from_d(d / 100)

    if code == "IP":
        p = get_float("Enter the p in i^(p): ", forbid_negative=True)
        ip = get_float(f"Enter the nominal interest rate payable {p}-thly per annum, as a percent: ")
        return i_from_ip(ip / 100, p)

    if code == "DP":
        p = get_float("Enter the p in d^(p): ", forbid_negative=True)
        dp = get_float(f"Enter the nominal discount rate payable {p}-thly per annum, as a percent: ")
        return i_from_dp(dp / 100, p)

    if code == "F":
        f = get_float("Enter the force of interest per annum, as a percent: ")
        return i_from_force(f / 100)


def run_cashflow_calculator():
    """'C' mode: work out annuity values for a given interest rate, time,
    and capital amount."""
    i = get_effective_i()
    t = get_float("Enter the time in years: ", forbid_zero=False, forbid_negative=True)
    ct = get_float("Enter the amount of capital to apply: ")

    pthly = input("Is the capital payable p-thly during the year? "
                   "(Y/N): ").strip().upper()

    if pthly == "Y":
        p = get_float("Enter the p-thly frequency (e.g. 12 for monthly): ",
                       forbid_negative=True)
        values = compute_annuities_pthly(i, t, p)
        descriptions = PTHLY_DESCRIPTIONS
        valid_codes = ", ".join(PTHLY_DESCRIPTIONS.keys())
    else:
        values = compute_annuities(i, t)
        descriptions = ANNUITY_DESCRIPTIONS
        valid_codes = ", ".join(ANNUITY_DESCRIPTIONS.keys())

    while True:
        print(DIVIDER)
        choice = input(
            f"Choose a function to calculate, or Q to quit:\n{valid_codes}\n> "
        ).upper()

        if choice == "Q":
            print(DIVIDER)
            print("Thanks for using this calculator :)")
            return

        if choice not in values:
            print(f"'{choice}' isn't a valid function, please choose one listed above.")
            continue

        result = ct * values[choice]
        print(DIVIDER)
        print(f"At t={t}, i={round(i, 6)}, ct={ct}:")
        print(f"This is {descriptions[choice]}: {result}")


def run_interest_converter():
    """'P' mode: convert one interest rate type into another."""
    i = get_effective_i()

    target = input(
        "Choose the interest rate type to convert to (I, D, IP, DP, F): "
    ).upper()
    target_code = ALIAS_LOOKUP.get(target)
    if target_code is None:
        print(f"'{target}' isn't a recognised interest rate type.")
        return

    if target_code == "I":
        print(f"Effective rate of interest per annum: i = {i}")
    elif target_code == "D":
        print(f"Effective rate of discount per annum: d = {d_from_i(i)}")
    elif target_code == "F":
        print(f"Force of interest per annum: delta = {force_from_i(i)}")
    elif target_code == "IP":
        p = get_float("Enter the p you want i^(p) expressed as: ", forbid_negative=True)
        print(f"Nominal interest payable {p}-thly per annum: i^({p}) = {ip_from_i(i, p)}")
    elif target_code == "DP":
        p = get_float("Enter the p you want d^(p) expressed as: ", forbid_negative=True)
        print(f"Nominal discount payable {p}-thly per annum: d^({p}) = {dp_from_i(i, p)}")


def main():
    while True:
        mode = input(
            "Do you want to (C) calculate a cashflow/annuity value, "
            "or (P) convert between interest rate types? "
        ).upper()

        if mode == "C":
            run_cashflow_calculator()
            break
        elif mode == "P":
            run_interest_converter()
            break
        else:
            print("Please enter C or P.")


if __name__ == "__main__":
    main()
