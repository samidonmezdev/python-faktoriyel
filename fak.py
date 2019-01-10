def fak(n):
    if(n==0):
        return 1
    else:
        toplam=1
        for i in range(1,n+1):
            toplam=toplam*i

        return toplam

c=fak(n)/(fak(n-r)*fak(r))
print(c)
