#Maria Girgis, Connor Aalto PA 5
#GUI startup

from graphics import*

def main():
    win=GraphWin("Black Jack Intro",900,500)
    casinoBack=Image(Point(450,250), "images/CASINO.gif")
    casinoBack.draw(win)
    intro=Text(Point(625,200),"Welcome to the Casino! \n Are you ready to win big?")
    intro.setSize(36)
    intro.setFace("times roman")
    intro.setStyle("bold")
    intro.setTextColor(color_rgb(255,204,51))
    intro.draw(win)
    s1=Image(Point(0,158),"images/s1 copy.gif")
    s1.draw(win)
    time.sleep(1)
    s1.undraw()
    b1fv=Image(Point(141,248),"images/b1fv copy.gif")
    b1fv.draw(win)
    time.sleep(1)
    b1fv.undraw()
    S1=Image(Point(297,311),"images/s1 copy.gif")
    S1.draw(win)
    time.sleep(1)
    S1.undraw()
    coin=Image(Point(624,338),"images/CHIP.gif")
    coin.draw(win)
    pt1=Point(450,300)
    pt2=Point(550,375)
    
    yes=drawButton(win,pt1,pt2,"Yes")
    #yes.draw(win)
    pt3=Point(700,300)
    pt4=Point(800,375)
    no=drawButton(win,pt3,pt4,"No..")
    #no.draw(win)
    point1=win.getMouse()
    if isClicked(no,point1):
        win.close()
    
        


def drawButton(win, pt1, pt2, label):
    button = Rectangle(pt1, pt2)
    button.setFill(color_rgb(255,204,51))
    button.draw(win)
    centerX = (pt1.getX() + pt2.getX()) / 2.0
    centerY = (pt1.getY() + pt2.getY()) / 2.0
    center=Point(centerX,centerY)
    myLabel=Text(center,label)
    myLabel=myLabel.draw(win)

    return button

def isClicked(button,point):
    x=point.getX()
    y=point.getY()
    pt1=button.getP1()
    pt2=button.getP2()
    if(pt1.getX() < x < pt2.getX() and pt1.getY() < y < pt2.getY()):
        return True
        print("clicked")
    else:
        return False
main()
