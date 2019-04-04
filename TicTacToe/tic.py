from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Tic Tac Toe')

click = True

labelText = "Let's play!"

def checker(buttons):
    global click
    if buttons['text'] == ' ' and click == True:
        buttons['text'] = 'X'
        click = False
    elif buttons['text'] == ' ' and click == False:
        buttons['text'] = 'O'
        click = True
    elif (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
          button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
          button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
          button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
          button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
          button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
          button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
          button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        messagebox.showinfo('Results', 'Player X wins')
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
        messagebox.showinfo('Results', 'Player O wins')


buttons = StringVar()


global button1, button2, button3, button4, button5, button6, button7, button8, button9, label

label = Label(window, text=labelText)
label.grid({'row': '0', 'sticky': 'NSEW', 'in': window})

button1 = Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button1)})
button1.grid({'row': '1', 'column': '0', 'sticky': 'NSEW', 'in': window})


button2 = Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button2)})
button2.grid({'row': '1', 'column': '1', 'sticky': 'NSEW', 'in': window})


button3 = Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button3)})
button3.grid({'row': '1', 'column': '2', 'sticky': 'NSEW', 'in': window})


button4 = Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button4)})
button4.grid({'row': '2', 'column': '0', 'sticky': 'NSEW', 'in': window})


button5 = Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button5)})
button5.grid({'row': '2', 'column': '1', 'sticky': 'NSEW', 'in': window})


button6 = Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button6)})
button6.grid({'row': '2', 'column': '2', 'sticky': 'NSEW', 'in': window})


button7 = Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button7)})
button7.grid({'row': '3', 'column': '0', 'sticky': 'NSEW', 'in': window})


button8 = Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button8)})
button8.grid({'row': '3', 'column': '1', 'sticky': 'NSEW', 'in': window})


button9 = Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(button9)})
button9.grid({'row': '3', 'column': '2', 'sticky': 'NSEW', 'in': window})


window.mainloop()