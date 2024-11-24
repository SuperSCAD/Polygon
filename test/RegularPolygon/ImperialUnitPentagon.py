from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.scad.Unit import Unit

from super_scad_polygon.RegularPolygon import RegularPolygon


class ImperialUnitPentagon(ScadWidget):
    """
    Class for an imperial unit pentagon.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self) -> None:
        """
        Object constructor.
        """
        ScadWidget.__init__(self)

        self.imperial_pentagon: RegularPolygon | None = None
        """
        The imperial pentagon.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Context.set_unit_length_current(Unit.INCH)

        self.imperial_pentagon = RegularPolygon(side_length=1.0, sides=5)
        len(self.imperial_pentagon.nodes)  # Force calculation of the nodes in inches.

        return self.imperial_pentagon

# ----------------------------------------------------------------------------------------------------------------------
