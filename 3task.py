strok = list(input())
strok2 = strok[:]
strok.sort()
maxsymb, max2symb  = strok[-1], strok[-2]
print(maxsymb, strok2.index(maxsymb))
print(max2symb)
