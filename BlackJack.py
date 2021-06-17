''' Blackjack - Created by Aman Nayyar'''

def blackjack():
    import random
    cardtype = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    cards = []
    for ct in cardtype:
        cards.extend([ct for x in range(0,4)])

    def draw_card():
        card = random.choice(cards)
        cards.remove(card)
        return card

    def cardsum(cardlist):
        count = cardlist.count('A')
        cardlist = [x for x in cardlist if x != 'A']
        cardlist.extend(['A' for x in range(count)])
        sumofcards = 0
        for c in cardlist:
            if c.isdigit():
                sumofcards+=int(c)
            elif c in ['K','Q','J']:
                sumofcards+=10
            else:
                sumofcards+=11
                if sumofcards > 21:
                    sumofcards-=11
                    sumofcards+=1
        return sumofcards
                
    print('Your Cards: ')
    card1 = draw_card()
    card2 = draw_card()
    print(card1,' and ',card2)
    your_cards = [card1,card2]


    card1 = draw_card()
    card2 = draw_card()
    opp_cards = [card1,card2]
    print('Opponent open card: ',card2)



    while cardsum(your_cards) <= 21:
        stand_hit = int(input('\nFor stand, press 0 and for Hit, press 1: '))
        if stand_hit == 1:
            drawn_card = draw_card()
            your_cards.append(drawn_card)
            print("Drawn Card: ",drawn_card)
        else:
            break

    your_sum = cardsum(your_cards)
    print('Your Total: ',your_sum)
    print('\nOpponent\'s Turn\n')

    while cardsum(opp_cards) <= 21:
        if cardsum(opp_cards) <= 12:
            drawn_card = draw_card()
            opp_cards.append(drawn_card)
            print('Opponent Hits and Draws ',drawn_card)
        elif cardsum(opp_cards) > 12 and cardsum(opp_cards) < 15:
            opp_choice = random.choice([0,1])
            if opp_choice == 0:
                break
            else:
                drawn_card = draw_card()
                opp_cards.append(drawn_card)
                print('Opponent Hits and Draws ',drawn_card)
        else:
            break

    opp_sum = cardsum(opp_cards)
    print('Opponent Total: ',opp_sum)


    if your_sum > 21 and opp_sum <= 21:
        print('\nYou are Busted, Opponent Wins')
    elif opp_sum > 21 and your_sum <= 21:
        print('\nOpponent is Busted, You Win')
    elif opp_sum > your_sum:
         print('\nOpponent has higher value, Opponent Wins')
    elif opp_sum < your_sum:
         print('\nYou have higher value, You Win')
    else:
         print('\nSame Value, Tied')


blackjack()
