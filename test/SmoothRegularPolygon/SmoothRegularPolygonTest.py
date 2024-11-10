from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad_smooth_profile.RoughFactory import RoughFactory

from super_scad_polygon.SmoothRegularPolygon import SmoothRegularPolygon
from test.FilletFactory import FilletFactory
from test.ScadTestCase import ScadTestCase


class RegularPolygonTestCase(ScadTestCase):
    """
    Testcases for smooth regular polygons.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_square_inner_radius(self):
        """
        Test for a smooth regular polygon with test profile.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fa=1.0, fs=0.1))
        polygon = SmoothRegularPolygon(sides=7,
                                       size=10.0,
                                       profile_factories=FilletFactory(radius=1.0))

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
