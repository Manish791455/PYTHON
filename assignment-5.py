markSHEET = []
scoreSheet = []
for n in range(int(input())):
    name = input()
    score = float(input())
    markSHEET += [[name,score]]
    scoreSheet += [score]
print(markSHEET)
print(scoreSheet)
x = sorted(set(scoreSheet))[1]
print(x)
for n,s in sorted(markSHEET):
    if s == x:
        print(n)    




