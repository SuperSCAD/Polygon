from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad

from super_scad_polygon.SmoothRectangle import SmoothRectangle
from test.FilletFactory import FilletFactory
from test.ScadTestCase import ScadTestCase


class SmoothRectangleTest(ScadTestCase):
    """
    Tests cases for SmoothRectangle.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_smooth_rectangle(self) -> None:
        """
        Tests plain smooth rectangle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fa=1.0, fs=0.1))
        triangle = SmoothRectangle(width=20.0, depth=10, profile_factories=FilletFactory(radius=1.0))

        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------