# Financial Mathematics Calculator

A command-line calculator for compound interest and annuity values,
covering the standard actuarial notation from Financial Mathematics 1
(effective/nominal/force of interest, level/increasing/decreasing
annuities, annual or p-thly payable).

## Why this got rewritten

The original version worked, but was built by duplicating the same
~40-line calculation block and ~150-line menu block separately for
every interest rate type (I, D, IP, DP, F), which made the file over
2000 lines despite the actual logic being fairly small.

Going through it to refactor also turned up a real bug: the force of
interest (delta) was being calculated as `math.exp(i)` in the annuity
section (and `math.log(i)` in the converter section), when the correct
identity is delta = ln(1+i). This meant every continuously-paid annuity
value (ANF, IANF, DANF, etc.) in the original version was wrong. Fixed
here, and verified against manual calculations (see `annuity_maths.py`
docstrings and the round-trip checks run during development).

## Structure

- **`annuity_maths.py`** - pure calculation functions (no input/print).
  Interest rate conversions (i, d, i^(p), d^(p), delta) and annuity
  values (PV/AV of level, increasing, decreasing annuities, annual and
  p-thly payable). Each function does one calculation, so the maths can
  be tested independently of the interactive part.
- **`financial_maths_calculator.py`** - the interactive CLI. Handles
  user input/menus and calls into `annuity_maths.py` for the actual
  numbers.

## Verifying the fix

```python
from annuity_maths import force_from_i
import math

i = 0.05
print(force_from_i(i))        # 0.04879... (correct: ln(1.05))
print(math.exp(i))            # 1.0512...  (what the old version used instead)
```

## Running it

```bash
python3 financial_maths_calculator.py
```

Choose **C** to calculate annuity/cashflow values, or **P** to convert
between interest rate types.

## Notes

The relationships between the level-annuity values and their increasing/
decreasing/continuous variants (e.g. `Ianf`, `Danff`, the p-thly
conversions) are preserved from the original version, not re-derived
from scratch. The main formulas (an, andue, sn, Ian, Dan, i^(p), d^(p))
were checked against standard identities during this rewrite; the less
common ones should still be checked against course notes before relying
on them for anything beyond this calculator.

