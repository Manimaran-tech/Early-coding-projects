def purchase():
    global fruits,l
    n=int(input("How many fruits gonna purchase:"))
    for i in range(1,n+1):
        order=input("Enter name of fruit " + str(i)+":")
        l.append(order)
    print("The fruits purchased :",l)
    return l
def kg():
    global fruits,l
    for num in range(0,len(l)):
        b=float(input(str(l[num])+" how many [kg]:"))
        fruits[l[num]]=fruits.get(l[num])*b
    #To sort them in alphabetical order
    l.sort()
    return l,fruits
def bill():
    global fruits,l
    q=len(l)
    print('===========================BILL===========================')
    s=0
    import math
    for j in range(q):
        print("Amount of",l[j],':',fruits.get(l[j]))
        v=fruits[l[j]]
        s=s+v
    math.ceil(s)
    print("The total bill amount is :",s)    
    print('=========================THANKYOU=========================')
#MODULE
def fruit_shop():
    purchase()#calling the funtion
    kg()
    bill()
#MAIN PROGRAM
print('Fruits available in our shop')
print('=======================FRUITS MENU========================')
#Main dictionary with default 1 Kg
fruits=dict({'apple':150,'orange':125,'blue berry':100,'cherry':65,'fig':45,'kiwi':120,'lime':60,
             'straw berry':135,'black berry':120,'pears':100,'rasp berry':110,'plum':140,'star fruit':100,
             'banana':135,'guava':90,'grapes':95,'lychee':110,'green apple':110,'pomegranate':115,'mango':170,'lemon':90,})
#For 1Kg
for key,value in fruits.items():
    print(key,":",value)
print("Every thing displayed here is for 1Kg")
print('==========================================================')
l=[]
fruit_shop()#callling the module
