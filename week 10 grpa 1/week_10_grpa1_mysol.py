def boyermoore(t,p):
    last = {} # Preprocess
    for i in range(len(p)):
        last[p[i]] = i
    poslist=[]
    i = 0
    while i <= (len(t)-len(p)):
        matched,j = True,len(p)-1
        while j >= 0 and matched:
            if t[i+j] != p[j]:
                matched = False
            j = j - 1
        if matched:
            poslist.append(i)
            i = i + 1
        else:
            j = j + 1
            if t[i+j] in last.keys():
                i = i + max(j-last[t[i+j]],1)
            else:
                i = i + j + 1
    return(poslist)

text="abcdabababcdabab"
pattern="abdd"
x=boyermoore(text,pattern)

max_count=0
count=0
for i in range(len(x)-1):
  if x[i+1]-x[i]==len(pattern):
    count+=1
  else:
    count=1
  if count>max_count:
    max_count=count
print(max_count)
