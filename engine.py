'''This module contains the gameplay'''

import logging
import sys

from models import Enemy, Player
import settings
from exeptions import EnemyDown, GameOver


logger = logging.getLogger('Engine')
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info('Hello, welcome! The WARRIORS, ROBBERS AND WIZARDS game has been started!')


def get_player_name():
    """Returns the player's name"""

    logger.info('ENTER YOUR NAME :')
    player_name = (input(str())).strip()
    player_name = player_name[0:20]
    while not player_name.isalpha():
        logger.info('Only letters are alowed')
        logger.info('ENTER YOUR NAME :')
        player_name = (input(str())).strip()
        player_name = player_name[0:20]
    return player_name

def play() -> None:
    """Play the game"""

    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy()
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown as exc:
            logger.info('')
            logger.info(exc)
            logger.info('ENEMY LEVEL %s IS DEFEATED!', enemy.level)
            logger.info('')
            enemy = Enemy(enemy.level + 1)
        except GameOver:
            logger.info('')
            logger.info('%s is defeated!', player_name)
            logger.info('SCORE POINTS: %s', player.score)
            with open(settings.FILENAME, 'a', encoding= settings.FILE_ENCODING) as fl_name:
                fl_name.write(player_name +  " " + str(player.score) + "\n")
            break
if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        logger.info('You press Ctrl + C and left the game')
        sys.exit()
