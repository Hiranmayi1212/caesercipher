from alphabetic import WritingSystem

# Create a WritingSystem instance to access all core functions
ws = WritingSystem()

# Retrieve the alphabet of the language
a=ws.by_language(ws.Language.English, letter_case=ws.LetterCase.Lower, as_list=True)



c=int(input("enter the cipher value"))
s=input("enter string to be encrypted")
for i in s:
    if i.lower() in a:
        n=a.index(i.lower())
        n=n+c
        b=a[(n%25)]
        if i.isupper()==True:
            b=b.upper()
        print(b)
        s=s.replace(i,b)
        
print(s) 