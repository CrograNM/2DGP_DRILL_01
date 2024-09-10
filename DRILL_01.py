import turtle

#90 -> 0:오른쪽 1:윗쪽, 2:왼쪽, 3:아래쪽
def move(n):
    turtle.stamp()
    turtle.setheading(90 * n)
    turtle.forward(50)
    
    
def restart():
    turtle.reset()

turtle.shape('turtle')

#( 90 * n )-> 0:오른쪽 1:윗쪽, 2:왼쪽, 3:아래쪽
#lambda : 함수를 인자로 전달해야 하는 경우 사용
turtle.onkey(lambda: move(1), 'w')
turtle.onkey(lambda: move(2), 'a')
turtle.onkey(lambda: move(3), 's')
turtle.onkey(lambda: move(0), 'd')
turtle.onkey(restart, 'Escape')

turtle.listen()
turtle.exitonclick()

#2021184033 조성욱