from typing import List


class Player:
    # __hand: List[int]

    def __init__(self, player_id: int, game_score=0, round_score=0):
        self.__id = player_id
        self.hand = []
        self.game_score = game_score
        self.round_score = round_score

    @property
    def id(self):
        return self.__id

    # @hand.setter
    # def hand(self, new_hand):
    #     self.__hand = new_hand

    def available_actions(self) -> List[int]:
        return self.hand
