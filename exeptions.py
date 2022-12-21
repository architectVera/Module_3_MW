"""This module contains the playing exception."""

class EnemyDown(Exception):
    """Class implements EnemyDown."""

    def __init__(self, message: str) -> None:
        """
            Initialize instance

        :param message: usually settings.MSG_EnemyDown
        """
        self.message = message

    def __str__(self) -> str:
        """Return a string representation  of instance  EnemyDown class"""

        return self.message


class GameOver(Exception):
    """Class implements GameOverError"""

    def __init__(self, message: str) -> None:
        """
            Initialize instance

        :param message: usually settings.MSG_GAMEOVER,
        """
        self.message = message

    def __str__(self) -> str:
        """Return a string representation  of instance  GameOverError  class"""
        return self.message
