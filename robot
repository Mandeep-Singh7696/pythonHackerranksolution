moves=input()
L=R=U=D=0
for mov in moves:
  if mov=='L':
    L+=1
  elif mov=='R':
    R+=1
  elif mov=='U':
    U+=1
  elif mov=='D':
    D+=1
if L==R and U==D:
  print('true')
 else:
  print('false')
  
