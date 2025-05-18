from super_scad.boolean.Union import Union
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.transformation.Paint import Paint
from super_scad.type import Vector2
from super_scad.type.Color import Color
from super_scad_smooth_profile.Rough import Rough
from super_scad_smooth_profiles.Fillet import Fillet

from super_scad_polygon.SmoothPolygon import SmoothPolygon
from test.ScadTestCase import ScadTestCase


class PolygonTestCase(ScadTestCase):
    """
    Testcases for smooth polygons.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_profiles(self):
        """
        Test profiles.
        """
        points = [Vector2(-1.0, -1.0), Vector2(-1.0, 1.0), Vector2(1.0, 1.0), Vector2(1.0, -1.0)]

        # Default profile is rough.
        polygon = SmoothPolygon(points=points)
        profiles = polygon.profiles
        self.assertEqual(4, len(profiles))
        for index in range(len(profiles)):
            profile = profiles[index]
            self.assertIsInstance(profile, Rough)

        # One profile is repeated.
        polygon = SmoothPolygon(points=points, profiles=Fillet(radius=1.0))
        profiles = polygon.profiles
        self.assertEqual(4, len(profiles))
        for index in range(len(profiles)):
            profile = profiles[index]
            self.assertIsInstance(profile, Fillet)

        # List of profiles is extended.
        polygon = SmoothPolygon(points=points, profiles=[Rough(), Fillet(radius=1.0)])
        profiles = polygon.profiles
        self.assertEqual(4, len(profiles))
        self.assertIsInstance(profiles[0], Rough)
        self.assertIsInstance(profiles[1], Fillet)
        for index in range(2, len(profiles)):
            self.assertIsInstance(profiles[0], Rough)

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_polygon(self):
        """
        Test for a smooth polygon with test profile.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fa=1.0, fs=0.1))

        points = [Vector2(0, 20.0), Vector2(10.0, 0.0), Vector2(0.0, 10.0), Vector2(-10.0, 0.0)]
        polygon = SmoothPolygon(points=points, profiles=Fillet(radius=1.0))

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_smooth_polygon_and_extend(self):
        """
        Test for a smooth polygon with test profile.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fa=1.0, fs=0.1, eps=0.1))

        points = [Vector2(0.0, 6.0), Vector2(10.0, 0.0), Vector2(-10.0, 0.0)]
        polygon1 = SmoothPolygon(points=points,
                                 profiles=Fillet(radius=1.0),
                                 extend_by_eps_sides={1})
        polygon2 = SmoothPolygon(points=points,
                                 profiles=Fillet(radius=1.0))

        polygons = Union(children=[Paint(color=Color('red'), child=polygon1),
                                   polygon2])

        scad.run_super_scad(polygons, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
