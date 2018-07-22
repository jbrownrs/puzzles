"""
Functions for making iterative guesses to the following
ECM-Selection problem:
"It's time for the ACME Ltd 'Spring into Summer' staff event.
Amongst the refreshments, there's a 10 litre punchbowl filled
to the brim with ACME's legendary punch. Now, a jug
(capacity J litres) is filled from the bowl, and the punchbowl
topped up with water. Assume there's no spillage, and the
punchbowl's contents mix completely.

Then the process is repeated once more - the jug is filled with
liquid from the punchbowl, and the bowl topped up with water.

Unfortunately for latecomers to the event, the proportion of
punch to water in the punchbowl is now 1:1.

What is the capacity of the jug?"
For the script to solve this run (in command line)
python3 ecm_puzzle.py
"""
import random
from math import log10, floor, sqrt

def round_sig(x, sig):
   return round(x, sig-int(floor(log10(abs(x))))-1)

def dip_the_bowl(punchbowl,jug):
    # for _ in xrange(howManyRepetitions):
    # currently defaults to two dips to remove punch and add water
    punch_amount_reduced = punchbowl - jug
    # how much punch is there if we then add in the jug of water
    punch_proportion = punch_amount_reduced/punchbowl
    # the actual punch amount will be the same as before addition of water
    # only the proportion will change
    # second removal of punch
    punch_amount_reduced_2 = (punch_amount_reduced)*punch_proportion
    # add water for second time what's the proportion of punch
    punch_proportion_two = punch_amount_reduced_2/punchbowl
    # print('Proportion of the punchbowl that is punch is', punch_proportion_two,
    # 'given a jug of capacity', jug)    
    if round_sig(punch_proportion_two,5) != 0.50:
       # if not enough punch we need a smaller jug
        # if too much punch we need a bigger jug
        jug = jug + (jug*(punch_proportion_two - 0.5))
        return dip_the_bowl(punchbowl,jug)
    else:
        answer = round_sig(jug,3)
        print('For a 1:1 mix (aka',round_sig(punch_proportion_two,2)*100,
        '% punch) in your',punchbowl,'litre punchbowl the jug capacity required is', round_sig(jug,3),'litres (to 3 s.f.)')   
        return answer

def size_input():
      while True:
         size = input("How big is your punchbowl (in litres)?\n")
         try:
            value = float(size)
            if value > 0:
               break
            else:
               print("Invalid input! Please enter a number greater than zero.")
         except ValueError:
            message = "Invalid input! Please enter a number greater than zero."
            print(message)
      return value

