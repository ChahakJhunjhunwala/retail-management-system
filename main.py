import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime
print("                                                                                                              Welcome to retail(appraisal) store")
print("\n")
while True:
    #MAIN MENU
    print("Main Menu:")
    print("1.help")
    print("2.ADMIN")
    print("3.SALES")
    print("4.STOCK")
    print("5.EXIT")
   
    n=int(input("choose an option from  main menu:"))
    if n==1:
        file_path ="password.txt"
        with open(file_path, 'r') as file:
            file_contents = file.read()
            print("content of help file")
            print(file_contents)
    elif n==2:
        #ADMIN
        x='ADMIN_123'
        p=input("enter the password:")
        if p==x:
            while True:
                print("menu for retriving data from admin:")
                print("1.display all the products")
                print("2.add any new product")
                print("3.delete any product")
                print("4.modify the price of any product")
                print("5.Employee")
                print("6.Exit")
                n1=int(input("enter your choice:"))
                if n1==1:
                    #DISPLAYING THE PRODUCT LIST
                    df1=pd.read_csv("D:\\chahak_project\\product_list.csv")
                    print("the product list is:")
                    print(df1)
                elif n1==2:
                    #ADDING A NEW PRODUCT
                    n2=int(input("enter no of new products"))
                    dk=pd.read_csv("D:\\chahak_project\\product_list.csv")
                    for i in range(n2):
                        pc=int(input("enter product code:"))
                        if pc in dk["PRODUCT CODE"].values:
                            print("product code already exist")
                           

                       
                        else:
                            gen=input("enter gender in upper case:")
                            br=input("enter brand in upper case:")
                            ct=input("enter clothes type in upper case:")
                            pp=int(input("enter product price:"))
                            dop=input("enter date of purchase(yyyy-mm-dd)")
                            qp=int(input("enter the quantity purchased:"))
                            new_roll1=[pc,gen,br,ct,pp,dop,qp]
                            with open("D:\\chahak_project\\product_list.csv", mode='a', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(new_roll1)
                            print(pc,"new product added")
                           
                       
                elif n1==3:
                    df = pd.read_csv("D:\\chahak_project\\product_list.csv")
                   
                    product_code_to_delete = int(input("Enter the product code to delete: "))
                    if product_code_to_delete in df['PRODUCT CODE'].values:
                        # Delete the row(s) with the specified product code
                        df = df[df['PRODUCT CODE'] != product_code_to_delete]
                       
                        df.to_csv("D:\\chahak_project\\product_list.csv", index=False)
                       
                        print("Product with code", product_code_to_delete," deleted successfully.")
                    else:
                        print("Product with code", product_code_to_delete," was not found.")
                elif n1==4:
                    df = pd.read_csv("D:\\chahak_project\\product_list.csv")
                    product_code_to_modify = int(input("Enter the product code to modify: "))
                    if product_code_to_modify in df['PRODUCT CODE'].values:
                        new_price = int(input("Enter the new price: "))
                        # Modify the price in the DataFrame
                        df.loc[df['PRODUCT CODE'] == product_code_to_modify, 'PRODUCT PRICE'] = new_price
                        df.to_csv("D:\\chahak_project\\product_list.csv", index=False)
                        print("Price for product with code",product_code_to_modify,"modified successfully.")
                    else:
                        print(f"Product with code ",product_code_to_modify," not found.")
                elif n1==5:
                    print("1:Add a new record ")
                    print("2: Display the detail")
                    print("3: Display the details of a specific employee")
                    print("4.modify")
                    emp1=int(input("enter your choice:"))
                    if emp1==1:
                        nn=int(input("enter the number of record:"))
                        dk=pd.read_csv("D:\\chahak_project\\emp_list.csv")
                        for y in range(nn):
                            empid=input("enter the id")
                            if empid in dk["EMP_ID"].values:
                                       print("employee id already exist")
                            else:
                                emp_n=input("enter the name ")
                                emp_s=int(input("enter the salary"))
                                emp_d=input('enter the designation in upper case')
                                doj=input("enter date of joining(yyyy-mm-dd)")
                                no=int(input("enter your number:"))
                                new_r=[empid,emp_n,emp_s,emp_d,doj,no]
                                with open("D:\\chahak_project\\emp_list.csv", mode='a', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow(new_r)
                        print("the record successfully added")    
                    elif emp1==3:
                        emp=pd.read_csv("D:\\chahak_project\\emp_list.csv")
                        ID=input("enter employee id to be displayed")
                        if ID in emp["EMP_ID"].values:
                            index = emp[emp["EMP_ID"] == ID].index[0]
                            print(emp.loc[index])
                        else:
                            print("employee id not found")
                    elif emp1==2:
                        print("the detail of employee:")
                        dk=pd.read_csv("D:\\chahak_project\\emp_list.csv")
                        print(dk)
                    elif emp1==4:
                        print("modify details:")
                        print("1.salary")
                        print("2.designation")
                        chc=int(input("enter your choice:"))
                        if chc==1:
                            df = pd.read_csv("D:\\chahak_project\\emp_list.csv")
                            emp_id_to_modify = input("Enter the product code to modify: ")
                            if emp_id_to_modify in df['EMP_ID'].values:
                                new_sal = int(input("Enter the new salary: "))
                                df.loc[df['EMP_ID'] == emp_id_to_modify, 'SALARY'] = new_sal
                                df.to_csv("D:\\chahak_project\\emp_list.csv", index=False)
                                print("salary for product with code",emp_id_to_modify,"modified successfully.")
                            else:
                                print("employee with code ",emp_id_to_modify," not found.")
                        elif chc==2:
                            df = pd.read_csv("D:\\chahak_project\\emp_list.csv")
                            emp_id_to_modify = input("Enter the product code to modify: ")
                            if emp_id_to_modify in df['EMP_ID'].values:
                                new_des = input("Enter the new designation: ")
                                df.loc[df['EMP_ID'] == emp_id_to_modify, 'DESIGNATION'] = new_des
                                df.to_csv("D:\\chahak_project\\emp_list.csv", index=False)
                                print("designation for product with code",emp_id_to_modify,"modified successfully.")
                            else:
                                print("employee with code ",emp_id_to_modify," not found.")

                   
                    else:
                        break
                else:
                    break
        else:
            print("incorrect password")
           
                       
                       
    elif n==3:
        #SALES
        y = 'SALES_456'
        a = input("Enter the password: ")
        if a == y:
            while True:
                print("Menu for retrieving data regarding the sale:")
                print("1 - Bills for customers")
                print("2 - Details regarding sales")
                print("3 - Sales report")
                print("4-exit")
                n2 = int(input("Enter your choice: "))
                if n2 == 1:
                     # MAKING BILLS FOR CUSTOMERS
                     invoice_no = 1000
                     df1 = pd.DataFrame(columns=['PRODUCT CODE', 'PRODUCT NAME', 'PRODUCT QUANTITY', 'PRICE'])
                     df2 = pd.DataFrame(columns=['CUSTOMER NAME', 'PHONE NUMBER', 'INVOICE NUMBER'])
                     while True:
                        df_product_list = pd.read_csv("D:/chahak_project/product_list.csv", index_col='PRODUCT CODE')
                        n = int(input("ENTER THE TOTAL NUMBER OF PRODUCTS PURCHASED: "))
                        total = 0
                        cust_name = input("Enter the name of the customer: ")
                        phone_no = int(input("Enter customer's phone number: "))
                        l = []
                        for i in range(n):
                            prod = int(input('Enter the product code: '))
                            qty = int(input("Enter the quantity of the products: "))
                            price = qty * df_product_list.at[prod, 'PRODUCT PRICE']
                            total += price
                            name = df_product_list.at[prod, 'BRAND']
                            l1 = [prod, name, qty, price]
                            l.append(l1)
                        gst = total * 0.12
                        print("WELCOME TO THE SUPERMARKET")
                        print("Invoice number:", invoice_no)
                        print(datetime.datetime.now())
                        print('Name:', cust_name)
                        print('Phone number:', phone_no)
                        print('PRODUCT CODE', '\t', 'PRODUCT NAME', '\t', 'PRODUCT QUANTITY', '\t', 'PRICE')
               
                        LEN=0
                        for i in range(n):
                            print('\t', l[LEN][0], '\t', l[LEN][1], '\t', l[LEN][2], '\t', l[LEN][3])
                            LEN += 1
                        print("GST@12%: ", gst)
                        total_price = total + gst
                        print('Total Price:', total_price)
                        LEN = len(l)
                        e = 0
                        for f in range(LEN):
                            e1 = len(df1)
                            df1.loc[e1] = l[e]
                            e+=1
                        l2 = [[cust_name, phone_no, invoice_no]]
                        E=0
                        for g in range(1):
                            e2 = len(df2)
                            df2.loc[e2] = l2[E]
                        df1.to_csv("D:/chahak_project/product_sold.csv", index=False)
                        df2.to_csv("D:/chahak_project/customer_detail.csv", index=False)
                        ch = input("Are there more customers (yes or no): ")
                        if ch == 'Yes' or ch == 'yes' or ch == 'YES':
                            invoice_no += 1
                            continue
                        else:
                            break
               
                elif n2 == 2:
                   # DISPLAYING THE DETAILS OF THE PRODUCTS SOLD
                  df_product_sold = pd.read_csv("D:/chahak_project/product_sold.csv", index_col='PRODUCT CODE')
                  df_customer_detail = pd.read_csv("D:/chahak_project/customer_detail.csv")
                  print("Details of the product sold:")
                  print(df_product_sold)
                  print("Details of the customers:")
                  print(df_customer_detail)
               
                elif n2==3:
                   # SALES ANALYSIS
                   df_product_sold = pd.read_csv("D:/chahak_project/product_sold.csv")
                   plt.bar(df_product_sold["PRODUCT CODE"], df_product_sold["PRICE"])

                   plt.xlabel("Product Codes")
                   plt.title("SALES ANALYSIS")
                   plt.show()
                   
                else:
                    break
        else:
                print("incorrect password")
               
               
    elif n==4:
            #STOCK
            z="STOCK_789"
            s=input("enter the password:")
            if s==z:
                while True:
                    print("menu for retrieving data regarding stock:")
                    print("1-quantity available for each product")
                    print("2-edit stock list")
                    print("3-stock analysis")
                    n3=int(input("enter your choice:"))
                    D=pd.read_csv("D:\\chahak_project\\quantity_list.csv",index_col="PRODUCT CODE")
                    l=len(D)
                    if n3==1:
                        #DISPLAYING THE STOCK LIST
                        print("the dataframe for the quantity available is:")
                        print(D)
                    elif n3==2:
                        #EDITING THE STOCK LIST
                        print("menu for editing stock list:")
                        print("1=add any new product")
                        print("2-to remove any product")
                        print("3-to update a particular stock")
                        print("4-update stock after sales")
                        print("5-exit")
                       
                        choice=int(input("enter your choice from the edit menu:"))
                        if choice==1:
                            k=int(input("enter number of record:"))
                            for z in range(k):
                                pc=int(input("enter product code:"))
                                gen=input("enter gender in upper case:")
                                br=input("enter brand in upper case:")
                                ct=input("enter clothes type in upper case:")
                                qty=int(input("enter the quantity:"))
                                new_roll2=[pc,gen,br,ct,qty]
                                with open("D:\\chahak_project\\quantity_list.csv", mode='a', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow(new_roll2)
                                print("product successfully updated")
                        elif choice==2:
                            df1=pd.read_csv("D:\\chahak_project\\quantity_list.csv")
                            product_code_to_delete = int(input("Enter the product code to delete: "))
                            if product_code_to_delete in df1['PRODUCT CODE'].values:
                                # Delete the row(s) with the specified product code
                                df1 = df1[df1['PRODUCT CODE'] != product_code_to_delete]
                                df1.to_csv("D:\\chahak_project\\quantity_list.csv", index=False)
                                print("Product with code", product_code_to_delete," deleted successfully.")
                            else:
                                print("Product with code", product_code_to_delete," was not found.")
                        elif choice==3:
                            product_code_to_modify = int(input("Enter the product code to modify: "))
                            df=pd.read_csv("D:\\chahak_project\\quantity_list.csv")
                            if product_code_to_modify in df['PRODUCT CODE'].values:
                                 new_qty = int(input("Enter the new quantity: "))
                                 # Modify the quantity in the DataFrame
                                 df.loc[df['PRODUCT CODE'] == product_code_to_modify, 'QUANTITY AVAILABLE'] = new_qty
                                 df.to_csv("D:\\chahak_project\\quantity_list.csv", index=False)
                                 print("Price for product with code",product_code_to_modify,"modified successfully.")
                        elif choice==4:
                            DF2=pd.read_csv("D:/chahak_project/product_sold.csv")
                            D2=pd.read_csv("D:\\chahak_project\\quantity_list.csv")
                            for e4 in DF2.loc[:,"PRODUCT CODE"]:
                                    for e5 in D2.loc[:,"PRODUCT CODE"]:
                                        if e4==e5:
                                            DF3=pd.read_csv("D:/chahak_project/product_sold.csv",index_col="PRODUCT CODE")
                                            D3=pd.read_csv("D:\\chahak_project\\quantity_list.csv",index_col="PRODUCT CODE")
                                            sold=DF3.loc[e4,"PRODUCT QUANTITY"]
                                            qnty=D3.loc[e5,"QUANTITY AVAILABLE"]
                                            D3.loc[e5,"QUANTITY AVAILABLE"]=(qnty-sold)
                                            D3.to_csv("D:\\chahak_project\\quantity_list.csv")
                            print("modified quantity")
                                   
 
                        else :
                            break
                    elif n3==3:
                        # STOCK ANALYSIS
                        df_product_stock = pd.read_csv("quantity_list.csv")
                        plt.bar(df_product_stock["PRODUCT CODE"], df_product_stock["QUANTITY AVAILABLE"])
                        plt.xlabel("Product Codes")
                        plt.title("STOCK ANALYSIS")
                        plt.show()
                    else:
                        break
            else:
                print("incorrect password")
    else:
            break
