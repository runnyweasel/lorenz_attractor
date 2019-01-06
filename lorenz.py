import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib.pyplot as plt 
import numpy as np  
import matplotlib.patches as mpatches
import pylab
from pylab import figure, axes, pie, title, show
import random
print("====================================================================")
print("=========================LORENZ ATTRACTOR===========================")
print("====================================================================")
h=input('time step ,e.g:0.01 :')
N=input('number of points needed in the plot : ')

print("=========================INITIAL CONDITIONS=========================")
t=input("enter initial time,e.g 0:")
x1=input('input initial x1,e.g 1.6:')
x2=input("enter initial x2,e.g 0:")
x3=input("enter initial x3,e.g 0:")

print("=============================PARAMETERS============================")

a=input('input a,e.g 10:')
b=input('input b,e.g 28:')
c=input('input c,e.g 8/3:')


print("====================================================================")
def fx1(t,x2,x1,x3):
   return  a*(x2-x1)    
def fx2(t,x2,x1,x3):
   return  x1*(b-x3)-x2
def fx3(t,x2,x1,x3):
   return  x1*x2-c*x3


mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')   






x21=[]
x11=[]
x31=[]
x12=[]
x22=[]
T=[]
T1=[]

T.append(t)
x31.append(x3)
x21.append(x2)
l=x1  
m=x2
n=x3
x11.append(x1)      
for i in range(1,N+1,1):
       K1x3=fx3(t,x2,x1,x3)     
       K1x2=fx2(t,x2,x1,x3)
       K1x1=fx1(t,x2,x1,x3)
       K2x3=fx3(t+h/2,x2+K1x2*h/2,x1+K1x1*h/2,x3+K1x3*h/2)
       K2x2=fx2(t+h/2,x2+K1x2*h/2,x1+K1x1*h/2,x3+K1x3*h/2)
       K2x1=fx1(t+h/2,x2+K1x2*h/2,x1+K1x1*h/2,x3+K1x3*h/2)
       K3x3=fx3(t+h/2,x2+K2x2*h/2,x1+K2x1*h/2,x3+K2x3*h/2)
       K3x2=fx2(t+h/2,x2+K2x2*h/2,x1+K2x1*h/2,x3+K2x3*h/2)
       K3x1=fx1(t+h/2,x2+K2x2*h/2,x1+K2x1*h/2,x3+K2x3*h/2)
       K4x3=fx3(t+h,x2+K3x2*h,x1+K3x1*h,x3+K3x3*h)
       K4x2=fx2(t+h,x2+K3x2*h,x1+K3x1*h,x3+K3x3*h)
       K4x1=fx1(t+h,x2+K3x2*h,x1+K3x1*h,x3+K3x3*h)
       x2=x2+(K1x2+2*K2x2+2*K3x2+K4x2)*h/6
       x21.append(x2)
       x1=x1+(K1x1+2*K2x1+2*K3x1+K4x1)*h/6
       x11.append(x1)
       x3=x3+(K1x3+2*K2x3+2*K3x3+K4x3)*h/6
       x31.append(x3)
       t=t+h
       T.append(t) 

        
print("====================================================")
        
 
        
 
ax.plot(x11, x21, x31, label='lorenz attractor:x1='+str(l)+" x2="+str(m)+" x3="+str(n))
ax.legend()
plt.show()

