import random


class SnakeAndLadder:

    def __init__(self):
        self.snake_dict = {
            99: 5,
            45: 10,
            32: 12,
            20: 1
        }
        self.ladder_dict = {
            21: 7,
            42: 32,
            94: 2,
            13: 22
        }

    def dice(self):
        """
        dice rolls and give value between 1 to 6
        :return: number from 1 to 6
        """
        return random.randint(1, 6)

    def snake(self, position):
        """

        :param position:player current position
        :return: player position after beaten  by Snake
        """

        if position in self.snake_dict:
            position = position - self.snake_dict.get(position)
        return position

    def ladder(self, position):
        """

        :param position:player current position
        :return: player position after taking ladder
        """
        if position in self.ladder_dict and (position + self.ladder_dict.get(position)) < 100:
            position = position + self.ladder_dict.get(position)
            return position
        else:
            return


if __name__ == "__main__":
    print("welcome to Snake And Ladder Problem")
    WINNER_POS = 100
    player_position = 0
    print("player initial position : {}".format(player_position))
    snake_and_ladder_obj = SnakeAndLadder()

    while player_position < WINNER_POS:
        dice = snake_and_ladder_obj.dice()
        print("dice: {}".format(dice))
        if player_position + dice <= 100:
            player_position = player_position + dice
        print(player_position)
        snake_and_ladder_obj.snake(player_position)
        snake_and_ladder_obj.ladder(player_position)
