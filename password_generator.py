import string
import tkinter as tk
import tkinter.ttk as ttk
import secrets


def generate_password(length, use_capital_letters, use_lowercase_letters):
    # Erstelle eine Liste mit allen möglichen Zeichen
    characters = string.digits
    if use_capital_letters:
        characters += string.ascii_uppercase
    if use_lowercase_letters:
        characters += string.ascii_lowercase

    # Wähle zufällige Zeichen aus der Liste aus und kombiniere sie zu einem Passwort
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password


def update_password(*args):
    # Generiere ein Passwort entsprechend der Einstellungen des Schiebereglers und der Checkboxen
    password = generate_password(
        length=length_slider.get(),
        use_capital_letters=capital_letters_var.get(),
        use_lowercase_letters=lowercase_letters_var.get()
    )
    # Aktualisiere das Output-Feld mit dem neuen Passwort
    password_output.set(password)


# Erstelle ein GUI-Fenster
window = tk.Tk()
window.title("Password Generator")

# Erstelle eine Überschrift
header_label = tk.Label(master=window, text="Password Generator", font=("Arial", 16))
header_label.pack(pady=(10, 20))

# Erstelle ein Output-Feld für das Passwort
password_output = tk.StringVar()
password_label = tk.Label(master=window, text="Password:")
password_entry = tk.Entry(master=window, textvariable=password_output, width=30, state="readonly")
password_entry.pack(pady=(10, 0))

# Erstelle einen Button zum Kopieren des Passworts
copy_button = tk.Button(master=window, text="Copy", command=lambda: password_entry.event_generate("<<Copy>>"))
copy_button.pack(pady=(5, 10))

# Erstelle einen Schieberegler zur Auswahl der Passwortlänge
length_label = tk.Label(master=window, text="Length:")
length_label.pack()
length_slider = tk.Scale(master=window, from_=8, to=32, orient=tk.HORIZONTAL, command=update_password)
length_slider.pack()

# Erstelle Checkboxen zur Auswahl der verwendeten Zeichenarten
capital_letters_var = tk.BooleanVar()
capital_letters_checkbox = tk.Checkbutton(master=window, text="Capital letters", variable=capital_letters_var,
                                          command=update_password)
capital_letters_checkbox.pack()
lowercase_letters_var = tk.BooleanVar()
lowercase_letters_checkbox = tk.Checkbutton(master=window, text="Lowercase letters", variable=lowercase_letters_var,
                                            command=update_password)
lowercase_letters_checkbox.pack()

# Generiere ein initiales Passwort
update_password()

# Zeige das GUI-Fenster an
window.mainloop()
