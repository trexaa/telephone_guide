import os 
import sys 
telephone_guide ={
    
}

menu = """
Choose
1) Search in telephone guide
2) add in telephone guide
3) show the all the telephone guide
4) to exti the program
"""

def st():
    def se():
        try:
            num = int(input("enter the number : "))
            print([telephone_guide[num]])
            var = input("do you want to serch again? ")
            if var.lower()=='no':
                os.execl(sys.executable, sys.executable, *sys.argv)
            if var.lower()=='yes':
                st()
        except KeyError:
            print("Sorry, the number is not found")
        except ValueError:
            print("This is invalid number")

    def add():
        try:
            name = input("enter the name")
            number = int(input("enter the numder "))
            telephone_guide[name]=number
            var = input("do you want to run again? ")
            if var.lower()=='no':
                os.execl(sys.executable, sys.executable, *sys.argv)
            if var.lower()=='yes':
                st()
        except KeyError:
            print("Sorry, the number is not found")
        except ValueError:
            print("This is invalid number")

    def show():
        print(telephone_guide)
        var = input("do you want to run again? ")
        if var.lower()=='no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower()=='yes':
            st()

    def exit():
        print("good bye")
        os.execl(sys.executable, sys.executable, *sys.argv)

    ans = input(menu)
    if ans == '1':
        se()
    if ans=='2':
        add()
    if ans=='3':
        show()
    if ans=='4':
        exit()
st()
