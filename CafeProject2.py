import shelve
import time
import datetime
from datetime import date

def menu_header():
    item = ["Code no.","Menu","Price"]
    print('{:^20s}{:^20s}{:>20s}'.format(item[0],item[1],item[2]))
    dot = '.' * 65
    print(dot)

def bill_header():
    dot = '.' * 70
    print(dot)
    item = ["Item name","Quantity","Price"]
    print('{:^20s}{:^20s}{:>20s}'.format(item[0],item[1],item[2]))
    print(dot)

def menu_print(key,value):
    print('{:^20s}{:^20s}{:>20s}'.format(key, value[0], value[1]))

def bill_print(list):
    print('{:^20s}{:^20s}{:>20s}'.format(list[0], list[1], list[2] ))

def menu():
    print("\n\n\t\t\t\t\tThe Menu of Cafe LOEY\n")

    print(">>>> Coffee <<<<\n")
    menu_header()
    for (key, value) in file.items():
        if 0 < int(key) < 5:
            menu_print(key, value)

    print("\n>>>> Cake <<<<\n")
    menu_header()
    for (key, value) in file.items():
        if 4 < int(key) < 9:
            menu_print(key, value)

    print("\n>>>> Tea <<<<\n")
    menu_header()
    for (key, value) in file.items():
        if 8 < int(key) < 13:
            menu_print(key, value)

    print("\n>>>> Snack <<<<\n")
    menu_header()
    for (key, value) in file.items():
        if 12 < int(key) < 17:
            menu_print(key, value)

def updatemenu():
    print("\nUpdated menu\n")
    menu_header()
    for (key, value) in file.items():
        if key == oldcode:
            menu_print(key, value)

def bill():
    print("\n\n\t\t\t\t\t\t\tThe Cafe LOEY\n")
    print(datetime.datetime.now())
    print("token number : " , token)
    bill_header()
    for (key,value) in order_bill.items():
        if key == token:
            for list in value:
                bill_print(list)

    dot = '.' * 70
    print(dot)
    for key in order_sum.keys():
        if key == token:
            price = sum(order_price)
            print('{:^20s}{:^20s}{:>20d}'.format("Total","  ", price))

def countdown(t=5):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
        print(timer, end='\t')
    print('\nYour order is here.')

token = int()
num = int()

print("\n\t\t\t\tWelcome from The Cafe LOEY")
choose = input("\nWhich service do you want to use?\nOwner or Customer : ")

if choose == "owner":
    while 1:
        password = input("\nEnter password : ")

        if password == "Cy271192":
            while 1:
                print("\nChoose the following function.")
                print("1 for Adding menu\n2 for Updating menu\n3 for Showing menu\n"
                      "4 for Searching menu\n5 for Checking order")
                menu_order = int(input(">>>"))

                if menu_order == 1:
                    try:
                        file = shelve.open("menu")
                    except IOError:
                        print("File cannot be opened.")

                    print("\nEnter code no,menu name,price.\nEnter done if you finish adding.")

                    while 1:
                        menu_code = input("\nEnter menu code number : ")
                        menu_info = input("Enter menu name (space) price : ")

                        if menu_code and menu_info == "done":
                            break
                        else:
                            file[menu_code] = menu_info.split()
                            continue

                    file.close()

                if menu_order == 2:
                    try:
                        file = shelve.open("menu")
                    except IOError:
                        print("File cannot be opened.")

                    while 1:
                        print("\nEnter done if you finish.")
                        update = input("What do you want to update (menu name or price) ? : ")

                        if update == "menu name":
                            oldcode = input("\nEnter the code no. of menu that you want to update : ")

                            for (key,value) in file.items():
                                if key == oldcode:
                                    print("It is", value[0], value[1])
                                    break

                            menuname = input("\nEnter new menu name : ")

                            for key in file.keys():
                                if key == oldcode:
                                    file[key] = list([menuname, file[key][1]])

                            updatemenu()
                            continue

                        elif update == "price":
                            oldcode = input("\nEnter the code no. of menu that you want to update : ")

                            for (key, value) in file.items():
                                if key == oldcode:
                                    print("It is", value[0], value[1])

                            menuprice = input("\nEnter new price : ")

                            for key in file.keys():
                                if key == oldcode:
                                    file[key] = list([file[key][0], menuprice])

                            updatemenu()
                            continue

                        elif update == "done":
                            break

                    file.close()

                if menu_order == 3:
                    try:
                        file = shelve.open("menu")
                    except IOError:
                        print("File cannot be opened.")

                    menu()

                    file.close()

                if menu_order == 4:
                    try:
                        file = shelve.open("menu")
                    except IOError:
                        print("File cannot be opened.")

                    while 1:
                        print("\nEnter done if you finish.")
                        search = input("Enter the menu name that you want to search : ")

                        if search == "done":
                            break
                        else:
                            for value in file.values():
                                if search == value[0]:
                                    print("\nHere is the menu that you are searching for.\n")
                                    menu_header()
                                    for (key,value) in file.items():
                                        if search == value[0]:
                                            menu_print(key, value)
                                            continue

                    file.close()

                if menu_order == 5:
                    Q = []
                    try:
                        orderfile = shelve.open("order")
                    except IOError:
                        print("File cannot be opened.")

                    today = date.today()
                    print("\nDate : ",today.strftime("%d/%m/%Y"))

                    for (key,value) in orderfile.items():
                        if type(value) is dict:
                            for (key, value) in value.items():
                                print("\nToken : ", key)
                                for list in value:
                                    bill_print(list)
                                    P = int(list[2])
                                    Q.append(P)

                    print("\nTotal bill of all order : ", sum(Q))

                    orderfile.close()

                q = input("\nDo you want to do another function? (yes or no) : ")
                if q == "yes":
                    continue
                if q == "no":
                    exit()

        else:
            print("\nTry again.Please Enter the correct password.")
            continue


if choose == "customer":
    try:
        orderfile = shelve.open("order")
    except IOError:
        print("File cannot be opened.")

    for value in orderfile.values():
        if len(value) == 0:
            token += 1
        if len(value) != 0:
            l = len(value)
            token += l

    orderfile.close()

    while 1:
        order_bill = dict()
        order_sum = dict()
        order_list = list()
        order_price = list()

        try:
            file = shelve.open("menu")
        except IOError:
            print("File cannot be opened.")

        menu()

        T = bool(token)
        if T == True:
            token += 1
        if T == False:
            token = 1

        print("\nEnter the code no. of menu and quantity that you want to order.\neg. 16,2 (if you want 2 Hotdog)")
        print("Enter done if you finish.")

        while 1:
            order = input("\nCode no. and quantity >>>> ")

            if order == "done":
                break
            else:
                split = order.split(",")
                for (key, value) in file.items():
                    if key == split[0]:
                        print(value[0], "\t", split[1])

                        x = (int(file[key][1]) * int(split[1]))
                        y = [value[0], split[1], str(x)]

                        order_list.append(y)
                        order_price.append(x)
                        continue

        order_bill[token] = order_list
        order_sum[token] = order_price
        for key in order_sum.keys():
            if key == token:
                price = sum(order_price)
                print(price)

        bill()

        bill_input = int(input("\nEnter bill : "))

        if bill_input == price:
            print("\nPlease wait for your order.")
            countdown()

        elif bill_input > price:
            extra = bill_input - price
            print("\nHere is extra money ", extra)
            print("\nPlease wait for your order.")
            countdown()

        elif bill_input < price:
            need = price - bill_input
            print("\nYour bill amount still needs ", need)
            need_input = int(input(">>>>"))
            if need_input == need:
                print("\nPlease wait for your order.")
                countdown()

        token_input = int(input("\nEnter your token number : "))
        if token_input == token:
            print("\n\n\t\t\t\t\tThank you for dining with us.")
            print("\n\t\t\t\t\t\t\tSee you again.")

        file.close()

        try:
            orderfile = shelve.open("order")
        except IOError:
            print("File cannot be opened.")

        if len(orderfile) == 0:
            key = 1
            k = str(key)
            orderfile[k] = order_bill
            break
        if len(orderfile) != 0:
            for key in orderfile.keys():
                k = int(key)
                k += len(orderfile)
                kk = str(k)
                orderfile[kk] = order_bill
                break

        orderfile.close()

        z = input("\nDo you want to order again (yes or no)? :")
        if z == "yes":
            continue
        if z == "no":
            print("\nThank you so much.")
            exit()


