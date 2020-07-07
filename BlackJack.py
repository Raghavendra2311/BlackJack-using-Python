import random
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}#

class deck:
    '''
    This is a class of deck of cards
    '''
    
    def __init__(self):
        self.deck1 = []
        for i in suits:
            for j in ranks:
                self.deck1.append(j+ " of " + i)
    
    def __str__(self):
        pass
    
    def deal(self):
        print(self.deck1)
    
    def shuffle(self):
        a = random.sample(self.deck1,len(self.deck1))
        return a 
        

def deal_cards():
    deck2=deck()
    global shuffled_deck2
    shuffled_deck2 = deck2.shuffle()
    def cards_show():
        dealer_card1 = shuffled_deck2[0]
        dealer_card2 = shuffled_deck2[1]
        print("Dealer Card 1 is: " + dealer_card2)
        player_card1 = shuffled_deck2[2]
        player_card2 = shuffled_deck2[3]
        print("Player Card 1 is: " +player_card1)
        print("Player Card 2 is: " +player_card2)
    cards_show()

def bet():
    '''
    This function asks the user for the bet that they would like to place
    '''
    
    x = True
    
    while x:
        global bet1
        bet1 = int(input("Enter your bet: ")) 
        ''' bet1 is the bet entered by the user'''
        balance = bal
        if bet1 <= balance:
            balance = balance - bet1
            print("{} is the balance Chips!" .format(balance))
            print("Lets Play!")
            x = False
            return bet1
        else:
            print("Unavailable funds!")


def play_choice():
    final_value = values[shuffled_deck2[2].split()[0]] + values[shuffled_deck2[3].split()[0]]
    comp_value = values[shuffled_deck2[0].split()[0]] + values[shuffled_deck2[1].split()[0]]
    n=4
    for i in range(4,51):
        if final_value < 21:
            choice = input("Do you wish to Hit or stand: ")
            if choice.upper() == "HIT":
                print(shuffled_deck2[n])
                final_value = final_value + values[shuffled_deck2[n].split()[0]]
                n +=1
            elif choice.upper() == "STAND":
                if comp_value > final_value :
                    print("You lose because the dealer has better cards")
                    status = 0
                    print("Dealer Cards are: " + shuffled_deck2[0] +" & "+ shuffled_deck2[1])
                elif comp_value > 21 or comp_value < final_value:
                    print("Congratulations, YOU WIN!")
                    status = 1
                else:
                    for i in range(4,51):
                        if comp_value < 17 :
                            comp_value = comp_value + values[shuffled_deck2[n].split()[0]]
                            n +=1
                        else :
                            if comp_value>final_value:
                                print("You Lose")
                                status = 0
                            else:
                                print("Congratulations, YOU WIN!")
                                status = 1
                            break
                break
        else:
            print("You lose")
            status=0
            break
    global bal
    if status ==1:
        bal = bal + (2*bet1)
    else:
        bal = bal - bet1
    print("New Balance is {}" .format(bal))



def play_again():
    playAgain = input("Do you want to play again?")
    if playAgain.upper() == "YES":
        final_func()
    elif playAgain.upper() == "NO":
        print("Thank you for playing")
 


global bal
bal = int(input("How much chips would you like to purchase?"))
def final_func():
    '''
    This function is the final function. The chronology is:
    1) It first asks the user for a bet. If bet is greater than the available balance, it proceeds.
    2) Then the program shows one card of the dealer and 2 cards of player.
    3) The player has to make a choice between 'Hit' and 'Stand'.
    4) If the user chooses Hit then one more card is drawn from the deck. If the new sum is greater than 21, the user loses. 
    Whilst if the total is less then 21, the program goes to 'STEP NO.  3'
    5) If the user chooses to Stand, the dealer i.e the Computer, keeps drawing cards until its total is greater than the player's
    total, or 21
    6) In case the dealer total goes greater than 21, the player Wins
    7) In case the dealer total is greater than player total, the player loses
    '''
    print("WELCOME TO BLACK-JACK")
    bet()
    deal_cards()
    play_choice()
    play_again()
    
final_func()                     