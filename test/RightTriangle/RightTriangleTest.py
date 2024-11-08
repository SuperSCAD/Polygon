from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad

from super_scad_polygon.RightTriangle import RightTriangle
from test.ScadTestCase import ScadTestCase


class RightTriangleTest(ScadTestCase):
    """
    Tests cases for RightTriangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_right_triangle(self) -> None:
        """
        Tests plain right triangle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        triangle = RightTriangle(width=20.0, depth=10.0)

        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
