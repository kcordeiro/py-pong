"""Py-Pong game runner. Configures and runs game window and game objects."""
import sys

import pygame

from py_pong.components.ball import Ball
from py_pong.components.player import Player
from py_pong.settings import BLACK
from py_pong.settings import PlayerSettings
from py_pong.settings import WINDOW_HEIGHT
from py_pong.settings import WINDOW_WIDTH


class GameRunner:
    """Pong game runner class. Handles game objects."""

    def __init__(self) -> None:
        """Initialize the game window and objects."""
        pygame.init()
        self.clock = pygame.time.Clock()

        # Display the game window
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Py-Pong")

        # Instantiate the two players and the ball
        self.player_1 = Player(
            self.window, PlayerSettings(name="Player 1", score_pos=100, x_pos=20)
        )
        self.player_2 = Player(
            self.window,
            PlayerSettings(
                name="Player 2", score_pos=WINDOW_WIDTH - 100, x_pos=WINDOW_WIDTH - 30
            ),
        )
        self.ball = Ball(self.window)

    def event_handler(self) -> None:
        """Handle game inputs."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player_1.data.y_dir = -1
                if event.key == pygame.K_s:
                    self.player_1.data.y_dir = 1
                if event.key == pygame.K_UP:
                    self.player_2.data.y_dir = -1
                if event.key == pygame.K_DOWN:
                    self.player_2.data.y_dir = 1
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_s]:
                    self.player_1.data.y_dir = 0
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    self.player_2.data.y_dir = 0

    def _check_collisions(self) -> None:
        """Check if the ball collided with either player paddle."""
        for player in [self.player_1, self.player_2]:
            if pygame.Rect.colliderect(self.ball.ball, player.pad_rect):
                self.ball.hit()

    def _check_for_score(self) -> None:
        """Check if either player has scored a goal."""
        # If the ball is off the window to the right, player 1 scored
        if self.ball.data.x_pos >= WINDOW_WIDTH:
            self.player_1.data.score += 1
            self.ball.reset()
        # If the ball is off the window to the left, player 2 scored
        if self.ball.data.x_pos <= 0:
            self.player_2.data.score += 1
            self.ball.reset()
        # If neither, no one scored

    def _update_display(self) -> None:
        """Update the positions of the objects in the game window."""
        self.player_1.display()
        self.player_2.display()
        self.ball.display()

        # Update the score display
        self.player_1.update_score()
        self.player_2.update_score()

        pygame.display.update()

    def run_game(self) -> None:
        """Handle the operations that run the game."""
        while True:
            # Fill the background
            self.window.fill(BLACK)
            # Handle user inputs
            self.event_handler()
            # Check if the ball hit a player paddle
            self._check_collisions()

            # Update game object positions in their respective dataclasses
            self.player_1.update()
            self.player_2.update()
            self.ball.update()
            # Check if either player scored a goal
            self._check_for_score()

            # Update everything displayed on the screen at 30 FPS
            self._update_display()
            self.clock.tick(30)


def main() -> None:
    """Allows for access on the commandline with the `py-game` command."""
    pong = GameRunner()
    pong.run_game()


if __name__ == "__main__":
    main()
