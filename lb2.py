marksSheet =  [['harry', 37.21], ['berry', 37.21], ['tina', 37.2], ['akriti', 41.0], ['harsh', 39.0]]
scoreSheet = [37.21, 37.21, 37.2, 41.0, 39.0]
s = sorted(marksSheet)


x = sorted(set(scoreSheet))[1]


for n,s in sorted(marksSheet):
    if s == x:
        print(n)    
# here i seperate sorted but iam not understanding