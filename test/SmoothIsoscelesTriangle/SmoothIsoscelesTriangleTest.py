from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad_smooth_profiles.Fillet import Fillet

from super_scad_polygon.SmoothIsoscelesTriangle import SmoothIsoscelesTriangle
from test.ScadTestCase import ScadTestCase


class SmoothIsoscelesTriangleTest(ScadTestCase):
    """
    Tests cases for SmoothIsoscelesTriangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_smooth_isosceles_triangle(self) -> None:
        """
        Tests plain smooth isosceles triangle.
        """
        scad = Scad(context=Context(fa=1.0, fs=0.1, eps=0.1))
        triangle = SmoothIsoscelesTriangle(width=6.0,
                                           depth=4.0,
                                           profiles=Fillet(radius=0.5),
                                           extend_by_eps_sides={2})

        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
