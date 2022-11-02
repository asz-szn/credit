
x = input("Card Number?")

while len(x) != 15: ### First length check
    x = input("Card Number?")
else: condition1 = True

if len(x) == 16: ### Mastercard & 16-Visa Check
    if x[0] == '5' & x[1] == '1' or '2' or '3' or '4' or '5':
        cardtype = "Mastercard"
    else: 
        print("Invalid Card")
        quit('Invalid')

    if x[0] == 4:
        cardtype = "Visa"
    else: 
        print("Invalid Card")
        quit('Invalid')
    

    i = len(x) - 2
    temp = []
    while True:
        temp.insert(1, str(int(x[i]) * 2))
        i = i - 2
        if i < 0:
            break
    
    joined = "".join(temp)
    digits1 = sum(int(i) for i in joined)
    
    u = len(x) - 1
    temp2 = []
    while True:
        temp2.insert(1, int(x[u]))
        u = u - 2
        if u <= 0:
            break
    
    digits2 = digits1 + sum(temp2)
    if digits2 % 10 == 0:
        condition2 = True
    else: 
        print("Invalid Card")
        quit('Invalid')

if len(x) == 15: ### Amex Check
    if int(x[0]) == 3 & int(x[1]) == 4 or 7:
        cardtype = "Amex"
    else: 
        print("Invalid Card")
        quit('Invalid')
        
    i = len(x) - 2
    temp = []
    while True:
        temp.insert(1, str(int(x[i]) * 2))
        i = i - 2
        if i < 0:
            break
    
    joined = "".join(temp)
    digits1 = sum(int(i) for i in joined)
    u = len(x) - 1
    temp2 = []
    while True:
        temp2.insert(1, int(x[u]))
        u = u - 2
        if u < 0:
            break
    
    digits2 = digits1 + sum(temp2)
    if digits2 % 10 == 0:
        condition2 = True
    else:
        print("Invalid Card")
        quit('Invalid')
    
if len(x) == 13: ### 13-Visa check
    if x[0] == '4':
        cardtype = "Visa"
    else: 
        print("Invalid Card")
        quit('Invalid')
        
    i = len(x) - 2
    temp = []
    while True:
        temp.insert(1, str(int(x[i]) * 2))
        i = i - 2
        if i < 0:
            break
    
    joined = "".join(temp)
    digits1 = sum(int(i) for i in joined)
    u = len(x) - 1
    temp2 = []
    while True:
        temp2.insert(1, int(x[u]))
        u = u - 2
        if u < 0:
            break
    
    digits2 = digits1 + sum(temp2)
    if digits2 % 10 == 0:
        condition2 = True
    else:
        print("Invalid Card")
        quit('Invalid')

if condition1 == True & condition2 == True:
    print("Valid " + cardtype + " Card")
else: print('Invalid Card')
