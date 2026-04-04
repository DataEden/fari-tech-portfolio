"""
This module contains functions for calculating basic statistical metrics.

Functions:
    average(data: list) -> float | list:
    maximum(data: list) -> int | list:
    variance(data: list) -> float | list:
    standard_deviation(data: list) -> float | list:
    
 Args:
        data (list[int | float]): A list of integers or floats representing numerical data.

Returns:
        float: Average value of list as a floating-point number.

    Example and use:
        >>> average([1, 2, 3, 4, 5])
        3.0
        >>> average([])
        0.0
"""

def average(data: list) -> float:
    """
    Calculate arithmetic mean using base Python (no sum()).
    Returns [] if input is empty (test-compatible behavior).
    """
    if not data:
        return []

    sum_pop = 0
    for data_val in data:
        sum_pop += data_val

    num_pop = 0
    for _ in data:
        num_pop += 1

    return round(sum_pop / num_pop, 2)


def maximum(data: list) -> float:
    """
    Return max value using base Python iteration.
    Returns [] if input is empty (test-compatible behavior).
    """
    if not data:
        return []

    max_value = data[0]
    for value in data:
        if value > max_value:
            max_value = value
    return max_value


def variance(data: list) -> float:
    """
    Compute population variance using base Python iteration.
    Returns [] if input is empty (test-compatible behavior).
    """
    if not data:
        return []

    n = len(data)

    mean = 0
    for value in data:
        mean += value
    mean /= n

    sum_sq_diff = 0
    for value in data:
        sum_sq_diff += (value - mean) ** 2

    return round(sum_sq_diff / n, 2)


def standard_deviation(data: list) -> float:
    """
    Compute population standard deviation from variance().
    Returns [] if input is empty (test-compatible behavior).
    """
    if not data:
        return []

    return round(variance(data) ** 0.5, 2)
