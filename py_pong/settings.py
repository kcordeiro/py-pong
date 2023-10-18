"""Static constants.

If it's an arbitrary value that will not be changed at runtime, it
belongs here. All should be type-hinted.
"""
from dataclasses import dataclass
from random import choice
from typing import Tuple

# RGB values of colors used
BLACK: Tuple[int, int, int] = (0, 0, 0)
ORANGE: Tuple[int, int, int] = (255, 151, 112)
PINK: Tuple[int, int, int] = (255, 112, 166)

# Window size parameters
WINDOW_WIDTH: int = 900
WINDOW_HEIGHT: int = 600


@dataclass
class PlayerSettings:  # pylint: disable=too-many-instance-attributes
    """Dataclass to store settings for the player object."""

    name: str
    score_pos: int
    x_pos: int
    y_pos: int = 0
    y_dir: int = 0
    height: int = 100
    width: int = 10
    speed: int = 10
    score: int = 0
    color: Tuple[int, int, int] = PINK


@dataclass
class BallSettings:  # pylint: disable=too-many-instance-attributes
    """Dataclass to store settings for the ball object."""

    x_pos: float = WINDOW_WIDTH / 2.0
    y_pos: float = WINDOW_HEIGHT / 2.0
    x_dir: int = choice([-1, 1])
    y_dir: int = choice([-1, 1])
    radius: int = 10
    speed: int = 8
    score: int = 0
    color: Tuple[int, int, int] = ORANGE
