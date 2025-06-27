#This code encrypts and decrypts the text entered by the user after he chooses the operation he wants ( Cesar + Polyb )..........

print(f"\n\n\n\t\t\t\t\t\t\t\t{chr(5)} Welcome {chr(5)}\n\n\n")

Try_again='1'
while (Try_again=='1'):
    while True:
        choice = input("  Enter 'C' for Cesar or 'P' for Polyb : ")
        if ( (choice=='c') or (choice=='C') or (choice=='p') or (choice=='P') ):
            break
        else:
            print("  Please choose C or P only.")
    # Cesaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaar...........................
    if ( (choice=='c') or (choice=='C') ):
        print("\n\n\t\t\t\t\t\t\t\t  -Cesar-")
        Text = str(input("\n\n  Enter your text : "))
        while True:
            try:
                Key = int(input("  Enter your key : "))
                break
            except ValueError:
                print("  Please enter a valid integer for the key. ")
        while True:
            try:
                Type = int(input("  Enter 1 if you want encrypt or 0 if you want decrypt : "))
                if Type in [0, 1]:
                    break
                else:
                    print("  Please enter 0 or 1 only.")
            except ValueError:
                print("  Please enter 0 or 1 only.")
        Text=list(Text)
        New_text =[]
        Key=Key%256
        if  (Type==0):
            Key=-Key
        for i in Text:
            y = (ord(i) + Key )%256
            New_text.append( chr(y) )
        New_text="".join(New_text)
        print(f"\n  The result is : {New_text} \n\n")
    #Polyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyb
    elif ( (choice=='p') or (choice=='P') ):
        print("\n\n\t\t\t\t\t\t\t\t  -Polyb-")
        Text=str(input("\n  Enter your text : "))
        L=len(Text)
        def is_valid(t):
            B=True
            if (len(t)%4!=0):
                B=False
            else:
                i=0
                while ((i<len(t)) and (B==True)):
                    if (t[i]=='0' and t[i+1] in '123456789') or (t[i]=='1' and t[i+1] in '0123456'):
                        B=True
                    else:
                        B=False
                        break
                    i=i+2
            return B
        while True:
            try:
                Type=int(input("  Enter 1 if you want encrypt or 0 if you want decrypt : "))
                if Type in [0,1]:
                    break
                else:
                    print("  Please enter 0 or 1 only.")
            except ValueError:
                print("  Please enter 0 or 1 only.")

        if (Type==1):
            M=[]
            for x in Text:
                i=ord(x)//16+1
                j=ord(x)%16+1
                i=str(i)
                if(len(i)==1):
                    i='0'+i
                M.append(i)
                j=str(j)
                if(len(j)==1):
                    j='0'+j
                M.append(j)
            New_text="".join(M)
            print(f"\n  The result is : {New_text} \n\n")
        else:
            while (is_valid(Text)==False):
                print("\n  Your Text is not valid for this operation.")
                print("  -> The length of your text must be a multiple of 4.")
                print("  -> Text must consist of numbers only to specify letters.")
                Text=str(input("\n  Please enter another text : "))

            Text=list(Text)
            Text=[ int(i) for i in Text ]
            M=[]
            i=0
            while (i<len(Text)):
                x=Text[i]*10+Text[i+1]
                x=(x-1)*16
                x=x+Text[i+2]*10+Text[i+3]-1
                M.append(chr(x))
                i=i+4
            New_text="".join(M)
            print(f"\n  The result is : {New_text} \n\n")
    Try_again= input("  Enter 1 if you want try again : ")
    if (Try_again!='1'):
        print(f"\n\n\n\t\t\t\t\t\t\t\t {chr(4)} End {chr(4)}")
        print("\t\t\t\t\t\t\t\t Goodbye \n\n")
    else:
        print("\n\n  *****************************************************        Another try        ******************************************   \n\n")