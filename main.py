from tkinter import Tk, Label, Button

def on_button_click():
    label.config(text="Button clicked!")

# Create the main window
window = Tk()

# Create a label
label = Label(window, text="Hello, World!")
label.pack()

# Create a button
button = Button(window, text="Click me", command=on_button_click)
button.pack()

# Start the main event loop
window.mainloop()
