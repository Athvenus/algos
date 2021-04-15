import random
import sys


POP_SIZA = 1000
P0 = []

def random_pack():
    return s_i
  
def initialize():
    return delta_0
  
def select(Pg):
    return sp
  
def adjust(delta_g):
    return delta_g_1
  
def insert(sc):
    return P_g_1
  
def search(s_g,delta_g_1):
    return s_c
  
def merge(Pg,Pg_1):
    return 
  
def main():
    for i in range(POP_SIZE):
        s = random_pack()
        P0.append(s)
       
    g = 0
    delta_0 = initialize()
    gmax = POP_SIZE
    
    while g+1 < gmax:
        for i in range(NEW_POP_SIZE):
            sp = select(Pg)
            delta_g_1 = adjust(delta_g)
            sc = search(s_g,delta_g_1)
            P_g_1 = insert(sc)
            if sc <= sbest:
                sbest = sc
    merge(Pg_1,Pg)
    
    return sbest
