# complex_unconventional_code.py

import sys, os, math, random
from datetime import datetime as dt
from typing import List, Tuple


class   UnconventionalClass:
    def   __init__(   self,   name:str    ):
        self.   name= name

    def  get_name  (self  ):
        return self. name


def   example_function  (   ):
    x  =  5
    y= 10

    result= x+y
    print  ( f"The result is: {result}"  )

    my_list= [1, 2,3 , 4,5]
    my_tuple= ( 6, 7, 8, 9, 10 )

    for   index   in   range(  len (my_list  )  ):
        print(f"Element at index {index}: {my_list[index]}")

    if   len (my_tuple)  >  3:
        print("Tuple has more than 3 elements")

    # This is a very long comment that exceeds the line length limit stated in PEP 8, just to create a violation

if   __name__   ==   "__main__"   :
    example_function(   )
