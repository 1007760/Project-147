from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Ascii Convertion")
root.configure(background = 'snow')
enter_word = Entry(root)
enter_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label = Label(root, text = "Student's name in ascii : ", bg = "light blue", fg = "black")
label2 = Label(root, text = "The encrypted name : ", bg = "light blue", fg = "black")

def Convertion() :
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2["text"] += str(chr(encrypted))
        
btn = Button(root, text = "Show the name in ascii and the encryption", command = Convertion, bg = 'blue', fg = 'black')
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label2.place(relx = 0.5, rely = 0.7, anchor = CENTER)
root.mainloop()