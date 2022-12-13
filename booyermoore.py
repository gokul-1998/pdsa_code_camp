def boyermoore(t,p):
    last = {} # Preprocess -> 
    for i in range(len(p)):
        last[p[i]] = i
    # create a dictionary with characters as keys and last seen index in pattern as values
    poslist=[]
    i = 0
    while i <= (len(t)-len(p)): #while i <= len(text) minus len(pattern):
        matched,j = True,len(p)-1   #set matched,j=True and len(pattern)-1 , means you are coming from last index of pattern.
        while j >= 0 and matched:   # while j(position in pattern) is >=0 (means we are moving the pointer in pattern) and matched remains unchanged
            if t[i+j] != p[j]:    # if t[i+j] (index in text) != p[j](index in pattern) (eg.if last index of pattern doesnt match i+j th index of text)
                matched = False   #set matched =False, hence it will go put of while loop
            j = j - 1   # if they are matched now we will check the previous character by reducing j=j-1
        if matched: # this line comes when the whole of pattern is matched in the text
            poslist.append(i) # we append the index i to poslist
            i = i + 1 # since its matched we move one step and continue
        else:  # if its not matched
            j = j + 1  # we increase the pointer j to j+1
            if t[i+j] in last.keys(): # and check if the (i+j)th character is present in patten dictionary,i.e. 
                i = i + max(j-last[t[i+j]],1)  # if it is found,move the pointer i to i+max(j-last[t[i+j]],1)
            else: # if the next character is not in the pattern dictionary, we can skip completely by adding i=i+j+1
                i = i + j + 1
    return(poslist)
print(boyermoore('abcaaacabc','abc'))

"""
Steps to follow
    1) create the last dictionary to preprocess the pattern,where keys are unique characters and values are last time the key is seen in the pattern
    2)create a list postlist=[] and set i=0
    3)while i<= len(t)-len(p) and set matched=True and j=last index of pattern-> [we process the text until  we reach len(text)-len(pattern) ]
        - while j>0 and matched [checking till what postion we are matching]
            - if t[i+j]!=p[j]: set matched=False
            j=j-1
        if matched: ->[if the text matches  the pattern] append i to poslist and increment i=i+1
        else:increment j=j+1
            if [check if the (i+j)th character is present in pattern dictionary ],we can skip completely by adding i=i+j+1, 
            else
"""