#** ** *Jeu 5 ** *
import random

gain = 0
compteur = 0
N = 1000000
while compteur < N:
    card_points = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
    card_signs = ['Heart', 'CLUB', 'DIAMOND', 'SPADE']
    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    random_card1 = random_point, random_sign
    point_card1 = int(random_card1[0])

    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    random_card2 = random_point, random_sign
    point_card2 = int(random_card2[0])

    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    random_card3 = random_point, random_sign
    point_card3 = int(random_card3[0])

    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    random_card4 = random_point, random_sign
    point_card4 = int(random_card4[0])

    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    random_card5 = random_point, random_sign
    point_card5 = int(random_card5[0])

    if point_card3 == point_card2 + 1 and point_card2 == point_card1 + 1:
        gain = gain + 1
        print(gain)
        # 1,2,3

    elif point_card3 == point_card2 + 1 and point_card4 == point_card3 + 1:
        gain = gain + 1
        print(gain)
        # 2,3,4

    elif point_card4 == point_card3 + 1 and point_card5 == point_card4 + 1:
        gain = gain + 1
        print(gain)
        # 3,4,5

    elif point_card2 == point_card1 + 1 and point_card3 == point_card2 + 1 \
            and point_card4 == point_card3 + 1:
        gain = gain + 1
        print(gain)
        # 1,2,3,4

    elif point_card3 == point_card2 + 1 and point_card4 == point_card3 + 1 \
            and point_card5 == point_card4 + 1:
        gain = gain + 1
        print(gain)
        # 2,3,4,5

    elif point_card5 == point_card4 + 1 and point_card4 == point_card3 + 1 \
            and point_card3 == point_card2 + 1 and point_card2 == point_card1 + 1:
        gain = gain + 1
        print(gain)
        # 1,2,3,4,5

    compteur = compteur + 1

ProbGain = gain/N
print(ProbGain)