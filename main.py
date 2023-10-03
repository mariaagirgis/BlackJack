#Maria Girgis
#PA 5 defining class
#11/12/22

from random import randint
from graphics import *
from buttonforblackjack import *
import time
from introScreen import*


def Graphics():
    win1=GraphWin("Game Window",900,500)
    background=Image(Point(450,250),"images/GAMEBACK.gif")
    background.draw(win1)

    return win1
    


class Card:
   
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def getValue(self):
        if self.rank == 0:
            return 1
        elif self.rank > 9:
            return 10
        
        else:
            return int(self.rank)
            
    
    def __str__(self):
        rank=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        suit={"d":"diamonds","c":"Clubs", "h":"Hearts","s":"Spades"}
        suitName=suit.get(self.suit)
        string= rank[self.getRank()]+" "+"of"+" "+suitName
        return string
    
       
class Deck:
    
    def __init__(self):
        self.deck=[]
        suit=["d","c", "h","s"]
        for i in range(13):
            for j in range(4):
                newCard=Card(i,suit[j])
                self.deck.append(newCard)
    def shuffle(self):
        for i in range(len(self.deck)-1,0,-1):
            r=randint(0,i)
            self.deck[i], self.deck[r]= self.deck[r], self.deck[i]
        #print(self.deck)
    def strDeck(self):
        for i in range(52):
            print(self.deck[i])
    def dealCard(self):
        dealCard=self.deck[0]
        self.deck.pop()
        self.shuffle()
        return dealCard
    def cardsLeft(self):
        print(len(self.deck))
        
class BlackJack:
    
    def __init__(self,dHand=[],pHand=[]):
        self.dHand=dHand
        self.pHand=pHand
        self.cards=Deck()
        self.cards.shuffle()
        self.handValue = 0
        
        #shuffle the declk
        #create dealer and player hand (2 random cards from the deck one for dealer one for player)
    def initDeal(self,gwin,xposD,yposD,xposP,yposP):

        
        
        self.pHand.append(self.cards.dealCard())
        self.pHand.append(self.cards.dealCard())
        
        self.dHand.append(self.cards.dealCard())
        self.dHand.append(self.cards.dealCard())
        #print player card
        for card in self.pHand:
            suit=card.getSuit()
            rank= card.getRank()
            img=Image(Point(xposP,yposP),"images/" + card.suit + str(card.rank)+".gif")
            img.draw(gwin)
            yposP=yposP+50

        #print dealer card
        for card in self.dHand:
            suit=card.getSuit()
            rank= card.getRank()
            img=Image(Point(xposD,yposD),"images/" + card.suit + str(card.rank)+".gif")
            img.draw(gwin)
            yposD=yposD+50


        return self.pHand

    def hit(self,gwin,xPos,yPos):
        nextCard=self.cards.dealCard()
        self.pHand.append(nextCard)
        suit=nextCard.getSuit()
        rank=nextCard.getRank()
        img=Image(Point(xPos,yPos),"images/" + suit + str(rank)+ ".gif")
        img.draw(gwin)
        

        #adds card to player hand
    def evaluateHand(self,hand):
        handValue = 0
        
        for card in hand:
            if card.getValue() == 1 and handValue + 11 <= 21:
                handValue = handValue + 11

            elif card.getValue() == 1 and handValue + 11 > 21:
                handValue = handValue + 1

            else:
                handValue = handValue + card.getValue()

        



        
        return handValue
    
    def dealerPlays(self, gwin, xPos, yPos):
            
        newCard = self.cards.dealCard()
        self.dHand.append(newCard)

        for self in self.dHand:
            suit = newCard.getSuit()
            rank = newCard.getRank()
            imgObj = Image(Point(xPos, yPos), "images/" + suit + str(rank) + ".gif")
            imgObj.draw(gwin)
        #tally up dealer and players hand and see who won 
        


def main():
        
    win1=Graphics()
    deck = Deck()

    game = BlackJack()
    game.initDeal(win1,100,100,400,100)
    
    playerCount = Text(Point(400, 30), str(game.evaluateHand(game.pHand)))
    playerCount.setSize(25)
    
    initDeal = game.dHand[0].getValue()
    
    
    
    dealerCount = Text(Point(100, 30), initDeal)
    blankCard = Image(Point(100, 150), 'images/b1fv.gif')
    blankCard.draw(win1)

    
    dealerCount.setSize(25)
    
    playerCount.draw(win1)
    dealerCount.draw(win1)


    hitButton = Button(win1, Point(250, 50), 100, 50, "hit")

    stayButton = Button(win1, Point(250, 150), 100, 50, "stay")

    quitButton = Button(win1, Point(600, 20), 100, 50, "quit")

  
    hitButton.activate()
    stayButton.activate()

    
    if game.evaluateHand(game.pHand) == 21:
        print("Player hits blackjack, player wins")
        
      #deactivate hit and stay buttons       
        hitButton.deactivate()
        stayButton.deactivate()
    


    hitCounter = 1
    dealCounter = 1

    pt = win1.getMouse()


    while not quitButton.clicked(pt):

        
        #when hit button is clicked
        

        if hitButton.clicked(pt):


            BlackJack.hit(game, win1, 400, 150 + (hitCounter*50))

            playerCount.undraw()
            playerCount = Text(Point(400, 30), str(game.evaluateHand(game.pHand)))
            playerCount.setSize(25)

            playerCount.draw(win1)

            quitButton.activate()

            hitCounter = hitCounter + 1

            if game.evaluateHand(game.pHand) > 21:
                print("You busted, player loses")
                break

            elif game.evaluateHand(game.pHand) == 21:
                print("Player hits blackjack, player wins")
                break

            pt = win1.getMouse()


        if stayButton.clicked(pt):

            blankCard.undraw()

            hitButton.deactivate()

            dealerCount.undraw()

            dealerCount = Text(Point(100, 30), str(game.evaluateHand(game.dHand)))
            dealerCount.setSize(25)
            dealerCount.draw(win1)

        

            if game.evaluateHand(game.dHand) == 21:
                print("Dealer hits Blackjack, you lose")
                break




            while game.evaluateHand(game.dHand) in range(0, 17):

                time.sleep(1)
                
                BlackJack.dealerPlays(game, win1, 100, 150 + (dealCounter*50))

                dealerCount.undraw()

                dealerCount = Text(Point(100, 30), str(game.evaluateHand(game.dHand)))
                dealerCount.setSize(25)
                dealerCount.draw(win1)
                dealCounter = dealCounter + 1

                if game.evaluateHand(game.dHand) >= 21:
                    print('Dealer Bust')
                    break

            if game.evaluateHand(game.dHand) > 16:
                print("Hard stop for dealer")
                break

                

    #eval final card numbers for player and dealer

    #deactivate hit and stay buttons       
    hitButton.deactivate()
    stayButton.deactivate()


    if game.evaluateHand(game.pHand) < 21:
        if game.evaluateHand(game.dHand) < 21:
            
            if game.evaluateHand(game.pHand) > game.evaluateHand(game.dHand):
                print("You win!")

            elif game.evaluateHand(game.dHand) > game.evaluateHand(game.pHand):
                print("Dealer wins!")

            else:
                print("Push!")

                



            

main()




                
            
    

