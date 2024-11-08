from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad

from super_scad_polygon.SmoothRightTriangle import SmoothRightTriangle
from test.FilletFactory import FilletFactory
from test.ScadTestCase import ScadTestCase


class SmoothRightTriangleTest(ScadTestCase):
    """
    Tests cases for SmoothRightTriangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_smooth_right_triangle(self) -> None:
        """
        Tests plain smooth right triangle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fa=1.0, fs=0.1))
        triangle = SmoothRightTriangle(width=20.0, depth=10.0, profile_factories=FilletFactory(radius=1.0))

        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
