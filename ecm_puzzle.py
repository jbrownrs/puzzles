"""
Script for making iterative guesses to the following
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
"""
import random
from math import log10, floor, sqrt
import ecm_puzzle_module

punchbowl = ecm_puzzle_module.size_input()
# initialise with a random jug capacity guess
jug = random.uniform(0.01, punchbowl-0.01)
print("Initialising with a random jug capacity guess of:",ecm_puzzle_module.round_sig(jug,3),'litres')
#could extend with changes to the number of jug dipping iterations
#howManyRepetitions = int((input("How many times do you wish to use the jug?"))
ecm_puzzle_module.dip_the_bowl(punchbowl, jug)

