Text = str(input("\n\n Enter your text : "))
l=len(Text)
def est_valid(Txt):
    B = True
    if len(Txt)%4 != 0:
        B = False
    else:
        while i < len(Txt) and B == True :
            if (Txt[i]=='0' and Text[i+1] in '123456789') or (Txt[i]=='1' and Txt[i+1]in '0123456'):
                B = True
            else:
                B = False
            i=i+2
    return B        
                        
while True:
        try:
            Type = int(input(" Enter 1 if you want encrypt or 0 if you want decrypt : "))
            if Type in [0, 1]:
                break
            else:
                print("Please enter 0 or 1 only.")
        except ValueError:
            print("Please enter 0 or 1 only.")
if (Type==1):
    M=[]
    for x in Text:
        i=ord(x)//16+1
        j=ord(x)%16+1
        i=str(i)
        if (len(i)==1):
            i='0'+i
        M.append(i)
        j=str(j)
        if (len(j)==1):
            j='0'+j    
        M.append(j)
    New_text="".join(map(str, M))
    print(f"\n The result is : {New_text}  \n")
    print("\n")

else : 
    M=[]
    while (est_valid(Text)==False):
        Text = str(input("\n\n pleaze Enter another text : "))
    Text = list(Text)
    Text = [int(k) for k in Text]
    p=0
    while p < l :
        i = Text[p]*10 +Text[p+1]
        j =Text[p+2]*10 + Text[p+3]
        n =(i-1)*16 + (j-1)
        M.append(chr(n))
        p=p+4
    T="".join(M)
    print("\n\n the result is:  " , T)
