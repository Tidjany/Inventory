#Shopify Backend Developer Intern Challenge - Summer 2022
#Tidjany Hindy



#Dictionaries
unit_price={}
description={}
stock={}

#Open file with stock
details = open("stock.txt","r")

#First line of the file is the number of items
no_items  = int((details.readline()).rstrip("\n"))

#Add items to dictionaries
for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=float(x2)
    unit_price.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    description.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=int(x2)
    stock.update({x1: x2})

details.close()

shipment=[]

c="y" #Runs the while loop as long as user wants


#UI
print("Welcome to the Invenotry Tracking Application")
print()
print("A-Add an item")
print("R-Remove an item")
print("E-Edit specifics of an item")
print("L-List all items")
print("S-Create Shipment")
print("F-Finalize Shipment")
print("T-List Shipments")
print("Q-Quit")
print("help-See all commands again")
print()

total_cost=0 
flag=0 #Shipment Check

while(c!= "q" or c!= "Q"):
    c= input("What would you like to do? ")
    
    if(c=="q" or c=="Q"):
        break
        
    elif(c=="A" or c=="a"):#Add an item
        p_no = int(input("Enter part number: "))
        p_pr = float(input("Enter part price: "))
        p_desc = input("Enter part description: ")
        p_stock = int(input("Enter part stock: "))
        
        m=0
        for i in range(0,len(unit_price)):
            if(p_no in unit_price):
                p_no+=1
                m=1
        if(m==1):
            print()
            print("That part number already exists, changing value to ",p_no)
                
        unit_price.update({p_no: p_pr})
        description.update({p_no: p_desc})
        if(p_stock > -1):
            stock.update({p_no: p_stock})
        else:
            p_stock = 0
            stock.update({p_no: p_stock})
            print("The stock of an item cannot be negative, the stock has been set to 0.")
        print()
        print("Item number: ",p_no," Description: ",description.get(p_no)," Price: ",unit_price.get(p_no)," Stock: ",stock.get(p_no))
        print("Item was added successfully!")
        print()
        
    elif(c=="E" or c=="e"):#Edit an item
        print()
        p_no = int(input("Enter part number: "))
        if(p_no in unit_price):
            p_pr = float(input("Enter part price: "))
            p_desc = input("Enter part description: ")
            p_stock = int(input("Enter part stock: "))
                
            unit_price.update({p_no: p_pr})
            description.update({p_no: p_desc})
            stock.update({p_no: p_stock})
            
        else:
            print("That item does not exist, to add an item use a")
        print()
    
            
    elif(c=="R" or c=="r"):#Remove an item
        print()
        p_no = int(input("Enter part number: "))
        if(p_no in unit_price):
            are_you_sure = input("Are you sure you want to remove that item(y/n)? ")
            if(are_you_sure=="y" or are_you_sure=="Y"):
                unit_price.pop(p_no)
                description.pop(p_no)
                stock.pop(p_no)
                print("Item successfully removed!")
            print()
        else:
            print("Sorry, we don't have such an item!")
            print()
        
    elif(c=="L" or c=="l"):#List all the items
        print()
        print("Items and their prices: ",unit_price)
        print("Descriptions: ",description)
        print("Stock left of Item: ",stock)
        print()

        
    elif(c=="S" or c=="s"):#Create Shipment
        print()
        p_no = int(input("Enter Item number: "))
        if(p_no in unit_price):
            if(flag==1):
                flag=0
            stock_current = stock.get(p_no)
            if(stock_current>0):
                stock_current = stock.get(p_no)
                stock[p_no] = stock_current-1
                print(description.get(p_no),"Shipment created ")
                shipment.append(p_no)
            else:
                print("We don't have that item in stock!")
        else:
                print("We don't have such an item!")
        print()
  
    elif(c=="F" or c=="f"):#Finlaize Shipment
        print()
        print("You shipped the following items: ",shipment)
        flag=1
        print()
        print("To quit press q")
        print()

        
    elif(c=="help"):#Display all commands
        print()
        print("A-Add an item")
        print("R-Remove an item")
        print("E-Edit specifics of an item")
        print("L-List all items")
        print("S-Create Shipment")
        print("F-Finalize Shipment")
        print("T-List Shipments")
        print("help-See all commands again")
        print()

                
    elif(c=="t" or c=="T"):#prints list shipment
        print()
        print(shipment)
        print()
        
#Write the updated inventory to the file
details = open("stock.txt","w")
no_items=len(unit_price)
details.write(str(no_items)+"\n")
for i in range(0,no_items):
    details.write(str(i+1)+"#"+str(unit_price[i+1])+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1)+"#"+description[i+1]+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1)+"#"+str(stock[i+1])+"\n")
    
details.close()
