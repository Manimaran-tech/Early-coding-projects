print("\t\t\t !!!!!!!WELCOME TO CRICKET GAME!!!!!!! ")
print('\t\t \t     !!!!ITS A 1 OVER MATCH!!!! ')
print("The limit is 0 to 10 if you enter the number greater than 10 it shows error and does not add you runs")
print("Your batting")
l=[]
s=0
for i in range(1,6+1):
    a=int(input("Face the " + str(i) + " ball:"))
    import random
    d=random.randint(0,10)
    print("The bowler kept :",d)
    if a>10:
        print("Error")
        break
    elif a==0 and d!=0:
        l.append(d)
        s=sum(l)
    elif a!=d:
        l.append(a)
        s=sum(l)
    elif a==0 and d==0:
        print("Play 1 or 2")
        c=input("Did you want to know the rules[yes,no]:")
        if c=="yes":
            print("If both numbers are same its means out if not your not out")
            for j in range(1):
                x=int(input("Strike the " + "1" + " ball:"))
                z=random.randint(1,2)
                print(z)
            if x!=z:
                print("your not out")
                l.append(0)
                continue 
            elif x>2:
                print("Sorry you kept wrong number \n that means your out ")
            elif x==z:
                print("You are out")
                l.append("W")
                break
            else:
                continue   
        else:
            for j in range(1):
                x=int(input("Strike the " + "1" + " ball:"))
                z=random.randint(1,2)
                print(z)
            if x!=z:
                print("your not out")
                l.append(0)
                continue 
            elif x>2:
                print("Sorry you kept wrong number \n that means your out ")
            elif x==z:
                print("You are out")
                l.append("W")
                break
            else:
                continue
    else:
        l.append("W")
        print("Your are out")
        break
print("The over played:",l)
print("The total runs is:",s)
print("Your bowling")
l2=[]
s2=0
for k in range(1,6+1):
    a=int(input("bowl the " + str(k) + " ball:"))
    import random
    d=random.randint(0,10)
    print("The PC kept :",d)
    if d>10:
        print("Error")
        break
    elif d==0 and a!=0:
        l2.append(a)
        s2=sum(l2)
    elif d!=a:
        l2.append(d)
        s2=sum(l2)
    elif a==0 and d==0:
        print("Play 1 or 2")
        for j in range(1):
                x=int(input("Strike the " + "1" + " ball:"))
                z=random.randint(1,2)
                print(z)
        if z!=x:
            print("Pc is not out")
            l2.append(0)
            continue
        elif z>2:
            print("Sorry you kept wrong number \n that means your out ")
        elif z==x:
            print("Pc is out")
            l2.append("W")
            break
        else:
            continue
    else:
        l2.append("W")
        print("Pc is out")
        break
    if s2>s:
        break
    else:
        pass
print("The over pc played:",l2)
print("The total runs is:",s2)
import math
m=math.fabs(s-s2)
if s2>s :
    print("THE PC WON THE MATCH IN THE DIFFRENCE OF",m)
elif s==s2:
    print("MATCH DRAW")
else:
    print("YOU HAVE WON THE MATCH IN THE DIFFRENCE OF",m)
print("Run the program to play again")
