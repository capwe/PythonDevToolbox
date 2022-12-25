import tkinter as tk
import webbrowser

# Create the main window
window = tk.Tk()
window.title("Bookmark Collector")

# Define the action to take when the first button is clicked
def open_link_1():
    webbrowser.open("https://chat.openai.com/")

# Define the action to take when the second button is clicked
def open_link_2():
    webbrowser.open("https://github.com/")

# Create the first button
button_1 = tk.Button(text="ChatGPT", command=open_link_1)
button_1.pack()

# Create the second button
button_2 = tk.Button(text="GitHub", command=open_link_2)
button_2.pack()

# Show the main window
window.mainloop()
