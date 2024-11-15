from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad

from super_scad_polygon.IsoscelesTriangle import IsoscelesTriangle
from test.ScadTestCase import ScadTestCase


class IsoscelesTriangleTest(ScadTestCase):
    """
    Tests cases for IsoscelesTriangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_isosceles_triangle(self) -> None:
        """
        Tests plain isosceles triangle.
        """
        context = Context(eps=0.1)
        scad = Scad(context=context)
        triangle = IsoscelesTriangle(width=6.0, depth=4.0, extend_sides_by_eps={2})

        self.assertAlmostEqual(triangle.width, 6.0)
        self.assertAlmostEqual(triangle.depth, 4.0)
        self.assertAlmostEqual(triangle.isosceles_length, 5.0)
        self.assertAlmostEqual(triangle.center_point.x, 3.0)
        self.assertAlmostEqual(triangle.center_point.y, triangle.depth / 3.0)

        nodes = triangle.nodes
        self.assertAlmostEqual((nodes[0] - nodes[1]).length, 5.0)
        self.assertAlmostEqual((nodes[1] - nodes[2]).length, 5.0)
        self.assertAlmostEqual((nodes[2] - nodes[0]).length, 6.0)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_centered_isosceles_triangle(self) -> None:
        """
        Tests plain isosceles triangle.
        """
        context = Context(eps=0.1)
        scad = Scad(context=context)
        triangle = IsoscelesTriangle(width=6.0, isosceles_length=5.0, center=True)

        self.assertAlmostEqual(triangle.width, 6.0)
        self.assertAlmostEqual(triangle.depth, 4.0)
        self.assertAlmostEqual(triangle.isosceles_length, 5.0)
        self.assertAlmostEqual(triangle.center_point.x, 0.0)
        self.assertAlmostEqual(triangle.center_point.y, 0.0)

        nodes = triangle.nodes
        self.assertAlmostEqual((nodes[0] - nodes[1]).length, 5.0)
        self.assertAlmostEqual((nodes[1] - nodes[2]).length, 5.0)
        self.assertAlmostEqual((nodes[2] - nodes[0]).length, 6.0)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
