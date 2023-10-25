for x in range(174457,174505+1):
    k=0
    s=[]
    for y in range(2,x//2+1):
        if x%y==0:
            k+=1
            s.append(y)
            if k>2:
                break
    if k==2:
        print(*s)