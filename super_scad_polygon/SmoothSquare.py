from typing import List

from super_scad.d2.Square import Square
from super_scad_smooth_profile.SmoothProfileFactory import SmoothProfileFactory

from super_scad_polygon.SmoothPolygonMixin import SmoothPolygonMixin


class SmoothSquare(SmoothPolygonMixin, Square):
    """
    A widget for right triangles with smooth corners.
    """

    # ----------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 size: float,
                 profile_factories: SmoothProfileFactory | List[SmoothProfileFactory] | None = None):
        """
        Object constructor.

        :param size: The side_length of the square.
        :param profile_factories: The profile factories to be applied at nodes of the right triangle. When a single
                                  profile factory is given, this profile will be applied at all nodes.
        """
        SmoothPolygonMixin.__init__(self, profile_factories=profile_factories)
        Square.__init__(self, size=size)

# ----------------------------------------------------------------------------------------------------------------------
