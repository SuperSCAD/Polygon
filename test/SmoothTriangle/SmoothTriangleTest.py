from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad_smooth_profiles.Fillet import Fillet

from super_scad_polygon.SmoothTriangle import SmoothTriangle
from test.ScadTestCase import ScadTestCase


class SmoothTriangleTest(ScadTestCase):
    """
    Tests cases for SmoothTriangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_smooth_triangle(self) -> None:
        """
        Tests plain smooth right triangle.
        """
        scad = Scad(context=Context(fa=1.0, fs=0.1, eps=0.1))
        triangle = SmoothTriangle(length_a=10.0,
                                  length_b=20.0,
                                  length_c=15.0,
                                  profiles=Fillet(radius=1.0),
                                  extend_by_eps_sides={2})

        path_actual, path_expected = self.paths()
        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
