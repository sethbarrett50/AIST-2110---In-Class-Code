from typing import Tuple, Union


def grade_format(
    score: float,
    out_of: float = 100.0,
    *,
    decimals: int = 2,
    return_tuple: bool = False,
    show_raw: bool = True,
) -> Union[str, Tuple[str, str]]:
    """
    Format a numeric grade as a percentage string with a letter grade.

    The function converts a score to a percentage (optionally using an
    `out_of` maximum), trims trailing zeros, and appends the letter grade
    using the scale:
        A: 90–100
        B: 80–89
        C: 75–79
        D: 70–74
        F:  0–69

    Examples
    --------
    >>> grade_formatter(92.5)
    '92.5% (A)'
    >>> grade_formatter(87, out_of=90)
    '96.67% (A) — raw: 87/90'
    >>> grade_formatter(74.0)
    '74% (D)'
    >>> grade_formatter(88.0, return_tuple=True)
    ('88%','B')

    Parameters
    ----------
    score : float
        The achieved points or percentage value. If `out_of` is 100.0 (the
        default), `score` is treated as a percentage in [0, 100]. Otherwise,
        `score/out_of * 100` is used.
    out_of : float, optional
        The maximum possible points corresponding to 100%. Defaults to 100.0.
    decimals : int, optional
        Maximum number of decimal places to display for the percentage and
        raw values. Must be >= 0. Defaults to 2.
    return_tuple : bool, optional
        If True, return a tuple `(percent_str, letter)` instead of a single
        combined string. Defaults to False.
    show_raw : bool, optional
        If True and `out_of` is not 100.0, append the raw score fragment
        `" — raw: <score>/<out_of>"` to the string. Defaults to True.

    Returns
    -------
    str or (str, str)
        Either a combined string like `'96.67% (A) — raw: 87/90'` or a tuple
        `('96.67%', 'A')` when `return_tuple=True`.

    Raises
    ------
    ValueError
        If `decimals` is negative, `out_of` <= 0, or the score is outside the
        valid range [0, out_of]. Specifically, the function enforces that the
        percentage is within [0, 100].

    Notes
    -----
    The letter grade decision uses the unrounded percentage; rounding only
    affects how the value is displayed.
    """
    if decimals < 0:
        raise ValueError("decimals must be >= 0")

    if out_of <= 0:
        raise ValueError("out_of must be > 0")

    if score < 0 or score > out_of:
        raise ValueError(
            f"score must be within [0, {out_of}] (got {score})."
        )

    percent = (score / out_of) * 100.0

    if percent < 0.0 or percent > 100.0:
        raise ValueError(
            f"Computed percentage {percent:.4f} is outside [0, 100]. "
            "Check 'score' and 'out_of'."
        )

    letter = _letter_from_percentage(percent)

    percent_str = f"{_trimmed_float(percent, decimals)}%"
    if return_tuple:
        return percent_str, letter

    result = f"{percent_str} ({letter})"
    if show_raw and out_of != 100.0:
        raw_score = _trimmed_float(score, decimals)
        raw_out_of = _trimmed_float(out_of, decimals)
        result = f"{result} — raw: {raw_score}/{raw_out_of}"

    return result


def _letter_from_percentage(percent: float) -> str:
    """
    Map a percentage to a letter grade using fixed thresholds.
    """
    if 90.0 <= percent <= 100.0:
        return "A"
    if 80.0 <= percent < 90.0:
        return "B"
    if 75.0 <= percent < 80.0:
        return "C"
    if 70.0 <= percent < 75.0:
        return "D"
    return "F"


def _trimmed_float(value: float, decimals: int) -> str:
    """
    Round to `decimals` places, then return a string without trailing zeros
    or a trailing decimal point.
    """
    rounded = round(value, decimals)
    text = f"{rounded:.{decimals}f}" if decimals > 0 else f"{int(round(rounded))}"
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text
