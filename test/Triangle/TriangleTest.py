import math

from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.type.Vector2 import Vector2

from super_scad_polygon.Triangle import Triangle
from test.ScadTestCase import ScadTestCase


class TriangleTest(ScadTestCase):
    """
    Tests cases for Triangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_triangle_from_3_lengths(self) -> None:
        """
        Tests triangle from 3 lengths.
        """
        scad = Scad(context=Context())
        triangle = Triangle(length_a=10.0, length_b=15.0, length_c=20.0)

        nodes = triangle.nodes
        self.assertAlmostEqual((nodes[2] - nodes[0]).length, 10.0)
        self.assertAlmostEqual((nodes[0] - nodes[1]).length, 15.0)
        self.assertAlmostEqual((nodes[1] - nodes[2]).length, 20.0)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_triangle_from_2_lengths_and_angle_a(self) -> None:
        """
        Tests triangle from 2 lengths adn one angle_a.
        """
        scad = Scad(context=Context(eps=0.1))
        triangle = Triangle(length_b=5.0, length_c=5.0, angle_a=2.0 * math.degrees(math.acos(4.0 / 5.0)))

        nodes = triangle.nodes
        self.assertAlmostEqual((nodes[2] - nodes[0]).length, 6.0)
        self.assertAlmostEqual((nodes[0] - nodes[1]).length, 5.0)
        self.assertAlmostEqual((nodes[1] - nodes[2]).length, 5.0)

        self.assertAlmostEqual(triangle.center_point.x, 3.0)
        self.assertAlmostEqual(triangle.center_point.y, 4.0 / 3.0)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_triangle_from_2_lengths_and_angle_b(self) -> None:
        """
        Tests triangle from 2 lengths adn one angle_b.
        """
        scad = Scad(context=Context(eps=0.1))
        triangle = Triangle(length_a=6.0, length_c=5.0, angle_b=math.degrees(math.acos(3.0 / 5.0)),
                            extend_sides_by_eps={2})

        nodes = triangle.nodes
        self.assertAlmostEqual((nodes[2] - nodes[0]).length, 6.0)
        self.assertAlmostEqual((nodes[0] - nodes[1]).length, 5.0)
        self.assertAlmostEqual((nodes[1] - nodes[2]).length, 5.0)

        self.assertAlmostEqual(triangle.center_point.x, 3.0)
        self.assertAlmostEqual(triangle.center_point.y, 4.0 / 3.0)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_triangle_from_2_lengths_and_angle_c(self) -> None:
        """
        Tests triangle from 2 lengths adn one angle_c.
        """
        scad = Scad(context=Context(eps=0.1))
        triangle = Triangle(length_a=6.0, length_b=5.0, angle_c=math.degrees(math.acos(3.0 / 5.0)),
                            extend_sides_by_eps={2})

        nodes = triangle.nodes
        self.assertAlmostEqual((nodes[2] - nodes[0]).length, 6.0)
        self.assertAlmostEqual((nodes[0] - nodes[1]).length, 5.0)
        self.assertAlmostEqual((nodes[1] - nodes[2]).length, 5.0)

        self.assertAlmostEqual(triangle.center_point.x, 3.0)
        self.assertAlmostEqual(triangle.center_point.y, 4.0 / 3.0)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_triangle_from_nodes(self) -> None:
        """
        Tests triangle from nodes.
        """
        scad = Scad(context=Context(eps=0.1))
        triangle = Triangle(nodes=[Vector2(1.0, 1.0), Vector2(4.0, 5.0), Vector2(7.0, 1.0)], extend_sides_by_eps={2})

        nodes = triangle.nodes
        self.assertAlmostEqual((nodes[2] - nodes[0]).length, 6.0)
        self.assertAlmostEqual((nodes[0] - nodes[1]).length, 5.0)
        self.assertAlmostEqual((nodes[1] - nodes[2]).length, 5.0)

        self.assertAlmostEqual(triangle.center_point.x, 4.0)
        self.assertAlmostEqual(triangle.center_point.y, 1 + 4.0 / 3.0)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
