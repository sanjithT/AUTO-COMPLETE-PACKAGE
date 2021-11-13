from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(filetypes=[("Text Files",
                                           "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Text Editor Application - {filepath}")


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")


def get():
    cursor_position = txt_edit.index(INSERT)
    k = txt_edit.get(float(int(float(cursor_position))), END)
    l = k.split()[-1]
    txt_edit.selection(float(int(float(cursor_position))), END)


window = Tk()
window.title("Text Editor Application")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

txt_edit = Text(window)

fr_buttons = Frame(window, relief=RAISED, bd=2)
fr_suggest = Frame(window, relief=SUNKEN, bd=5, height=50, width=500)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)
btn_get = Button(fr_buttons, text="Get", command=get)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_get.grid(row=2, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
fr_suggest.grid(row=1, column=1, columnspan=1)

window.mainloop()