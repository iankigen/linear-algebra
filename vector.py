import numpy


class Vector(object):
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension = len(coordinates)
		except ValueError:
			raise ValueError('The coordinates must be nonempty')
		except TypeError:
			raise TypeError('The coordinates must be an iterable')

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	def __eq__(self, vector):
		return self.coordinates == vector.coordinates

	def __add__(self, vector):
		return numpy.array(self.coordinates) + numpy.array(vector.coordinates)


my_vector = Vector([1, 2, 3])
print(my_vector)

my_vector1 = Vector([-1, 2, 3])
print(my_vector == my_vector1)

my_vector2 = Vector([1, 2, 3])
print(my_vector == my_vector2)

print(my_vector + my_vector1)
