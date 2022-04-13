#turtle 그래픽을 이용하여 그림을 그리는 프로그램 모듈 만들기
import turtle as t
def draw_circle(n): #왼쪽으로 원을 그리는 프로그램
    m = 360/n
    for i in range(n):
        t.circle(100)
        t.left(m)
def draw_square(size): #사각형을 안에서 바깥으로 확장하면서 그리는 프로그램
    for i in range(4):
        t.fd(size)
        t.left(90)
        size+=5
def draw_line(): #거미줄 같은 모양을 그리는 프로그램
    t.forward(100)
    t.backward(100)
#turtleM이라는 폴더(디렉토리)를 만들고 위 모듈을 해당 디렉토리로 넣자.
#turtleM이라는 패키지가 생성되었으니, 모듈을 호출하여 turtle 프로그램을 실행시켜보자.
from turtleM.prgtt import *
draw_circle(10)
draw_square(20)
draw_line()
t.done()
