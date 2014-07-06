import random

hits = 0
fails = 0


print "HACKER ROLLER v0.1"
pool = int(raw_input('DICE POOL: '))
print "ROLLING..."
for die in range(0, pool):
    die = random.randint(1, 6)
    print die
    if die in range(5, 7):
        hits = hits+1
    elif die == 1:
        fails = fails+1

print "HITS: "+str(hits)

if fails >= pool/2:
    if hits == 0:
        print "CRITICAL GLITCH!"
        print "ERROR ERROR CRIT GLITCH EQUALS VERY YES"
        hits = 1/hits
    else:
        print "GLITCH!"
        print "ALL YOUR GLITCH IS BELONG TO YOU"

