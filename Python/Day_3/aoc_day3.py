import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import vizualisation

import re
print("Advent Of Code - Day 3")

PUZZLEINPUT = open('input.txt', 'r').readlines()

#Hold all claims
claims = []
# Match with raw strings
regex_pattern = r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

for line in PUZZLEINPUT:
    match = re.match(regex_pattern,line)
    claims.append([int(x) for x in match.groups()])

# See all the squares vizualized
# vizualisation.plot_claims(claims)