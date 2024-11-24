import math

from super_scad.boolean.Union import Union
from super_scad.d2.Circle import Circle
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit
from super_scad.transformation.Paint import Paint
from super_scad.type.Color import Color

from super_scad_polygon.RegularPolygon import RegularPolygon
from test.RegularPolygon.ImperialUnitPentagon import ImperialUnitPentagon
from test.ScadTestCase import ScadTestCase


class RegularPolygonTestCase(ScadTestCase):
    """
    Testcases for regular polygons.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes(self):
        """
        Test the size of a regular polygon.
        """
        polygon = RegularPolygon(sides=5, outer_radius=10.0)
        self.assertEqual(polygon.sides, 5)
        polygon = RegularPolygon(sides=5, outer_radius=10.0)
        self.assertAlmostEqual(polygon.outer_radius, 10.0)
        polygon = RegularPolygon(sides=5, outer_radius=10.0)
        self.assertAlmostEqual(polygon.outer_diameter, 20.0)
        polygon = RegularPolygon(sides=5, outer_radius=10.0)
        self.assertAlmostEqual(polygon.inner_radius, 8.0902, places=4)
        polygon = RegularPolygon(sides=5, outer_radius=10.0)
        self.assertAlmostEqual(polygon.inner_diameter, 16.1803, places=4)
        polygon = RegularPolygon(sides=5, outer_radius=10.0)
        self.assertAlmostEqual(polygon.side_length, 11.7557, places=4)

        polygon = RegularPolygon(sides=5, outer_diameter=20.0)
        self.assertEqual(polygon.sides, 5)
        polygon = RegularPolygon(sides=5, outer_diameter=20.0)
        self.assertAlmostEqual(polygon.outer_radius, 10.0)
        polygon = RegularPolygon(sides=5, outer_diameter=20.0)
        self.assertAlmostEqual(polygon.outer_diameter, 20.0)
        polygon = RegularPolygon(sides=5, outer_diameter=20.0)
        self.assertAlmostEqual(polygon.inner_radius, 8.0902, places=4)
        polygon = RegularPolygon(sides=5, outer_diameter=20.0)
        self.assertAlmostEqual(polygon.inner_diameter, 16.1803, places=4)
        polygon = RegularPolygon(sides=5, outer_diameter=20.0)
        self.assertAlmostEqual(polygon.side_length, 11.7557, places=4)

        polygon = RegularPolygon(sides=5, inner_radius=8.090169)
        self.assertEqual(polygon.sides, 5)
        polygon = RegularPolygon(sides=5, inner_radius=8.090169)
        self.assertAlmostEqual(polygon.outer_radius, 10.0, places=4)
        polygon = RegularPolygon(sides=5, inner_radius=8.090169)
        self.assertAlmostEqual(polygon.outer_diameter, 20.0, places=4)
        polygon = RegularPolygon(sides=5, inner_radius=8.090169)
        self.assertAlmostEqual(polygon.inner_radius, 8.0902, places=4)
        polygon = RegularPolygon(sides=5, inner_radius=8.090169)
        self.assertAlmostEqual(polygon.inner_diameter, 16.1803, places=4)
        polygon = RegularPolygon(sides=5, inner_radius=8.090169)
        self.assertAlmostEqual(polygon.side_length, 11.7557, places=4)
        polygon = RegularPolygon(sides=5, inner_radius=8.090169)

        polygon = RegularPolygon(sides=5, inner_diameter=16.180339)
        self.assertEqual(polygon.sides, 5)
        polygon = RegularPolygon(sides=5, inner_diameter=16.180339)
        self.assertAlmostEqual(polygon.outer_radius, 10.0, places=4)
        polygon = RegularPolygon(sides=5, inner_diameter=16.180339)
        self.assertAlmostEqual(polygon.outer_diameter, 20.0, places=4)
        polygon = RegularPolygon(sides=5, inner_diameter=16.180339)
        self.assertAlmostEqual(polygon.inner_radius, 8.0902, places=4)
        polygon = RegularPolygon(sides=5, inner_diameter=16.180339)
        self.assertAlmostEqual(polygon.inner_diameter, 16.1803, places=4)
        polygon = RegularPolygon(sides=5, inner_diameter=16.180339)
        self.assertAlmostEqual(polygon.side_length, 11.7557, places=4)

        polygon = RegularPolygon(sides=5, side_length=11.755705)
        self.assertEqual(polygon.sides, 5)
        polygon = RegularPolygon(sides=5, side_length=11.755705)
        self.assertAlmostEqual(polygon.outer_radius, 10.0, places=4)
        polygon = RegularPolygon(sides=5, side_length=11.755705)
        self.assertAlmostEqual(polygon.outer_diameter, 20.0, places=4)
        polygon = RegularPolygon(sides=5, side_length=11.755705)
        self.assertAlmostEqual(polygon.inner_radius, 8.0902, places=4)
        polygon = RegularPolygon(sides=5, side_length=11.755705)
        self.assertAlmostEqual(polygon.inner_diameter, 16.1803, places=4)
        polygon = RegularPolygon(sides=5, side_length=11.755705)
        self.assertAlmostEqual(polygon.side_length, 11.7557, places=4)

    # ------------------------------------------------------------------------------------------------------------------
    def test_square_inner_radius(self):
        """
        Test for a regular polygon defined by its inner radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        polygon = RegularPolygon(sides=4, inner_radius=1.0)

        self.assertAlmostEqual(1.0, polygon.inner_radius)
        self.assertAlmostEqual(math.sqrt(2.0), polygon.outer_radius)
        self.assertAlmostEqual(2.0, polygon.side_length)
        self.assertAlmostEqual(90.0, polygon.inner_angle)
        self.assertAlmostEqual(90.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(45.0, angles[0])
        self.assertAlmostEqual(315.0, angles[1])
        self.assertAlmostEqual(225.0, angles[2])
        self.assertAlmostEqual(135.0, angles[3])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_square_outer_radius(self):
        """
        Test for a regular polygon defined by its outer radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        polygon = RegularPolygon(sides=4, outer_radius=1.0)

        self.assertAlmostEqual(0.5 * math.sqrt(2.0), polygon.inner_radius)
        self.assertAlmostEqual(1.0, polygon.outer_radius)
        self.assertAlmostEqual(math.sqrt(2.0), polygon.side_length)
        self.assertAlmostEqual(90.0, polygon.inner_angle)
        self.assertAlmostEqual(90.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(45.0, angles[0])
        self.assertAlmostEqual(315.0, angles[1])
        self.assertAlmostEqual(225.0, angles[2])
        self.assertAlmostEqual(135.0, angles[3])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_square_size(self):
        """
        Test for a regular polygon defined by its side_length.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        polygon = RegularPolygon(sides=4, side_length=1.0)

        self.assertAlmostEqual(0.5, polygon.inner_radius)
        self.assertAlmostEqual(0.5 * math.sqrt(2.0), polygon.outer_radius)
        self.assertAlmostEqual(1.0, polygon.side_length)
        self.assertAlmostEqual(90.0, polygon.inner_angle)
        self.assertAlmostEqual(90.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(45.0, angles[0])
        self.assertAlmostEqual(315.0, angles[1])
        self.assertAlmostEqual(225.0, angles[2])
        self.assertAlmostEqual(135.0, angles[3])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_pentagon_inner_radius(self):
        """
        Test for a regular polygon defined by its inner radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        polygon = RegularPolygon(sides=5, inner_radius=1.0)

        self.assertAlmostEqual(1.0, polygon.inner_radius)
        self.assertAlmostEqual(2.0, polygon.inner_diameter)
        self.assertAlmostEqual(1.0 / math.cos(math.pi / 5), polygon.outer_radius)
        self.assertAlmostEqual(2.0 / math.cos(math.pi / 5), polygon.outer_diameter)
        self.assertAlmostEqual(2 * math.tan(math.pi / 5), polygon.side_length)
        self.assertAlmostEqual(108.0, polygon.inner_angle)
        self.assertAlmostEqual(72.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(90.0, angles[0])
        self.assertAlmostEqual(18.0, angles[1])
        self.assertAlmostEqual(306.0, angles[2])
        self.assertAlmostEqual(234.0, angles[3])
        self.assertAlmostEqual(162.0, angles[4])

        union = Union(children=[Paint(color=Color(color='blue'), child=Circle(radius=polygon.outer_radius, fn4n=True)),
                                Paint(color=Color(color='red'), child=polygon),
                                Paint(color=Color(color='green'),
                                      child=Circle(radius=polygon.inner_radius, fn4n=True))])

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_pentagon_inner_diameter(self):
        """
        Test for a regular polygon defined by its inner diameter.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        polygon = RegularPolygon(sides=5, inner_diameter=2.0)

        self.assertAlmostEqual(1.0, polygon.inner_radius)
        self.assertAlmostEqual(2.0, polygon.inner_diameter)
        self.assertAlmostEqual(1.0 / math.cos(math.pi / 5), polygon.outer_radius)
        self.assertAlmostEqual(2.0 / math.cos(math.pi / 5), polygon.outer_diameter)
        self.assertAlmostEqual(2 * math.tan(math.pi / 5), polygon.side_length)
        self.assertAlmostEqual(108.0, polygon.inner_angle)
        self.assertAlmostEqual(72.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(90.0, angles[0])
        self.assertAlmostEqual(18.0, angles[1])
        self.assertAlmostEqual(306.0, angles[2])
        self.assertAlmostEqual(234.0, angles[3])
        self.assertAlmostEqual(162.0, angles[4])

        union = Union(children=[Paint(color=Color(color='blue'), child=Circle(radius=polygon.outer_radius, fn4n=True)),
                                Paint(color=Color(color='red'), child=polygon),
                                Paint(color=Color(color='green'),
                                      child=Circle(radius=polygon.inner_radius, fn4n=True))])

        scad.run_super_scad(union, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_pentagon_outer_radius(self):
        """
        Test for a regular polygon defined by its outer radius.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        polygon = RegularPolygon(sides=5, outer_radius=1.0)

        self.assertAlmostEqual(1.0 * math.cos(math.pi / 5), polygon.inner_radius)
        self.assertAlmostEqual(2.0 * math.cos(math.pi / 5), polygon.inner_diameter)
        self.assertAlmostEqual(1.0, polygon.outer_radius)
        self.assertAlmostEqual(2.0, polygon.outer_diameter)
        self.assertAlmostEqual(2 * math.sin(math.pi / 5), polygon.side_length)
        self.assertAlmostEqual(108.0, polygon.inner_angle)
        self.assertAlmostEqual(72.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(90.0, angles[0])
        self.assertAlmostEqual(18.0, angles[1])
        self.assertAlmostEqual(306.0, angles[2])
        self.assertAlmostEqual(234.0, angles[3])
        self.assertAlmostEqual(162.0, angles[4])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_pentagon_outer_diameter(self):
        """
        Test for a regular polygon defined by its outer diameter.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        polygon = RegularPolygon(sides=5, outer_diameter=2.0)

        self.assertAlmostEqual(1.0 * math.cos(math.pi / 5), polygon.inner_radius)
        self.assertAlmostEqual(2.0 * math.cos(math.pi / 5), polygon.inner_diameter)
        self.assertAlmostEqual(1.0, polygon.outer_radius)
        self.assertAlmostEqual(2.0, polygon.outer_diameter)
        self.assertAlmostEqual(2 * math.sin(math.pi / 5), polygon.side_length)
        self.assertAlmostEqual(108.0, polygon.inner_angle)
        self.assertAlmostEqual(72.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(90.0, angles[0])
        self.assertAlmostEqual(18.0, angles[1])
        self.assertAlmostEqual(306.0, angles[2])
        self.assertAlmostEqual(234.0, angles[3])
        self.assertAlmostEqual(162.0, angles[4])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_pentagon_size(self):
        """
        Test for a regular polygon defined by its side_length.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        polygon = RegularPolygon(sides=5, side_length=1.0)

        self.assertAlmostEqual(1.0 / (2 * math.tan(math.pi / 5)), polygon.inner_radius)
        self.assertAlmostEqual(2.0 / (2 * math.tan(math.pi / 5)), polygon.inner_diameter)
        self.assertAlmostEqual(1.0 / (2 * math.sin(math.pi / 5)), polygon.outer_radius)
        self.assertAlmostEqual(2.0 / (2 * math.sin(math.pi / 5)), polygon.outer_diameter)
        self.assertAlmostEqual(1.0, polygon.side_length)
        self.assertAlmostEqual(108.0, polygon.inner_angle)
        self.assertAlmostEqual(72.0, polygon.exterior_angle)

        angles = polygon.angles
        self.assertAlmostEqual(90.0, angles[0])
        self.assertAlmostEqual(18.0, angles[1])
        self.assertAlmostEqual(306.0, angles[2])
        self.assertAlmostEqual(234.0, angles[3])
        self.assertAlmostEqual(162.0, angles[4])

        scad.run_super_scad(polygon, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def xtest_imperial_metric_pentagon_size(self):
        """
        Test for an imperial unit pentagon in metric units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        polygon = ImperialUnitPentagon()
        scad.run_super_scad(polygon, path_actual)

        self.assertAlmostEqual(25.4 / (2 * math.tan(math.pi / 5)), polygon.imperial_pentagon.inner_radius)
        self.assertAlmostEqual(25.4 / (math.tan(math.pi / 5)), polygon.imperial_pentagon.inner_diameter)
        self.assertAlmostEqual(25.4 / (2 * math.sin(math.pi / 5)), polygon.imperial_pentagon.outer_radius)
        self.assertAlmostEqual(25.4 / (math.sin(math.pi / 5)), polygon.imperial_pentagon.outer_diameter)
        self.assertAlmostEqual(25.4, polygon.imperial_pentagon.side_length)
        self.assertAlmostEqual(polygon.imperial_pentagon.nodes[0].y, polygon.imperial_pentagon.outer_radius)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_imperial_imperial_pentagon_size(self):
        """
        Test for an imperial unit pentagon in imperial units.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(unit_length_final=Unit.INCH))
        polygon = ImperialUnitPentagon()

        scad.run_super_scad(polygon, path_actual)

        self.assertAlmostEqual(1.0 / (2 * math.tan(math.pi / 5)), polygon.imperial_pentagon.inner_radius)
        self.assertAlmostEqual(2.0 / (2 * math.tan(math.pi / 5)), polygon.imperial_pentagon.inner_diameter)
        self.assertAlmostEqual(1.0 / (2 * math.sin(math.pi / 5)), polygon.imperial_pentagon.outer_radius)
        self.assertAlmostEqual(2.0 / (2 * math.sin(math.pi / 5)), polygon.imperial_pentagon.outer_diameter)
        self.assertAlmostEqual(1.0, polygon.imperial_pentagon.side_length)

        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
