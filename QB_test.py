"""
Basic test for module ComplexNum.py
Requires module pytest

Version
V1.0    JS  Initial version

"""

import pytest
from ComplexNum import ComplexNum

ComplexNum1Real = 1
ComplexNum1Imag = 2
ComplexNum2Real = -3
ComplexNum2Imag = -4
ComplexNumber1 = ComplexNum(ComplexNum1Real,ComplexNum1Imag)
ComplexNumber2 = ComplexNum(ComplexNum2Real,ComplexNum2Imag)


def test_CompexNumPos():
    ComplexNumber1 = ComplexNum(ComplexNum1Real,ComplexNum1Imag)
    assert str(ComplexNumber1) == "1+j2"

def test_CompexNumNeg():
    ComplexNumber2 = ComplexNum(ComplexNum2Real,ComplexNum2Imag)
    assert str(ComplexNumber2) == "-3-j4"

def test_add():
    value = ComplexNumber1+ComplexNumber2
    assert str(value) == "-2-j2"

def test_subtract():
    value = ComplexNumber1-ComplexNumber2
    assert str(value)  == "4+j6"

def test_multiply():
    value = ComplexNumber1*ComplexNumber2
    assert str(value)  == "5-j10"

def test_divide():
    value = ComplexNumber1/ComplexNumber2
    assert str(value)  == "-0.44-j0.08"