"""
turnin.py - Use this file to enter your answers, and turn in a printout of this file.

UVA CS 1120
Spring 2016

Project 1 -- Making Mosaics

My name:    David Evans
My UVA ID:  dee2b
"""

# The next line includes the provided code for use in your answers: (don't delete it)
from mosaic import *  

def get_brightness(color):
   return get_red(color) + get_blue(color) \
                 + get_green(color)
   
def is_brighter(color1, color2):
   return get_brightness(color1) > get_brightness(color2)

def test_brighter():
    assert is_brighter(WHITE, RED)
    assert not is_brighter(RED, WHITE)
    # ...
    print("Passed all tests!")


def color_difference(colora, colorb):
   def component_difference(component):
      return abs(component(colora) - component(colorb))
      
   return (component_difference(get_red) +
           component_difference(get_blue) +
           component_difference(get_green))

def closer_color(sample, color1, color2):
    """
    Put your code here that implements the closer_color function
    Your function should return True if color1 is closer to sample,
    and otherwise return False.
    """
    return color_difference(color1, sample) < color_difference(color2, sample)
    
def test_closer():
    assert closer_color(RED, PURPLE, WHITE)
    assert not closer_color(WHITE, BLACK, YELLOW)
    assert closer_color(GREEN, make_color(20, 255, 20), make_color(20, 255, 30))
    print ("All tests passed!") 

# Uncomment the next line once you've attempted Question 5 to
# make a photomosaic.  To make something better, replace the provided
# rotunda.gif with a more interesting picture!  (Must be in .gif format.)

# make_photomosaic("rotunda.gif", "tiles/", closer_color)
