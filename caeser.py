from alphabetic import WritingSystem

# Create a WritingSystem instance to access all core functions
ws = WritingSystem()

# Retrieve the alphabet of the language
a=ws.by_language(ws.Language.English, letter_case=ws.LetterCase.Lower, as_list=True)


def encrypt(c,s):
    for i in s:
        if i.lower() in a:
            n=a.index(i.lower())
            n=n+c
            b=a[(n%25)]
            if i.isupper()==True:
                b=b.upper()
            s=s.replace(i,b)
        
    print(s) 
    
def decrypt(c,s):
    for i in s:
        if i.lower() in a:
            n=a.index(i.lower())
            n=n-c
            b=a[(n%25)]
            if i.isupper()==True:
                b=b.upper()
            s=s.replace(i,b)
    print(s) 

c=int(input("enter the cipher value"))
s=input("enter string ")
d=int(input("enter 1 for encrypt 2 for decrypt"))
if d==1:
    encrypt(c,s)
elif d==2:
    decrypt(c,s)
