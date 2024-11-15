import math

from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad

from super_scad_polygon.EquilateralTriangle import EquilateralTriangle
from test.ScadTestCase import ScadTestCase


class EquilateralTriangleTest(ScadTestCase):
    """
    Tests cases for EquilateralTriangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_equilateral_triangle(self) -> None:
        """
        Tests plain equilateral triangle.
        """
        context = Context(eps=0.1)
        scad = Scad(context=context)
        triangle = EquilateralTriangle(side_length=5.0, extend_sides_by_eps={2})

        self.assertAlmostEqual(triangle.depth, 0.5 * math.sqrt(3.0) * 5.0)
        self.assertAlmostEqual(triangle.center_point.x, 2.5)
        self.assertAlmostEqual(triangle.center_point.y, triangle.depth / 3.0)

        inner_angles = triangle.inner_angles(context=context)
        self.assertAlmostEqual(inner_angles[0], 60.0)
        self.assertAlmostEqual(inner_angles[1], 60.0)
        self.assertAlmostEqual(inner_angles[2], 60.0)

        nodes = triangle.nodes
        self.assertAlmostEqual((nodes[0] - nodes[1]).length, 5.0)
        self.assertAlmostEqual((nodes[1] - nodes[2]).length, 5.0)
        self.assertAlmostEqual((nodes[2] - nodes[0]).length, 5.0)


        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_equilateral_triangle(self) -> None:
        """
        Tests plain equilateral triangle.
        """
        context = Context(eps=0.1)
        scad = Scad(context=context)
        triangle = EquilateralTriangle(depth=0.5 * math.sqrt(3.0) * 5.0, center=True)

        self.assertAlmostEqual(triangle.side_length, 5.0)
        self.assertAlmostEqual(triangle.center_point.x, 0.0)
        self.assertAlmostEqual(triangle.center_point.y, 0.0)

        inner_angles = triangle.inner_angles(context=context)
        self.assertAlmostEqual(inner_angles[0], 60.0)
        self.assertAlmostEqual(inner_angles[1], 60.0)
        self.assertAlmostEqual(inner_angles[2], 60.0)

        nodes = triangle.nodes
        self.assertAlmostEqual((nodes[0] - nodes[1]).length, 5.0)
        self.assertAlmostEqual((nodes[1] - nodes[2]).length, 5.0)
        self.assertAlmostEqual((nodes[2] - nodes[0]).length, 5.0)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
