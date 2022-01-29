def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for i in range(6):
        for j in range(6):
            if dice1[i] > dice2[j]:
                dice1_wins += 1
            elif dice2[j] > dice1[i]:
                dice2_wins += 1
    return (dice1_wins, dice2_wins)


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    for i in range(len(dices)):
        c = 1
        for j in range(len(dices)):
            if i == j:
                continue
            wins = count_wins(dices[i], dices[j])
            if wins[0] < wins[1]:
                break
            else:
                c += 1
        if c == len(dices):
            return i
    return -1


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    best = find_the_best_dice(dices)
    strategy["choose_first"] = best >= 0
    if strategy["choose_first"]:
        strategy["first_dice"] = best
    else:
        difference = []
        for i in range(len(dices)):
            difference.append(-1)
        for i in range(len(dices)):
            for j in range(i+1, len(dices)):
                if i == j:
                    continue
                wins = count_wins(dices[i], dices[j])
                if wins[0] >= wins[1]:
                    diff = wins[0]-wins[1]
                    if diff > difference[j]:
                        difference[j] = diff
                        strategy[j] = i
                else:
                    diff = wins[1]-wins[0]
                    if diff > difference[i]:
                        difference[i] = diff
                        strategy[i] = j
    return strategy


s = compute_strategy(
    [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]])
print(s)
s = compute_strategy(
    [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]])
print(s)
s = compute_strategy(
    [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])
print(s)
