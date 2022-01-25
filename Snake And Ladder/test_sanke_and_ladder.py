from snake_and_lader_game import SnakeAndLadder


def test_dice():
    testdice = SnakeAndLadder()
    assert testdice.dice() in [1, 2, 3, 4, 5, 6]

def test_snake_mehod():
    test_snake=SnakeAndLadder()
    assert test_snake.snake(99)==94

def test_lader_method():
    test_ladder=SnakeAndLadder()
    assert test_ladder.ladder(94)==96

