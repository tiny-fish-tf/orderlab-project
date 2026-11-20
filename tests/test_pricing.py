# tests/test_pricing.py
import pytest

from orderlab.pricing import final_total, subtotal


def test_subtotal_normal():
    assert subtotal(10_000, 2) == 30_000


def test_subtotal_zero():
    assert subtotal(0, 3) == 0


def test_subtotal_negative():
    with pytest.raises(ValueError):
        subtotal(-100, 2)


def test_discount_below_zero():
    with pytest.raises(ValueError):
        final_total(10_000, 2, -1)


def test_discount_over_100():
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10_000, 2, 101)