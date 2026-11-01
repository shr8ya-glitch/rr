a=3000
for n in range(1,a+1):
    c=0
    r=0
    t=n
    for i in range(1,t+1):
        if t%i==0:
            c=c+1
    if c==2:
        while t>0:
            r =r*10+(t%10)
            t//=10
        if r==n:
            print(n)