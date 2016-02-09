
import stepAnimation
from math import *

def alternatingGridAnimation(canvas,width,height,step):
    x1=50    # left of the whole graph
    y1=50    #top of the whole graph
    x2=width-50  # right of the whole graph
    y2=height-50  # bottom of the whole graph
    canvas.create_rectangle(x1,y1,x2,y2)    # the outline of the whole graph
    w1=100    # width of each rectangle of 10 by 5
    h1=50     # height of each rectangle of 10 by 5
    w2=50     # width of each rectangle of 5 by 10
    h2=100    # height of each rectangle of 5 by 10
    if step%100<50:     # 10 by 5
        for Y in xrange(0,10):
            for X in xrange(0,5):
                canvas.create_rectangle(x1+w1*X,y1+h1*Y,x1+w1*(X+1),
                    y1+h1*(Y+1), fill= "lightblue" if( X%2==Y%2)else "pink")
        canvas.create_rectangle(x1+w1*((step%w1)%5),y1+h1*((step%w1)/5),
            x1+w1*((step%w1)%5+1),y1+h1*((step%w1)/5+1),
            fill="blue" if step%2==0 else "red")
    else:               # 5 by 10
        for Y in xrange(0,5):
            for X in xrange(0,10):
                canvas.create_rectangle(x1+w2*X,y1+h2*Y,x1+w2*(X+1),
                    y1+h2*(Y+1), fill= "lightblue" if( X%2==Y%2)else "pink")
        if (step%50)%20<10:
            canvas.create_rectangle(x1+w2*(step%10),y1+h2*((step%w2)/10),
                x1+w2*(step%10+1),y1+h2*((step%w2)/10+1),
                fill="blue" if step%2==0 else "red")
        else:
            canvas.create_rectangle(x1+w2*(step%10),y1+h2*((step%w2)/10),
                x1+w2*(step%10+1),y1+h2*((step%w2)/10+1),
                fill="red" if step%2==0 else "blue")
      
    canvas.create_text(width/2,height/2,
        text="10 by 5" if (step%100<50) else "5 by 10",
        font="Helvetica 85 bold",fill="brown")
    
stepAnimation.run(alternatingGridAnimation,width=600,height=600)
