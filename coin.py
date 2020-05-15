##Tossing a coin 20 time

import random
r = {'h': 0,'t': 0}
s = list(r.keys())
h=[]
t=[]
for i in range(20):
    if random.choice(s) =='h':
        h.append(1)
    else:
        t.append(0)

print("Heads=",len(h))
print("Tails=",len(t))
