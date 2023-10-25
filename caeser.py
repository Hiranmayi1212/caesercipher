a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encrypt(c,s):
    for i in s:
        if i in a:
            n=a.index(i)
            n=n-c
            b=a[(n%25)]
            s=s.replace(i,b)
        
    print(s) 

def decrypt(c,s):
    for i in s:
        if i in a:
            n=a.index(i)
            n=n-c
            b=a[(n%25)]
            s=s.replace(i,b)
        
    print(s) 

c=int(input("enter the cipher value"))
s=input("enter string ")
d=int(input("enter 1 for encrypt 2 for decrypt"))
if d==1:
    encrypt(c,s)
elif d==2:
    decrypt(c,s)
