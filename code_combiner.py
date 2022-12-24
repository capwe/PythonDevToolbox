import tkinter as tk

class CodeCombiner(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry('1200x800')
        self.is_dark_mode = False

        self.dark_mode_button = tk.Button(self, text='Light - Dark Mode', command=self.toggle_dark_mode)
        self.dark_mode_button.pack()

        self.master.title("Code Combiner")
        self.code_blocks = []
        self.current_block = 0

        # Initialisierung der Eingabeframe
        self.input_frame = tk.Frame(self)
        self.input_frame.pack(side='top', fill='both')

        self.input_label = tk.Label(self.input_frame, text='Input')
        self.input_label.pack(side='top')

        # Hinzufügen des Scrollbars für das Input-Textfeld
        self.input_scrollbar = tk.Scrollbar(self.input_frame)
        self.input_scrollbar.pack(side='right', fill='y')

        self.input_text = tk.Text(self.input_frame, height=10)
        self.input_text.pack(side='right', fill='both')
        self.input_text.focus_set()
        self.line_numbers = tk.Text(self.input_frame, width=4, padx=4, takefocus=0, border=0, background='khaki', state='disabled', wrap='none')
        self.line_numbers.pack(side='left', fill='y')

        self.update_line_numbers()
        self.input_text.bind('<Any-KeyPress>', self.update_line_numbers)
        self.input_text.bind('<Any-ButtonPress>', self.update_line_numbers)

        

        # Initialisierung der Ausgabeframe

        self.output_frame = tk.Frame(self)
        self.output_frame.pack(side='bottom', fill='both')
        self.output_label = tk.Label(self.output_frame, text='Output')
        self.output_label.pack(side='top')
        self.output_text = tk.Text(self.output_frame, height=10)
        self.output_text.pack(side='top', fill='both')

        self.combine_button = tk.Button(self, text='Kombinieren', command=self.combine_code)
        self.combine_button.pack()
        self.clear_button = tk.Button(self, text='Löschen', command=self.clear_code)
        self.clear_button.pack()

        self.copy_button = tk.Button(self, text='Kopieren', command=self.copy_output)
        self.copy_button.pack()


    def update_line_numbers(self, event=None):
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', 'end')
        for i, line in enumerate(self.input_text.get('1.0', 'end').split('\n')):
            self.line_numbers.insert('end', f'{i + 1}\n')
        self.line_numbers.config(state='disabled')
        self.line_numbers.config(height=int(self.input_text.index('end').split('.')[0]))

    def combine_code(self):
        self.code_blocks.append(self.input_text.get("1.0", "end"))
        combined_code = '\n'.join(self.code_blocks)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", combined_code)
        self.input_text.delete("1.0", "end")
        self.input_text.focus_set()

    def clear_code(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.input_text.focus_set()
        self.code_blocks = []
        self.current_block = 0

    def copy_output(self):
        self.output_text.clipboard_clear()
        self.output_text.clipboard_append(self.output_text.get("1.0", "end"))

    def toggle_dark_mode(self):
        if self.master.cget("bg") == "white":
            self.master.config(bg="darkgray")
            self.input_text.config(bg='darkgray', fg='black')
            self.output_text.config(bg='darkgray', fg='black')
            self.line_numbers.config(bg='darkgray', fg='black')
        else:
            self.master.config(bg="white")
            self.input_text.config(bg='white', fg='black')
            self.output_text.config(bg='white', fg='black')
            self.line_numbers.config(bg='white', fg='black')


root = tk.Tk()
app = CodeCombiner(master=root)
app.pack()
root.mainloop()
        