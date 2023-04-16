import tkinter as tk;

calulation = ''

def AddToCalculation(symbol):
    global calulation
    calulation += str(symbol)
    text_result.delete(1.0,'end')
    text_result.insert('end',calulation)
    

def EvaluteCalculation():
    global calulation
    try:
        calulation = eval(calulation)
        text_result.delete(1.0,'end')
        text_result.insert(1.0,calulation)
    except:
        ClearField()
        text_result.insert(1.0,"Error")
        pass

def ClearField():
    global calulation
    calulation = ""
    text_result.delete(1.0,"end")
    


root = tk.Tk()
root.geometry("300x275")
text_result = tk.Text(root, height=2, width=15,font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 = tk.Button(root,text=1,width=5, command=lambda: AddToCalculation(1))
btn_1.grid(row=2,column=1)

btn_2 = tk.Button(root,text=2,width=5, command=lambda: AddToCalculation(2))
btn_2.grid(row=2,column=2)

btn_3 = tk.Button(root,text=3,width=5, command=lambda: AddToCalculation(3))
btn_3.grid(row=2,column=3)

btn_4 = tk.Button(root,text=4,width=5, command=lambda: AddToCalculation(4))
btn_4.grid(row=3,column=1)

btn_5 = tk.Button(root,text=5,width=5, command=lambda: AddToCalculation(5))
btn_5.grid(row=3,column=2)

btn_6 = tk.Button(root,text=6,width=5, command=lambda: AddToCalculation(6))
btn_6.grid(row=3,column=3)

btn_7 = tk.Button(root,text=7,width=5, command=lambda: AddToCalculation(7))
btn_7.grid(row=4,column=1)

btn_8 = tk.Button(root,text=8,width=5, command=lambda: AddToCalculation(8))
btn_8.grid(row=4,column=2)

btn_9 = tk.Button(root,text=9,width=5, command=lambda: AddToCalculation(9))
btn_9.grid(row=4,column=3)

btn_0 = tk.Button(root,text=0,width=5, command=lambda: AddToCalculation(0))
btn_0.grid(row=5,column=1)

btn_dot = tk.Button(root,text='.', width=5,command=lambda: AddToCalculation('.'))
btn_dot.grid(row=5,column=2)

btn_equal = tk.Button(root,text='=',width=5, command=EvaluteCalculation)
btn_equal.grid(row=5,column=3)

btn_clear = tk.Button(root,text='C',width=5,command= ClearField)
btn_clear.grid(row=2,column=4)

btn_div = tk.Button(root,text='/',width=5, command=lambda: AddToCalculation('/'))
btn_div.grid(row=3,column=4)

btn_plus = tk.Button(root,text='+',width=5, command=lambda: AddToCalculation('+'))
btn_plus.grid(row=4,column=4)

btn_subtract = tk.Button(root,text='-',width=5, command=lambda: AddToCalculation('-'))
btn_subtract.grid(row=5,column=4)

btn_multy = tk.Button(root,text='*',width=5, command=lambda: AddToCalculation('*'))
btn_multy.grid(row=6,column=4)

btn_r_bracket = tk.Button(root,text='(',width=5,command=lambda:AddToCalculation('('))
btn_r_bracket.grid(row=6,column=1)

btn_l_bracket = tk.Button(root,text=')',width=5,command=lambda:AddToCalculation(')'))
btn_l_bracket.grid(row=6,column=2)

root.mainloop()