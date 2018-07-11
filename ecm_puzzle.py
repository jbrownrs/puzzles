"""
Script for making iterative guesses to the following
ECM-Selection problem:
It's time for the ACME Ltd 'Spring into Summer' staff event.
Amongst the refreshments, there's a 10 litre punchbowl filled
to the brim with ACME's legendary punch. Now, a jug
(capacity J litres) is filled from the bowl, and the punchbowl
topped up with water. Assume there's no spillage, and the
punchbowl's contents mix completely.

Then the process is repeated once more - the jug is filled with
liquid from the punchbowl, and the bowl topped up with water.

Unfortunately for latecomers to the event, the proportion of
punch to water in the punchbowl is now 1:1.

What is the capacity of the jug?
"""
import random
from math import log10, floor, sqrt

punchbowl = float(input("How big is your punchbowl?"))
# initialise with a random jug capacity guess
jug = random.uniform(0.01, punchbowl-0.01)
print(jug)

#howManyRepetitions = int((input("How many times do you wish to use the jug?"))

def round_sig(x, sig=5):
   return round(x, sig-int(floor(log10(abs(x))))-1)

def dip_the_bowl(punchbowl, jug):
    #for _ in xrange(howManyRepetitions):
    punch_amount_reduced = punchbowl - jug
    #how much punch is there if we then add in the jug of water
    punch_proportion = punch_amount_reduced/punchbowl
    # the actual punch amount will be the same as before addition of water
    # only the proportion will change
    # second removal of punch
    punch_amount_reduced_2 = (punch_amount_reduced)*punch_proportion
    #punch_amount_two = ((punchbowl - jug)/punchbowl)*(punchbowl - jug)
    # add water for second time what's the proportion of punch
    punch_proportion_two = punch_amount_reduced_2/punchbowl
    print('Proportion of the punchbowl that is punch is', punch_proportion_two,
          'given a jug of capacity', jug)    
    if round_sig(punch_proportion_two) == 0.50:
        print('For a 50:50 mix (aka', punch_proportion_two,
        '% punch) the jug capacity is', jug)   
        return
    #elif punch_proportion_two > 0.5:
        #jug = (punchbowl - jug)/2
        # if too much punch need a bigger jug
        # jug = jug + (0.3*jug)
     #   jug = jug + (jug*(punch_proportion_two - 0.5))
     #   dip_the_bowl(punchbowl,jug)
    else:
        #jug = jug/2
        # if not enough punch need a smaller jug
        #jug = jug - (0.3*jug)
        jug = jug + (jug*(punch_proportion_two - 0.5))
        dip_the_bowl(punchbowl,jug)
            
