from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root. title("Restraunt Management System")

text_input = StringVar()
operator = ""


rand_ = StringVar()
fries = StringVar()
burger = StringVar()
filet = StringVar()
subTotal = StringVar()
Total = StringVar()
serviceCharge = StringVar()
drinks = StringVar()
tax = StringVar()
cost = StringVar()
chickenBurger = StringVar()
cheeseBurger = StringVar()

tops = Frame(root, width=1600, height=50, relief=SUNKEN)
tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=800, height=700, bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)

# =========================Time=================================
localtime = time.asctime(time.localtime(time.time()))

# ===========================Info===============================
linfo = Label(tops, font="arial 50 bold",
              text="Restaurant Management System", fg="steel blue", bd=10, anchor=W)
linfo.grid(row=0, column=0)
linfo = Label(tops, font="arial 20 bold",
              text=localtime, fg="steel blue", bd=10, anchor=W)
linfo.grid(row=1, column=0)

# =====================================Calculator===============================


def btnClick(numbers):
    global operator
    operator = operator+str(numbers)
    text_input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_input.set("")


def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


def ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand_.set(randomRef)
    print(randomRef)

    coF = float(fries.get())
    coD = float(drinks.get())
    coFilet = float(filet.get())
    coBurger = float(burger.get())
    coChickenBurger = float(chickenBurger.get())
    coCheeseBurger = float(cheeseBurger.get())

    costofFries = coF*0.99
    costofDrinks = coD*1.00
    costofFilet = coFilet*2.99
    costofBurger = coBurger*2.87
    costChicken = coChickenBurger*2.89
    costCheeseBurger = coCheeseBurger*2.69

    costofMeal = 'Rs.', str("%.2f" % (
        costofFries+costofDrinks+costofFilet+costofBurger+costChicken+costCheeseBurger
    ))

    payTax = ((
        costofFries+costofDrinks+costofFilet+costofBurger+costChicken+costCheeseBurger
    ))*0.2

    totalCost = costofFries+costofDrinks+costofFilet+costofBurger+costChicken+costCheeseBurger

    serCharge = (costofFries+costofDrinks+costofFilet +
                 costofBurger+costChicken+costCheeseBurger)/99

    service = 'Rs.', str("%.2f" % serCharge)
    overAllCost = 'Rs.', str("%.2f" % (payTax+totalCost+serCharge))
    # paidTax = 'Rs.', str("%2f" % payTax)

    serviceCharge.set(service)
    cost.set(costofMeal)
    tax.set(costofMeal)
    subTotal.set(costofMeal)
    Total.set(overAllCost)


def exit_():
    root.destroy()


def reset():
    rand_.set("")
    fries.set("")
    burger.set("")
    filet.set("")
    subTotal.set("")
    Total.set("")
    serviceCharge.set("")
    drinks.set("")
    tax.set("")
    cost.set("")
    chickenBurger.set("")
    cheeseBurger.set("")


txtDisplay = Entry(f2, font="arial 20 bold", textvariable=text_input,
                   bd=30, insertwidth=4, bg="powder blue", justify="right")
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
              text="7", bg="powder blue", command=lambda: btnClick(7))
btn7.grid(row=2, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
              text="8", bg="powder blue", command=lambda: btnClick(8))
btn8.grid(row=2, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
              text="9", bg="powder blue", command=lambda: btnClick(9))
btn9.grid(row=2, column=2)
addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
                  text="+", bg="powder blue", command=lambda: btnClick("+"))
addition.grid(row=2, column=3)

# -------------------------------------------------------------------------------
btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
              text="4", bg="powder blue", command=lambda: btnClick(4))
btn4.grid(row=3, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
              text="5", bg="powder blue", command=lambda: btnClick(5))
btn5.grid(row=3, column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
              text="6", bg="powder blue", command=lambda: btnClick(6))
btn6.grid(row=3, column=2)
subtraction = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
                     text="-", bg="powder blue", command=lambda: btnClick("-"))
subtraction.grid(row=3, column=3)

# --------------------------------------------------------------------------------
btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
              text="1", bg="powder blue", command=lambda: btnClick(1))
btn1.grid(row=4, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
              text="2", bg="powder blue", command=lambda: btnClick(2))
btn2.grid(row=4, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
              text="3", bg="powder blue", command=lambda: btnClick(3))
btn3.grid(row=4, column=2)
multiply = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
                  text="*", bg="powder blue", command=lambda: btnClick("*"))
multiply.grid(row=4, column=3)

# ------------------------------------------------------------------------------
btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
              text="0", bg="powder blue", command=lambda: btnClick(0))
btn0.grid(row=5, column=0)
clear = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
               text="C", bg="powder blue", command=btnClear)
clear.grid(row=5, column=1)
equal = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
               text="=", bg="powder blue", command=btnEquals)
equal.grid(row=5, column=2)
divide = Button(f2, padx=16, pady=16, bd=8, fg="black", font="arial 20 bold",
                text="/", bg="powder blue", command=lambda: btnClick("/"))
divide.grid(row=5, column=3)

# --------------------------------Restaurant Info 1---------------------------------------------------------


lReference = Label(f1, font="arial 16 bold",
                   text="Reference", bd=16, anchor=W)
lReference.grid(row=0, column=0, sticky=W)
txtReference = Entry(f1, font="arial 16 bold", textvariable=rand_,
                     bd=10, insertwidth=4, bg="powder blue", justify=RIGHT)
txtReference.grid(row=0, column=1)

lFries = Label(f1, font="arial 16 bold", text="Large Fries",
               bd=16, anchor=W)
lFries.grid(row=1, column=0, sticky=W)
txtFries = Entry(f1, font="arial 16 bold", textvariable=fries,
                 bd=10, insertwidth=4, bg="powder blue", justify=RIGHT)
txtFries.grid(row=1, column=1)

lBurger = Label(f1, font="arial 16 bold", text="Burger Meals",
                bd=16, anchor=W)
lBurger.grid(row=2, column=0, sticky=W)
txtBurger = Entry(f1, font="arial 16 bold", textvariable=burger,
                  bd=10, insertwidth=4, bg="powder blue", justify=RIGHT)
txtBurger.grid(row=2, column=1)

lfilet = Label(f1, font="arial 16 bold", text="Filet Meal",
               bd=16, anchor=W)
lfilet.grid(row=3, column=0, sticky=W)
txtfilet = Entry(f1, font="arial 16 bold", textvariable=filet,
                 bd=10, insertwidth=4, bg="powder blue", justify=RIGHT)
txtfilet.grid(row=3, column=1)

lchickenMeal = Label(f1, font="arial 16 bold",
                     text="Chicken Burger", bd=16, anchor=W)
lchickenMeal.grid(row=4, column=0, sticky=W)
txtchickenMeal = Entry(f1, font="arial 16 bold", textvariable=chickenBurger,
                       bd=10, insertwidth=4, bg="powder blue", justify=RIGHT)
txtchickenMeal.grid(row=4, column=1)

lcheeseBurger = Label(f1, font="arial 16 bold",
                      text="Cheese Burger", bd=16, anchor=W)
lcheeseBurger.grid(row=5, column=0, sticky=W)
txtcheeseBurger = Entry(f1, font="arial 16 bold", textvariable=cheeseBurger,
                        bd=10, insertwidth=4, bg="powder blue", justify=RIGHT)
txtcheeseBurger.grid(row=5, column=1)

# --------------------------------Restaurant Info 1-------------------------------------------
lDrinks = Label(f1, font="arial 16 bold",
                text="Drinks", bd=16, anchor=W)
lDrinks.grid(row=0, column=2, sticky=W)
txtDrinks = Entry(f1, font="arial 16 bold", textvariable=drinks,
                  bd=10, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtDrinks.grid(row=0, column=3)

lCost = Label(f1, font="arial 16 bold", text="Cost of Meal",
              bd=16, anchor=W)
lCost.grid(row=1, column=2, sticky=W)
txtCost = Entry(f1, font="arial 16 bold", textvariable=cost,
                bd=10, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtCost.grid(row=1, column=3)

lserviceCharge = Label(f1, font="arial 16 bold", text="Service Charge",
                       bd=16, anchor=W)
lserviceCharge.grid(row=2, column=2, sticky=W)
txtserviceCharge = Entry(f1, font="arial 16 bold", textvariable=serviceCharge,
                         bd=10, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtserviceCharge.grid(row=2, column=3)

lstateTax = Label(f1, font="arial 16 bold", text="State Tax",
                  bd=16, anchor=W)
lstateTax.grid(row=3, column=2, sticky=W)
txtstateTax = Entry(f1, font="arial 16 bold", textvariable=tax,
                    bd=10, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtstateTax.grid(row=3, column=3)

lsubTotal = Label(f1, font="arial 16 bold",
                  text="Sub Total", bd=16, anchor=W)
lsubTotal.grid(row=4, column=2, sticky=W)
txtsubTotal = Entry(f1, font="arial 16 bold", textvariable=subTotal,
                    bd=10, insertwidth=4, bg="#ffffff", justify=RIGHT)
txtsubTotal.grid(row=4, column=3)

ltotalCost = Label(f1, font="arial 16 bold",
                   text="Total Cost", bd=16, anchor=W)
ltotalCost.grid(row=5, column=2, sticky=W)
txttotalCost = Entry(f1, font="arial 16 bold", textvariable=Total,
                     bd=10, insertwidth=4, bg="#ffffff", justify=RIGHT)
txttotalCost.grid(row=5, column=3)

# ------------------------------Buttons------------------------------------
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font="arial 16 bold",
                  width=10, text="Total", bg="powder blue", command=ref)
btnTotal.grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font="arial 16 bold",
                  width=10, text="Reset", bg="powder blue", command=reset)
btnReset.grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font="arial 16 bold",
                 width=10, text="Exit", bg="powder blue", command=exit_)
btnExit.grid(row=7, column=3)


root.mainloop()
