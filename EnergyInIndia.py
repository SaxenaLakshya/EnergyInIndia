import matplotlib.pyplot as plt
import pandas as pd

path = "C://Users//Lakshya Saxena//Downloads//EnergyInIndia.csv" # Please enter the file location from your PC
df = pd.read_csv(path)


def line_graphs():
    print("********Energy Data Graphs********")
    print("1. Graph of Oil consumption in India")
    print("2. Graph of Coal consumption in India")
    print("3. Graph of Solar Energy consumption in India")
    print("4. Graph of Nuclear Energy consumption in India")
    print("5. Graph of BioFuel consumption in India")
    print("6. Graph of Gas Consumption in India")

    n = int(input("Enter the graph number: "))

    if n == 1:
        df.plot(x='Year', y='Oil Consumption - EJ', color='brown')
        plt.grid()
        plt.show()

    elif n == 2:
        df.plot(x='Year', y='Coal Consumption - EJ', color='black')
        plt.grid()
        plt.show()

    elif n == 3:
        df.plot(x='Year', y='Solar Consumption - EJ', color='orange')
        plt.grid()
        plt.show()

    elif n == 4:
        df.plot(x='Year', y='Nuclear Consumption - EJ', color='cyan')
        plt.grid()
        plt.show()

    elif n == 5:
        df.plot(x='Year', y='Biofuels (TWh)', color='green')
        plt.grid()
        plt.show()

    elif n == 6:
        df.plot(x='Year', y='Gas Consumption - EJ', color='purple')
        plt.grid()
        plt.show()

    else:
        print("Invalid Input!")

def bar_graph():
    print("********Energy Data Graphs********")
    print("1. Graph of Oil consumption in India")
    print("2. Graph of Coal consumption in India")
    print("3. Graph of Solar Energy consumption in India")
    print("4. Graph of Nuclear Energy consumption in India")
    print("5. Graph of BioFuel consumption in India")
    print("6. Graph of Gas Consumption in India")

    n = int(input("Enter the graph number: "))

    if n == 1:
        df.plot.bar(x='Year', y='Oil Consumption - EJ', color='brown')
        plt.grid()
        plt.show()

    elif n == 2:
        df.plot.bar(x='Year', y='Coal Consumption - EJ', color='black')
        plt.grid()
        plt.show()

    elif n == 3:
        df.plot.bar(x='Year', y='Solar Consumption - EJ', color='orange')
        plt.grid()
        plt.show()

    elif n == 4:
        df.plot.bar(x='Year', y='Nuclear Consumption - EJ', color='cyan')
        plt.grid()
        plt.show()

    elif n == 5:
        df.plot.bar(x='Year', y='Biofuels (TWh)', color='green')
        plt.grid()
        plt.show()

    elif n == 6:
        df.plot.bar(x='Year', y='Gas Consumption - EJ', color='purple')
        plt.grid()
        plt.show()

    else:
        print("Invalid Input!")

def readcsv():
    print("Reading Data from CSV")
    print(df)


def no_index():
    print("Reading data from CSV without index")
    df1 = pd.read_csv(path, index_col=0)
    print(df1)


def new_column():
    c = len(df['Year'])
    col = []
    for i in range(c):
        a = input("Enter value: ")
        i = i + 1
        col.append(a)
    a = input("Enter the name of new column: ")
    df[a] = col
    print(df)


def new_row():
    neweg = []
    print("Adding new energy information")
    neweg1 = input("Enter the information of New Energy: ")
    for i in range(len(df.columns) - 1):
        neweg.append(neweg1)
        value = input("Enter the information of column: ")
        neweg.append(value)
        i = i + 1
        df.append(neweg)
    print(df)


def data_sorting():
    print("Press 1 to arrange the record as per the Oil Consumption")
    print("Press 2 to arrange the record as per the Gas Consumption")
    print("Press 3 to arrange the record as per the Coal Consumption")
    print("Press 4 to arrange the record as per the Hydro Consumption")
    print("Press 5 to arrange the record as per the Nuclear Consumption")

    op6 = int(input("Enter Your Choice: "))
    if op6 == 1:
        df.sort_values(by=['Oil Consumption - EJ'], inplace=True)
        print(df)
    elif op6 == 2:
        df.sort_values(by=['Gas Consumption - EJ'], axis=0, inplace=True)
        print(df)
    elif op6 == 3:
        df.sort_values(by=['Coal Consumption - EJ'], inplace=True)
        print(df)
    elif op6 == 4:
        df.sort_values(by=['Hydro Consumption - EJ'], inplace=True)
        print(df)
    elif op6 == 5:
        df.sort_values(by=['Nuclear Consumption - EJ'], inplace=True)
        print(df)
    else:
        print("Invalid Input")


def top_bottom_selected_records():
    top = int(input("How many records to display from top:"))
    print("First", top, "records")
    print(df.head(top))
    bottom = int(input("how many records to display from bottom:"))
    print("Last", bottom, "records")
    print(df.tail(bottom))


def duplicate():
    print("Duplicate the file with new file")
    df = pd.read_csv(path)
    df.to_csv(path)
    print("Data from the new file")
    print(df)


def new_column_name():
    print("Adding new column name to existing data")
    df = pd.read_csv(path, index_col=0, skiprows=1, names=['States'])
    print(df)


def general_trivia():
    print("1. Maximum Nuclear Energy Consumption ", df['Nuclear Consumption - EJ'].max())
    print("2. Minimum Nuclear Energy Consumption ", df['Nuclear Consumption - EJ'].min())
    print("3. Average Nuclear Energy Consumption ", df['Nuclear Consumption - EJ'].mean())
    print("4. Median Nuclear Energy Consumption ", df['Nuclear Consumption - EJ'].median())

def data_info():
    df.info()

def rename():
    df=pd.read_csv("C:\\Users\\Deepti\\Desktop\\covid1.csv")
    df= df.set_index('StateUT')
    print("Press 1 for Renaming of a Row")
    print("Press 2 for Renaming of a column")
    ch=int(input("enter your choice"))
    if ch==1:
       oldenergy=input("Enter the name of the Energy which you want to rename:")
       newenergy=input("Enter the name of the New Energy: ")
       df.rename({oldenergy:newenergy},inplace=True)
       print(df)
       df.to_csv(path)
    elif ch==2:
      oldcol=input("Enter the name of the column  which you want to rename: ")
      newcol=input("Enter the new name of the column of the existing column: ")
      df.rename(columns={oldcol:newcol},inplace=True)
      print(df)
      df.to_csv(path)

def delete():
    df = pd.read_csv(path)
    print("Press 1 To Delete a column")
    print("Press 2 To Delete a Row")
    ch = int(input("enter your choice"))
    if ch == 1:
        col = input("enter the name of the column which you want to delete")
        df.drop(col, axis=1, inplace=True)

    elif ch == 2:
        row = input("enter the name of the state whose information you want to delete")
        df.drop(row, axis=0, inplace=True)

    print("Deleted Successfully")
    df.to_csv(path)

def main_menu():
    print("***************Different Energies in India Data Analysis***************")
    print("Read Data from File in different Way")
    print("1. Read Complete CSV file")
    print("2. Reading Complete file without index")
    print("----------Data Manipulation----------")
    print("3. Insert a new column")
    print("4. Insert a new Row or New Year's information")
    print("5. Sort Data according to Energies")
    print("6. Duplicate the file with a New File")
    print("7. Sort Data from Top and Bottom")
    print("8. General Trivia of Nuclear Energy")
    print("9. Print the basic information about the data")
    print("10. Rename any Column")
    print("11. Delete any column")
    print("----------Graphs----------")
    print("12. Print the Line Graphs of Energies")
    print("13. Print the Bar Graphs of Energies")
    print("========================================================================")


while(True):
    main_menu()
    opt=int(input("Enter your Choice: "))
    if opt==1:
        readcsv()
    elif opt==2:
        no_index()
    elif opt==3:
        new_column()
    elif opt==4:
        new_row()
    elif opt==5:
        data_sorting()
    elif opt==6:
        duplicate()
    elif opt==7:
        top_bottom_selected_records()
    elif opt==8:
        general_trivia()
    elif opt==9:
        data_info()
    elif opt==10:
        rename()
    elif opt==11:
        delete()
    elif opt==12:
        line_graphs()
    elif opt==13:
        bar_graph()

    else:
        print("Wrong input!")
    msg = input("Do you want to select again? y/n: ")
    if msg == 'y':
        continue
    else:
        print("Thank You! Visit again!")
        break
