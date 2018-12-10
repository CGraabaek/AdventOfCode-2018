import re
print("Advent Of Code - Day 4")

PUZZLEINPUT = open('input.txt', 'r').readlines()

regex_pattern = r"\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] (.+)"
regex_guard = r"#([0-9]+)"
#regex_pattern = r"([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

input = []
print(PUZZLEINPUT[0])

for line in PUZZLEINPUT:
    match = re.match(regex_pattern,line)
    input.append([str(x) for x in match.groups()])

guards = []
current_guard = None
i = 0

for year, month, day, hour, minute, message in input:
    if "Guard" in message:
        regex_guard = r"Guard #([0-9]+) begins shift"
        match = re.match(regex_guard,message)
        guard_id = match.group(1)
        if int(guard_id) not in guards:    
            guards.append(int(guard_id))
        
    
print(sorted(guards))
