from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad

from super_scad_polygon.SmoothSquare import SmoothSquare
from test.FilletFactory import FilletFactory
from test.ScadTestCase import ScadTestCase


class SmoothSquareTest(ScadTestCase):
    """
    Tests cases for SmoothSquare.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_smooth_square(self) -> None:
        """
        Tests plain smooth square.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fa=1.0, fs=0.1))
        triangle = SmoothSquare(size=15.0, profile_factories=FilletFactory(radius=1.0))

        scad.run_super_scad(triangle, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
