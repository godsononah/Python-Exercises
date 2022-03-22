from tkinter import *
from quitter import Quitter

def fetch():
    numlist = (ent.get()).split(', ')
    result = 0
    for num in numlist:
        result += int(num)
    print('Result => {}'.format(result))                  # get text
    show = Toplevel(root)
    show.title('Result')
    msg = Message(show, text=('The sum of {} is {}'.format(ent.get(), result)))
    msg.config(bg='pink', font=('times', 20, 'italic'))
    msg.pack(expand=YES, fill=BOTH)

root = Tk()
ent = Entry(root)
ent.insert(0, 'Type numbers here')                            # set text
ent.pack(side=TOP, fill=X)                                  # grow horizontal

ent.focus()                                                 # save a click
ent.bind('<Return>', (lambda event: fetch()))               # on enter key
btn = Button(root, text='Fetch', command=fetch)             # and on button
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()