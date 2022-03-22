import numpy as np

arr = np.array(([18,2,3,4],[1,4,7,6],[7,60,8,18],[1,1,1,1],[77,11,50,0]))
arr

dom_val = []

row = 5
column = 4

def neigbours(arr,r,c):
    if r+c==0:
        a = [arr[0][1],arr[1][:2]]
        return a
    elif r==0 and c!=column-1:
        a = [arr[0][[c-1,c+1]],arr[1][[c,c+1,c-1]]]
        return a
    elif r==0 and c==column-1:
        a = [arr[0][c-1],arr[1][[c-1,c]]]
        return a
    elif r==row-1 and c==0:
        a = [arr[r][1],arr[r-1][[c+1,c]]]
        return a
    elif r==row-1 and c!=column-1:
        a = [arr[r][[c-1,c+1]],arr[r-1][[c,c+1,c-1]]]
        return a
    elif r==row-1 and c==column-1:
        a = [arr[r][c-1],arr[r-1][[c-1,c]]]
        return a
    elif c==0:
        a = [arr[r-1][[c,c+1]],arr[r][c+1],arr[r+1][[c,c+1]]]
        return a
    elif c==column-1:
        a = [arr[r-1][[c,c-1]],arr[r][c-1],arr[r+1][[c,c-1]]]
        return a
    else:
        a = [arr[r-1][[c-1,c,c+1]],arr[r][[c-1,c+1]],arr[r+1][[c-1,c,c+1]]]
        return a

def neigbour_compare(r,c,neigbours):
    a = True
    for x in neigbours:
        if type(x)==np.ndarray:
            for y in x:
                #print(f"arr{r}{c} <= {y}")
                if arr[r][c] <= y:
                    a= False
        else:
            if arr[r][c] <= x:
                a= False
        #print(a)
    if a:
        dom_val.append((r,c))

for x in range(row):
    for y in range(column):
        neigbour_compare(x,y,neigbours(arr,x,y))

print(arr)
print(dom_val)