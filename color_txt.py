from graphics import *

def main():
    win = GraphWin('Draw a Triangle', 350, 350)
    win.yUp() 
    win.setBackground('yellow')
    message = Text(Point(win.getWidth()/2, 30), 'Click on three points')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    vertices = [p1, p2, p3]

    triangle = Polygon(vertices)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4) 
    triangle.draw(win)

    message.setText('Click anywhere to quit') 
    win.getMouse()
    win.close() 

main()
