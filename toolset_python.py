import tkinter as tk
import subprocess

# Erstelle das Hauptfenster
window = tk.Tk()
window.title("Python Dev Toolbox")

# Erstelle ein 4x5-Raster für die Buttons
buttons = []
for i in range(4):
    row = []
    for j in range(5):
        if i == 0 and j == 0:
            # Erstelle einen Button mit der Beschriftung "Code Combiner"
            button = tk.Button(text="Code Combiner")
            # Definiere die Aktion, die ausgeführt wird, wenn der Button geklickt wird
            def on_button_clicked():
                subprocess.run(["python", "code_combiner.py"])
            button.config(command=on_button_clicked)
        elif i == 0 and j == 1:
            # Erstelle einen Button mit der Beschriftung "Password Generator"
            button = tk.Button(text="Password Generator")
            # Definiere die Aktion, die ausgeführt wird, wenn der Button geklickt wird
            def on_button_clicked():
                subprocess.run(["python", "password_generator.py"])
            button.config(command=on_button_clicked)
        else:
            # Erstelle einen Button mit der Nummer (i * 5 + j + 2) als Beschriftung
            button = tk.Button(text=str(i * 5 + j + 2))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

# Zeige das Hauptfenster an
window.mainloop()