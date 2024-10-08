tally_score = 0
q1=int(input("input '7'\n>"))
q2=int(input("input '6842'\n>"))
q3=int(input("input a WHOLE number LESS than 0\n>"))
q4=int(input("input a WHOLE number GREATER than 0\n>"))
q5=int(input("what is 2+2-2/2?\n>"))

if q1 == 7:
    tally_score = tally_score +1
else:
    tally_score = tally_score +0

if q2 == 6842:
    tally_score = tally_score +1
else:
    tally_score = tally_score +0
if q3 < 0:
    tally_score = tally_score +1
else:
    tally_score = tally_score +0

if q4 > 0:
    tally_score = tally_score +1
else: 
    tally_score = tally_score +0

if q5 == 3:
    tally_score = tally_score +1
else: 
    tally_score = tally_score +0

tally_score = str(tally_score)
print("Your score is " + tally_score + ".")