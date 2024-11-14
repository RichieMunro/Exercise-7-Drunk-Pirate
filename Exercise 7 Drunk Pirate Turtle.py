import turtle 
wn = turtle.Screen()
wn.bgcolor ("green")
wn.title("Drunk Pirate")

dp = turtle.Turtle()
dp.color("blue")
dp.pensize(10)

for f in [dp.left(160), dp.forward(100), dp.right(-43), dp.forward(100), 
        dp.left(270), dp.forward(100), dp.right(-97), dp.forward(100), 
        dp.right(-43), dp.forward(100), dp.left(200), dp.forward(100), 
        dp.right(-940), dp.forward(100), dp.left(17), dp.forward(100), 
        dp.right(-86), dp.forward(100)]:
    piratewalk = dp
    print(piratewalk)

wn.mainloop
