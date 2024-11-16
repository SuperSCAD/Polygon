from super_scad.boolean.Union import Union
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color
from super_scad_smooth_profile.Rough import Rough

from super_scad_polygon.SmoothRegularPolygon import SmoothRegularPolygon
from test.Fillet import Fillet
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
                                       side_length=10.0,
                                       profiles=Fillet(radius=1.0))

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_hexagon_extended(self):
        """
        Test a smooth and extended hexagon.
        """
        scad = Scad(context=Context(fa=1.0, fs=0.1, eps=0.1))

        hexagon1 = SmoothRegularPolygon(sides=6,
                                        outer_diameter=10.0,
                                        profiles=[Fillet(radius=1.0),
                                                  Fillet(radius=1.0),
                                                  Rough(),
                                                  Fillet(radius=1.0),
                                                  Fillet(radius=1.0)],
                                        extend_sides_by_eps=True)
        hexagon2 = SmoothRegularPolygon(sides=6,
                                        outer_diameter=10.0,
                                        profiles=[Fillet(radius=1.0),
                                                  Fillet(radius=1.0),
                                                  Rough(),
                                                  Fillet(radius=1.0),
                                                  Fillet(radius=1.0), ])

        hexagons = Union(children=[Paint(color=Color('red'), child=hexagon1),
                                   hexagon2])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(hexagons, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
