def countchar (fname):
    vowels="aeiouAEIOU"
    vcount=ccount=ucount=lcount=0
    with open(fname,"r")as file:
        text=file.read()
        for char in text:
            if char. isalpha():
                if char in vowels:
                    vcount+=1
                else:
                    ccount+=1
            if char. isupper():
                ucount+=1
            elif char. islower():
                lcount+=1
    print("vowels:", vcount)
    print("consonants:",ccount)
    print("upper characteritics:",ucount)
    print("lower characteritics:",lcount)
def creatfile(fname,content):
    with open(fname,"w")as file:
        file.write(content)
fname="sample.txt"
content=input("enter a number:")
creatfile(fname,content)
countchar(fname)


        







    