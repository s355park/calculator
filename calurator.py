from tkinter import *

# simple calculation methods.
def calculation(left_operland, right_operland, operator):
    if operator=='+':
        return float(left_operland)+float(right_operland)
    elif operator=='-':
        return float(left_operland)-float(right_operland)
    elif operator=='X':
        return float(left_operland)*float(right_operland)
    elif operator=='/':
        return float(left_operland)/float(right_operland)

root=Tk()

# main entry taking input and outputting results
main_entry= Entry(root, width=70, bg="white", fg="black")
main_entry.grid(row=0, column=0, columnspan=4)

input_operators_list=[]
input_numbers_list=[]
input_total_list=[]

# brief : when number is received, output to the main_entry
# params
# the_inputted_num : the number from 0-9 that user wanted to add to the main_entry
# return : nothing
def input_num(the_inputted_num):
    temp='+-X/'
    if  ((len(input_numbers_list)!=0) and (temp.find(input_total_list[-1])!=-1)):
        main_entry.delete(0, END)
        main_entry.insert(0, the_inputted_num)
    else:
        current=main_entry.get()
        main_entry.delete(0, END)
        current=current+the_inputted_num
        main_entry.insert(0, current)
    input_total_list.append(the_inputted_num)

# brief : when symbol is received, save them in list in reverse polish notation.
# params
# the_operator : the operator that user wanted to add to the main_entry
# return : nothing
def input_operator(the_operator):
    input_numbers_list.append(main_entry.get())
    priority={'+':1, '-':1, 'X':0, '/':0}
    input_total_list.append(the_operator)
    if len(input_operators_list) == 0:
        input_operators_list.append(the_operator)
        return
    else:
        if priority[input_operators_list[-1]] <= priority[the_operator]:
            num2=input_numbers_list.pop()
            num1=input_numbers_list.pop()
            input_numbers_list.append(calculation(num1, num2, input_operators_list.pop()))
            input_operators_list.append(the_operator)
            main_entry.delete(0, END)
            main_entry.insert(0, input_numbers_list[-1])
        else:
            input_operators_list.append(the_operator)
            main_entry.delete(0, END)
            main_entry.insert(0, input_numbers_list[-1])

# brief : when equal is inputted, calculate those that are remaining in stack and output it to main_entry
# params : nothing
# return : nothing
def input_equal():
    input_numbers_list.append(main_entry.get())
    while(len(input_operators_list)!=0):
        num2=input_numbers_list.pop()
        num1=input_numbers_list.pop()
        input_numbers_list.append(calculation(num1, num2, input_operators_list.pop()))
    main_entry.delete(0, END)
    main_entry.insert(0, input_numbers_list[0])

# create buttons.
button1=Button(root, text="1", padx=40, pady=25,command=lambda: input_num("1"))
button2=Button(root, text="2", padx=40, pady=25,command=lambda: input_num("2"))
button3=Button(root, text="3", padx=40, pady=25,command=lambda: input_num("3"))
button4=Button(root, text="4", padx=40, pady=25,command=lambda: input_num("4"))
button5=Button(root, text="5", padx=40, pady=25,command=lambda: input_num("5"))
button6=Button(root, text="6", padx=40, pady=25,command=lambda: input_num("6"))
button7=Button(root, text="7", padx=40, pady=25,command=lambda: input_num("7"))
button8=Button(root, text="8", padx=40, pady=25,command=lambda: input_num("8"))
button9=Button(root, text="9", padx=40, pady=25,command=lambda: input_num("9"))

button_equal=Button(root, text="=", padx=40, pady=25, command=input_equal)
button_add=Button(root, text="+", padx=40, pady=25,command=lambda: input_operator('+'))
button_subtract=Button(root, text="-", padx=40, pady=25,command=lambda: input_operator('-'))
button_multiplication=Button(root, text="X",padx=40, pady=25, command=lambda: input_operator('X'))
button_division=Button(root, text="/",padx=40, pady=25, command=lambda: input_operator('/'))

#d ecides where they are located on grid.
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiplication.grid(row=3, column=3)
button_division.grid(row=4, column=3)
button_equal.grid(row=4,column=0)

root.mainloop()