n=int(input())

x0,y0=map(int,input().split())
xn2,yn2=map(int,input().split())

c_x=(x0+xn2)/2
c_y=(y0+yn2)/2

x0-=c_x
y0-=c_y

from math import sin,cos,pi
x1=cos(2*pi/n)*x0-sin(2*pi/n)*y0+c_x
y1=sin(2*pi/n)*x0+cos(2*pi/n)*y0+c_y

print(x1,y1)