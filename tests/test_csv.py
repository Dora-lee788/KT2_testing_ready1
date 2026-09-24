from pathlib import Path

import pytest

from src.csv_analysis import calculate_average, find_errors


DATA = Path(__file__).resolve().parents[1] / "data"


def test_original_csv_contains_error():
    assert find_errors(DATA / "grades_original.csv") == [10]


def test_broken_csv_raises_error():
    with pytest.raises(ValueError):
        calculate_average(DATA / "grades_original.csv")


def test_average_final():
    assert calculate_average(DATA / "grades.csv") == pytest.approx(53.0)
