__author__ = 'BrianAguirre'

import math
import timeit

#Using the estimation from the proof found on: http://www.souravsengupta.com/cds2016/lectures/Fibonacci_Anstee.pdf

def fibonnacci_n(n):

    answer = 0
    sqrtFive = math.pow(5, 1/2)

    answer = (sqrtFive/5)*((1+sqrtFive)/2)**(n)
    
    return round(answer)


print(fibonnacci_n(20000000))

