"""
Complex number function

To declare complex number Real+Imaginary*j,
use A = ComplexNum(Real, Imaginary)

Basic arithmetic function works on A

Version
V1.0    JS  Initial version, contains basic functionality

"""
import math
from math import copysign

class ComplexNum:
	def __init__(self, real, imag = 0):
		self.real = real
		self.imag = imag

	def __str__(self):
		if copysign(1,self.imag) == 1:
			return f"{self.real}+j{self.imag}"
		else:
			return f"{self.real}-j{abs(self.imag)}"

	def __add__(self, other):
		return ComplexNum(self.real + other.real, self.imag + other.imag)

	def __sub__(self, other):
		return ComplexNum(self.real - other.real, self.imag - other.imag)

	def __mul__(self, other):
		return ComplexNum(self.real * other.real - self.imag * other.imag,
						  self.real * other.imag + self.imag * other.real)

	def __truediv__(self, other):
		return ComplexNum((self.real * other.real + self.imag * other.imag)/(other.real**2+ other.imag**2),
						  (self.imag * other.real - self.real * other.imag)/(other.real**2+ other.imag**2))

