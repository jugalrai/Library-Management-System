from datetime import date
import datetime
date=datetime.datetime.today()
file=open('Header.txt','r')
Header=file.readlines()
for lines in Header:
    print(lines)
    print()
file.close()

file=open('Stock.txt','r')
Book=file.readlines()

list=[]
for l in Book:
    list.append(l.replace("\n"," ").split(","))

for line in Book:
    print(line)
file.close()
selectid=[]
bookname=[]
author=[]
quantity=[]
price=[]
for column in list:
    selectid.append(column[0])
    bookname.append(column[1])
    author.append(column[2])
    quantity.append(column[3])
    price.append(column[4])
file.close()

def writeStock():
    file=open('Stock.txt','w')
    for i in range(0,len(selectid),1):
        file.write(str(selectid[i]) +',' )
        file.write(''+str(bookname[i]) +',' )
        file.write(''+str(author[i]) +',' )
        file.write(''+str(quantity[i]) +',' )
        file.write(''+str(price[i]))
        file.write("\n")
    file.close()

def borrow():
    result=int(quantity[bookid-1])-1
    quantity[bookid-1]="      "+str(result)+"        "
    print("The number of remaining book is : "+str(result))
    now = date.today()
    pay = amount()
    file = open('Borrow.txt','a')
    file.write("Name: "+ name +
               "\n"+ "BookID: "+ str(bookid)+"\n" +
               "Current Date: "+ now.strftime("%B %d, %Y")+"\n"+
               "Amount: "+ str(pay)
                +"\n")
    file.close()
    file = open('Books.txt','a')
    file.write( name +
               ","+ str(bookid) +
               ","+ now.strftime("%B %d %Y")+
               ","+ str(pay)
                +"\n")
    file.close()


def deposit():
    result=int(quantity[bookid-1])+1
    quantity[bookid-1]="      "+str(result)+"        "
    print("The number of remaining book is : "+str(result))
    deposite = open('Books.txt','r')
    read = deposite.readlines()
    empty=[]
    check=[]
    for line in read:
        empty.append(line.replace("\n","").split(","))
    deposite.close()
    total_paid = 0
    now = date.today()
    days = now.strftime("%B %d %Y")
    for seperatevalue in empty:
        if (name == seperatevalue[0]):
            if(str(bookid)==seperatevalue[1]):
                check.append(seperatevalue)   
    for firstlist in check:
        if (name == firstlist[0]):
            if(str(bookid) == firstlist[1]):
                days=int(input("how many days did you borrow a Books?"+"\n"+"= "))
                if (days>10):
                    total_paid+=float(firstlist[3])*(days-10)
                elif (days==10):
                    total_paid=0
                else:
                    total_paid=0
            else:
                print("You have not borrow this book.")
                break
        else:
            print("You have not borrow any book.")
            break
            
    print("Thank You for returning a Book.")
    print("I hope you enjoy it!")

    file = open('Return.txt','a')
    file.write("Name: "+ name +
               "\n"+ "BookID: "+ str(bookid)+"\n" +
               "Current Date: "+ str(date)+"\n"+
               "Charged: "+ str(total_paid)
                +"\n")
    file.close()
    
def amount():
    amount=float(price[bookid-1])
    return amount


name=str(input("Enter your name: "))
collegeid=str(input("Enter your college id: "))
ans='y'
while ans=='y':
    index=0
    bookid=int(input('Enter the book id: '))
    for i in range(0,len(selectid),1):
        if(bookid==int(selectid[i])):
            index+=1
            userinput=int(input("Press 1 to borrow or 2 to deposit:"))
            if(userinput==1):
                borrow()
                pay=amount()
                writeStock()
                #success=True
            elif(userinput==2):
                deposit()
                pay=amount()
                writeStock()
                #success=True
    if(index==0):
        print('The book is not here: ')
    ans=str(input("Press y to continue or any key to exit:"))
#else:
#print('The book is not here')
