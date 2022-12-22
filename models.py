"""This module contains the Enemy class and the Player class."""

import logging
import random

import settings
from exeptions import EnemyDown, GameOver

logger = logging.getLogger("Models")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


class Enemy:
    """Describes the playing enemy-bot"""

    def __init__(self,level: int = 1):
        """
        Initialize instance

        level: int
        health_point_enemy: int
        """

        self.level = level
        self.health_point_enemy = self.level

    def __repr__(self):
        """Return a string representation of an instance"""

        return f'Class Enemy, level = {self.level}, health point = {self.level}'

    def descrease_health(self):
        """Method decreases the health points value by 1 (one)"""

        self.health_point_enemy -= settings.STEP_SCORE
        if self.health_point_enemy < settings.ENEMY_HEALTH_DOWN:
            raise EnemyDown(settings.MSG_ENEMYDOWN)

        return self.health_point_enemy - settings.STEP_SCORE

    def select_attack(self):
        """Return a random attack choice from valid choices"""

        variants_of_heroes = [settings.WARRIOR, settings.ROBBER, settings.WIZARD]
        enemy_choice_attack = random.choice(variants_of_heroes)
        logger.info("Enemy chosen is %s", enemy_choice_attack)
        return enemy_choice_attack

    def select_defence(self):
        """Return a random defence choice from valid choices"""

        variants_of_heroes = [settings.WARRIOR, settings.ROBBER, settings.WIZARD]
        enemy_choice_defence = random.choice(variants_of_heroes)
        logger.info("Enemy chosen is %s", enemy_choice_defence)
        return enemy_choice_defence


class Player:
    """Describes the choice of user"""

    def __init__(self,name: str):
        """Initialize instance"""

        self.name = name
        self.health_point_player = settings.INITIAL_PLAYERS_HEALTH
        self.score = 0

    def __repr__(self):
        """Return a string representation of an instance"""

        return f'Player (name = {self.name}, score = {self.score})'

    def add_score(self,score: int):
        """Add score points"""

        self.score += score

    def decrease_health(self):
        """Method decreases the health points value by 1 (one)"""

        self.health_point_player -= settings.STEP_SCORE
        if self.health_point_player < settings.ENEMY_HEALTH_DOWN:
            raise GameOver(settings.MSG_GAMEOVER)

    def select_attack(self):
        """Return a fight choice made by the user"""

        player_choice_attack = None
        while player_choice_attack not in [settings.WARRIOR, settings.ROBBER, settings.WIZARD]:
            player_choice_attack = input(
                'MAKE A FIGHT CHOISE FROM (WARRIOR - 1, ROBBER - 2, WIZARD - 3): '
            )
        return player_choice_attack

    def select_defence(self):
        """	Return a fight choice made by the user"""

        player_choice_defence = None

        while player_choice_defence not in [settings.WARRIOR,  settings.ROBBER, settings.WIZARD]:
            player_choice_defence = input(
                'MAKE A FIGHT CHOISE FROM (WARRIOR - 1, ROBBER - 2, WIZARD - 3): '
            )
        return player_choice_defence

    @staticmethod
    def fight(attack, defence):
        """Performs fight result calculation"""

        if attack == defence:
            result = settings.DRAW
        if attack == settings.WARRIOR and defence == settings.ROBBER\
                or attack == settings.ROBBER and defence == settings.WIZARD\
                or attack == settings.WIZARD and defence == settings.WARRIOR:
            result = settings.SUCCESS
        else:
            result = settings.FAILURE
        return result
#
    def attack(self, enemy: Enemy) -> None:
        """Attack on enemy"""

        logger.info("Your attack!")
        attack = self.select_attack()
        defence = enemy.select_defence()
        fight_result = self.fight(attack, defence)
        if fight_result == settings.SUCCESS:
            logger.info(settings.SUCCESS_ATTACK)
            try:
                enemy.descrease_health()
                self.add_score(settings.SCORE_FOR_SUCCESS)
                logger.info('Your score is %s', self.score)
            except EnemyDown:
                self.add_score(settings.SCORE_FOR_DEFETING_THE_ENEMY)
                raise

        elif fight_result == settings.FAILURE:
            logger.info(settings.FAILURE_ATTACK)
            try:
                self.decrease_health()
                logger.info('Your health is %s', self.health_point_player)
            except GameOver:
                logger.info('')
                logger.info(settings.MSG_GAMEOVER)
                raise
        elif fight_result == settings.DRAW:
            logger.info(settings.DRAW_MSG)

    def defence(self,  enemy: Enemy) -> None:
        """Perform defence from an enemy attack"""

        logger.info("Your defence!")
        defence = self.select_defence()
        attack = enemy.select_defence()
        fight_result = self.fight(attack, defence)

        if fight_result == settings.SUCCESS:
            logger.info(settings.FAILURE_DEFENCE)
            try:
                self.decrease_health()
                logger.info('Your health is %s', self.health_point_player)
            except GameOver:
                logger.info('')
                logger.info(settings.MSG_GAMEOVER)
                raise

        elif fight_result == settings.FAILURE:
            logger.info(settings.SUCCESS_DEFENCE)
            try:
                enemy.descrease_health()
                self.add_score(settings.SCORE_FOR_SUCCESS)
                logger.info('Your score is %s', self.score)
            except EnemyDown:
                self.add_score(settings.SCORE_FOR_DEFETING_THE_ENEMY)
                raise

        elif fight_result == settings.DRAW:
            logger.info(settings.DRAW_MSG)
