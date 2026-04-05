# Score categories.
# Change the values as you see fit

def choice(counter ,dice ):
    c = 0
    for x,y in counter.items():
        c += x * y
    return c
        

def yatch(counter ,dice ):
    unique = dice[0]
    if counter == {}:
        return 0
    elif counter[unique] == 5:
        return 50
    else: return 0
        
def full_house(counter ,dice):
    if len(dice) == 2:
        a = dice[0]
        b = dice[1]
        if counter[a] in (2,3) and counter[b] in (2,3):
            return a * counter[a] + b * counter[b]
        else: return 0
    else: return 0

def little_straight(counter,dice):
    if len(dice) == 5 and dice[0] ==1:
        cnt = 0
        for x in range(len(dice)):
            if x != 0 and dice[x] -dice[x-1] == 1:
                cnt +=1
            
        if cnt == 4: return 30
        else: return 0

    else: return 0

def big_straight(counter,dice):
    if len(dice) == 5 and dice[0] ==2:
        cnt = 0
        for x in range(len(dice)):
            if x != 0 and dice[x] -dice[x-1] == 1:
                cnt +=1
            
        if cnt == 4: return 30
        else: return 0

    else: return 0
    

def four_of_a_kind(counter ,dice):
    if len(dice) == 2:
        a = dice[0]
        b = dice[1]
        if counter[a] > counter[b] and counter[a] == 4:
            return counter[a] * a
        elif counter[b] > counter[a] and counter[b] == 4:
            return counter[b] * b
        else: return 0
    elif len(dice) == 1 and counter[dice[0]] == 5:
        a = dice[0]
        return (counter[a] -1) * a
    else: return 0
            
        
        
def ones(counter,dice):
    if 1 in counter:
        if counter[1] > 0:
            return counter[1]
        else: return 0
    else:
        return 0
def twos(counter,dice):
    if 2 in counter:
        if counter[2] > 0:
            return counter[2] *2
        else: return 0
    else:
        return 0
def threes(counter,dice):
    if 3 in counter:
        if counter[3] > 0:
            return counter[3] *3
        else: return 0
    else:
        return 0
def fours(counter,dice):
    if 4 in counter:
        if counter[4] > 0:
            return counter[4] *4
        else: return 0
    else:
        return 0

def fives(counter,dice):
    if 5 in counter:
        if counter[5] > 0:
            return counter[5] *5
        else: return 0
    else:
        return 0

def sixes(counter,dice):
    if 6 in counter:
        if counter[6] > 0:
            return counter[6] *6
        else: return 0
    else:
        return 0



YACHT = yatch
ONES = ones
TWOS = twos
THREES = threes
FOURS = fours
FIVES = fives
SIXES = sixes
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = choice


def score(dice, category):

    counter = {}
    dice_unique = list(set(dice))
    dice_unique.sort()
    for i in range(len(dice)):
        if dice[i] in counter:
            counter[dice[i]] += 1
        else:
            counter[dice[i]] = 1

    return category(counter = counter, dice = dice_unique)
