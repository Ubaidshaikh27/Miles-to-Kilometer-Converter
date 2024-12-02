from tkinter import *
#
#
#
#
# def button_clicked():
#     my_label.config(text=inputs.get() )
#
# def button_two():
#     my_label.config(text=inputs.get() )
#
#
# window = Tk()
# window.title("My First GUI")
# window.minsize(width=500, height=300)
#
# ## Label
#
# my_label = Label(text="I am a Label", font=("Arial", 20,"normal "))
# my_label["text"] = "New  a Text"
# my_label.config(text="New Text")
# my_label.grid(column=0, row=0)
#
# ##Button
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
# button2 = Button(text="New Button", command=button_two)
# button2.grid(column=2, row=0)
#
# ##Entry
# inputs = Entry()
# print(inputs.get())
# inputs.grid(column=3, row=2)


#####MILES TO KILOMETER CONVERTER


def calculate():
    output = float(entry.get()) * 1.609

    miles.config(text=output)



window = Tk()
window.title("Miles to Km Converter")
window.config(padx=30, pady=30)



###label

my_label = Label(text=" is equal to", font=("Arial", 20,"normal "))
my_label.grid(column=2, row=4)
# my_label.config(padx=50, pady=30)

my_label2 = Label(text=" Miles", font=("Arial", 20,"normal "))
my_label2.grid(column=5, row=2)



my_label3 = Label(text=" Km", font=("Arial", 20,"normal "))
my_label3.grid(column=5, row=4)

miles = Label(text=" 0", font=("Arial", 20,"normal "))
miles.grid(column=3, row=4)




###button
button = Button(text="Calculate", command=calculate)
button.grid(column=3, row=9)
button.config(padx=10, pady=5)



###Entry

entry = Entry()
entry.get()
entry.grid(column=3, row=2)


















window.mainloop()