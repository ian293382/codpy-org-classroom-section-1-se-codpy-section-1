from judge_code import game_over

def test_game_over_0():
    assert game_over(0) == True

def test_game_over_666():
    assert game_over(666) == True

def test_game_over_other():
    # i.e health = 3 give other number
    assert game_over(3) == False
