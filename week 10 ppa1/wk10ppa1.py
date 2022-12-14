def BMCount(t,p):
  last = {} # Preprocess
  for i in range(len(p)): 
    last[p[i]] = i   # dist for preprocessing
  poslist,i, count = [], 0, 0 # Loop  #poslist -> list of indices at which we have pattern match
  
  while i <= (len(t)-len(p)): #while the pointer is less than the len(text)- len(pattern)
    matched,j = True,len(p)-1 # setting matched to True,j is a pointer
    poslist.append(i) # adding 0 to the poslist
    while j >= 0 and matched:  # 
      count += 1  # increating the count everytime the last character matches the pattern last character.
      if t[i+j] != p[j]:
        matched = False
      j = j - 1
    if matched:
      i = i + 1
    else:
      j = j + 1
      if t[i+j] in last.keys():
        i = i + max(j-last[t[i+j]],1)
      else:
        i = i + j + 1
  return poslist, count
t = "straw plus berry is strawberry"
p="strawberry" 
list, c = BMCount(t, p)
print(*list)
print(c)