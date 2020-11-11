"""
View is a graphical representation of the model data.
"""
#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk,  Menu, colorchooser as cc, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd

#===========================
# View
#===========================
class View(tk.Tk):
    #------------------------------------------
    # Initialize
    #------------------------------------------
    def __init__(self, controller):
        super().__init__()
        self._controller = controller

        self._init_config()
        self._init_vars()
        self._init_UI()

    #------------------------------------------
    # Instance Attributes
    #------------------------------------------
    def _init_vars(self):
        pass

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def _init_config(self):
        self.resizable(True, True)
        self.title('MVC template')
        self.iconbitmap('python.ico')
        self._style = ttk.Style(self)
        self._style.theme_use('clam')

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def _init_UI(self):
        pass

    #-------------------------------------------
    # Start Loop
    #-------------------------------------------
    def main(self):
        self.mainloop()




















    #     self.title('Calculator')
    #     self.frame = self._make_frame()

    #     self.entry_var = tk.StringVar()
    #     entry = self._make_entry(self.frame, self.entry_var, tk.RIGHT)

    #     self._make_button()

    # def main(self):
    #     self.mainloop()

    # def _make_entry(self, parent, var_, justify):
    #     entry = ttk.Entry(parent, textvariable=var_, justify=justify, state=tk.DISABLED)
    #     entry.pack()

    # def _make_frame(self):
    #     frame = ttk.Frame()
    #     frame.pack(padx=10, pady=10)
    #     return frame

    # def _make_button(self):
    #     outer_frame = ttk.Frame(self.frame)
    #     outer_frame.pack()

    #     frame = ttk.Frame(outer_frame)
    #     frame.pack()

    #     buttons_in_row = 0
    #     for caption in self.buttons_captions:
    #         if buttons_in_row == self.BUTTONS_MAX_PER_ROW:
    #             frame = ttk.Frame(outer_frame)
    #             frame.pack()

    #             buttons_in_row = 0

    #         button = ttk.Button(frame, text=caption)
    #         button.pack(side=tk.LEFT)

    #         buttons_in_row += 1

