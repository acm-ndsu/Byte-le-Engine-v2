import unittest

from game.utils.vector import Vector
import game.test_suite.utils

class TestVector(unittest.TestCase):
    """
    `Test Vector Notes:`

        This class tests the different methods in the Vector class.
    """

    def setUp(self) -> None:
        self.vector1: Vector = Vector(8, 10)
        self.vector2: Vector = Vector(x=5, y=5)
        self.utils = game.test_suite.utils

    # test sets
    def test_vector_set_x(self) -> None:
        self.vector1.x = 5
        self.assertEqual(self.vector1.x, 5)

    def test_vector_set_x_fail(self) -> None:
        with self.assertRaises(ValueError) as e:
            self.vector1.x = 'test'
        self.assertTrue(self.utils.spell_check(str(e.exception), f'The given x value, {"test"}, is not an integer.', False))

    def test_vector_set_y(self) -> None:
        self.vector1.y = 5
        self.assertEqual(self.vector1.y, 5)

    def test_vector_set_y_fail(self) -> None:
        with self.assertRaises(ValueError) as e:
            self.vector1.y = 'test'
        self.assertTrue(self.utils.spell_check(str(e.exception), f'The given y value, {"test"}, is not an integer.', False))

    def test_from_xy_tuple(self) -> None:
        self.assertEqual(Vector.from_xy_tuple((8, 10)), self.vector1)

    def test_from_yx_tuple(self) -> None:
        self.assertEqual(Vector.from_yx_tuple((10, 8)), self.vector1)

    def test_add_vectors(self) -> None:
        self.assertEqual(Vector.add_vectors(self.vector1, self.vector2), Vector(13, 15))

    def test_add_to_vector(self) -> None:
        self.assertEqual(self.vector1.add_to_vector(self.vector2), Vector(13, 15))

    def test_add_x_y(self) -> None:
        self.assertEqual(self.vector1.add_x_y(5, 5), Vector(13, 15))

    

