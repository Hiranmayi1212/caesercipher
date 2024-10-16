from alphabetic import WritingSystem

# Create a WritingSystem instance to access all core functions
ws = WritingSystem()

# Retrieve the alphabet of the language
a=ws.by_language(ws.Language.English, letter_case=ws.LetterCase.Lower, as_list=True)


def encrypt(n,c):
    return n+c
    
def decrypt(n,c):
    return n-c

c=int(input("enter the cipher value"))
s=input("enter string ")
d=int(input("enter 1 for encrypt 2 for decrypt"))
for i in s:
        if i.lower() in a:
            n=a.index(i.lower())
            if d==1:
                n=encrypt(n,c)
            elif d==2:
                n=decrypt(n,c)
            b=a[(n%25)]
            if i.isupper()==True:
                b=b.upper()
            s=s.replace(i,b)

print(s) 