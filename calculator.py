from tkinter import *

is_calculation_completed = False


def write(value):
    global is_calculation_completed
    value_entered = input.get()
    number = len(value_entered)

    print("internal Values:", value_entered)

    if number == 0 and value == '.':
        value = '0.'

    if '.' == value and '.' in value_entered:
        return

    if is_calculation_completed:
        input.delete(0, 'end')
        is_calculation_completed = False
    input.insert(number, str(value))


def account_transactions(value):
    global calculate
    calculate = value
    global first_number
    first_number = float(input.get())
    print(first_number)
    input.delete(0, 'end')


def delete_all_values():
    global first_number
    global second_number
    print('All Values â€‹â€‹Deleted')
    first_number = 0
    second_number = 0
    input.delete(0, 'end')


def delete_values():
    input.delete(0, 'end')


def calculation_process():
    global first_number
    global second_number
    global is_calculation_completed
    second_number = float(input.get())
    print(second_number)
    global calculate

    result = 0
    if calculate == 0:
        result = first_number + second_number
    elif calculate == 1:
        result = first_number - second_number
    elif calculate == 2:
        result = first_number * second_number
    elif calculate == 3:
        result = first_number / second_number
    elif calculate == 4:
        result = "0"

    is_calculation_completed = True

    first_number = result
    input.delete(0, 'end')
    input.insert(0, str(result))


def delete_all():
    input.delete(0, 'end')


pencere = Tk()
pencere.geometry('250x300')
input = Entry(font="Verdana 14 bold", width=15, justify=RIGHT)
input.place(x=20, y=20)

button = []

for i in range(1, 10):
    button.append(Button(text=str(i), font="Verdana 14 bold", command=lambda value=i: write(value)))

counter = 0

for i in range(0, 3):
    for j in range(0, 3):
        button[counter].place(x=20 + j * 50, y=50 + i * 50)
        counter += 1

process = []

for i in range(0, 4):
    process.append(Button(font="Verdana 14 bold", width=2, command=lambda value=i: account_transactions(value)))

process[0]['text'] = "+"
process[1]['text'] = "-"
process[2]['text'] = "*"
process[3]['text'] = "/"

for i in range(0, 4):
    process[i].place(x=170, y=50 + 50 * i)

zero_button = Button(text=0, font="Verdana 14 bold", command=lambda value=0: write(value))
zero_button.place(x=20, y=200)

dot_button = Button(text=".", font="Verdana 14 bold", width=2, command=lambda value=".": write(value))
dot_button.place(x=70, y=200)

equal_button = Button(text="=", fg="GREEN", font="Verdana 14 bold", width=2, command=calculation_process)
equal_button.place(x=120, y=200)

delete_button = Button(text="C", fg="RED", font="Verdana 14 bold", width=6, command=delete_values)
delete_button.place(x=20, y=250)

delete_all_button = Button(text="CE", fg="RED", font="Verdana 14 bold", width=6, command=delete_all_values)
delete_all_button.place(x=120, y=250)

pencere.mainloop()
