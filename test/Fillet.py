import math
from typing import Tuple

from super_scad.scad.ScadWidget import ScadWidget
from super_scad_smooth_profile.SmoothProfile2D import SmoothProfile2D
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams

from test.FilletWidget import FilletWidget


class Fillet(SmoothProfile2D):
    """
    A profile that produces fillet smoothing profile widgets.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, radius: float):
        """
        Object constructor.

        :param radius: The radius of the fillet.
        """
        self._radius = radius
        """
        The radius of the fillet.
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def is_external(self) -> bool:
        """
        Returns whether the fillet is an external fillet.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def is_internal(self) -> bool:
        """
        Returns whether the fillet is an internal fillet.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def convexity(self) -> int | None:
        """
        Return the convexity of the profile.
        """
        return 2

    # ------------------------------------------------------------------------------------------------------------------
    def offset1(self, *, inner_angle: float) -> float:
        """
        Returns the offset of the smooth profile on the first vertex of the node.

        :param inner_angle: Inner angle between the two vertices of the node.
        """
        if self._radius > 0.0 and inner_angle < 180.0:
            # The corner is convex.
            alpha = math.radians(inner_angle) / 2.0

            return self._radius * math.cos(alpha) / math.sin(alpha)

        if self._radius > 0.0 and inner_angle > 180.0:
            # The corner is concave.
            alpha = math.radians(360.0 - inner_angle) / 2.0

            return self._radius * math.cos(alpha) / math.sin(alpha)

        if self._radius < 0.0:
            # Negative radius.
            return self._radius

        return 0.0

    # ------------------------------------------------------------------------------------------------------------------
    def offset2(self, *, inner_angle: float) -> float:
        """
        Returns the offset of the smooth profile on the second vertex of the node.

        :param inner_angle: Inner angle between the two vertices of the node.
        """
        return self.offset1(inner_angle=inner_angle)

    # ------------------------------------------------------------------------------------------------------------------
    def create_smooth_profiles(self, *, params: SmoothProfileParams) -> Tuple[ScadWidget | None, ScadWidget | None]:
        """
        Returns a smoothing profile widget creating a fillet.

        :param params: The parameters for the smooth profile widget.
        """
        if self._radius == 0.0 or self._radius > 0.0 and params.inner_angle == 180.0:
            return None, None

        widget = FilletWidget(radius=self._radius,
                              inner_angle=params.inner_angle,
                              normal_angle=params.normal_angle,
                              position=params.position)

        if self._radius > 0.0 and params.inner_angle < 180.0:
            return widget, None

        return None, widget

# ----------------------------------------------------------------------------------------------------------------------
