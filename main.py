import math
import tkinter.messagebox
from cmath import exp
from tkinter import *
from tkinter import Tk, Button

tk = Tk()

tk.title(" Probability of exact outages ")
tk.geometry("280x600")
winWidth = tk.winfo_reqwidth()
winwHeight = tk.winfo_reqheight()
posRight = int(tk.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(tk.winfo_screenheight() / 2 - winwHeight / 2)
tk.geometry("+{}+{}".format(posRight, posDown))

# background image
img = PhotoImage(file="power design.png")
img1 = img.subsample(2, 2)

Label(tk, image=img1).grid(row=0, column=1, columnspan=2, rowspan=2, pady=5, padx=5)

label_1 = Label(tk, text="Enter the value for time (t1)/hour: ")
label_2 = Label(tk, text="Enter the value for K: ")
label_1.grid(row=4, column=2, sticky=W, pady=2)
label_2.grid(row=7, column=2, sticky=W, pady=2)

# entry from user
time = Entry(tk)
k_constant = Entry(tk)

time.grid(row=5, column=2)
k_constant.grid(row=8, column=2)


def get_data():
    time_data = time.get()
    constant_data = k_constant.get()
    lambda_not = 0.0622
    percent = 100
    ebase = 2.718281828
    try:
        time1 = float(time_data)
        value = float(constant_data)
        k = math.factorial(value)
        denominator = exp(lambda_not * time1) * k
        numerator = (lambda_not * time1)

        probability_of_exactly = math.pow(k, numerator) / denominator

        percentage_probability = probability_of_exactly * percent

        Real_number_part = percentage_probability.real
        format_float = float("{:.3f}".format(Real_number_part))

        def condition():
            if format_float < 50:
                tkinter.messagebox.showerror(title='Error', message=f'Please Apply redundancy \n\n {format_float}%')
            elif format_float >= 50:
                tkinter.messagebox.showinfo(title='Result', message=f"The result: {format_float}%")

        condition()
    except ValueError:
        tkinter.messagebox.showerror(title='Error', message="Please enter an integer value")



calculate = Button(tk, command=get_data, text='Calculate', activebackground='red')
calculate.grid(row=10, column=2)



tk.mainloop()
