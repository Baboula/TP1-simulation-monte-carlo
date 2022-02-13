#** ** *Jeu 2 ** *
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

    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    random_card2 = random_point, random_sign

    if random_card1 == random_card2:
        # print('vous avez gagnez!')
        gain = gain + 1
        print(gain)
    # else:
    # print('vous avez perdu !')

    compteur = compteur + 1

ProbGain = gain/N
print(ProbGain)
