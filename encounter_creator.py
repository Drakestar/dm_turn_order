from tkinter import *


class EncounterBox(Toplevel):
    def __init__(self, main):
        Toplevel.__init__(self)

        self.title("Encounter Generator")
        self.geometry("350x200")
        # File info
        self.file_text = Text(self, width=20, height=1)
        self.file_text.insert(INSERT, "Encounter file name:")
        self.file_text.config(state=DISABLED)
        self.file_text.grid(row=0, column=0, columnspan=1, sticky=NW)
        self.file_entry = Entry(self)
        self.file_entry.grid(row=0, column=1, columnspan=1, sticky=NW)
        # Input info
        self.name_text = Text(self, width=20, height=1)
        self.name_text.insert(INSERT, "Name")
        self.name_text.config(state=DISABLED)
        self.name_text.grid(row=1, column=0, columnspan=1, sticky=NW)
        self.bonus_text = Text(self, width=20, height=1)
        self.bonus_text.insert(INSERT, "Bonus")
        self.bonus_text.grid(row=1, column=1, columnspan=1, sticky=NW)
        self.bonus_text.config(state=DISABLED)
        # Input boxes
        self.en1 = Entry(self)
        self.en1.grid(row=3, column=0, columnspan=1, sticky=NW)
        self.eb1 = Entry(self)
        self.eb1.grid(row=3, column=1, columnspan=1, sticky=NW)
        self.en2 = Entry(self)
        self.en2.grid(row=4, column=0, columnspan=1, sticky=NW)
        self.eb2 = Entry(self)
        self.eb2.grid(row=4, column=1, columnspan=1, sticky=NW)
        self.en3 = Entry(self)
        self.en3.grid(row=5, column=0, columnspan=1, sticky=NW)
        self.eb3 = Entry(self)
        self.eb3.grid(row=5, column=1, columnspan=1, sticky=NW)
        self.en4 = Entry(self)
        self.en4.grid(row=6, column=0, columnspan=1, sticky=NW)
        self.eb4 = Entry(self)
        self.eb4.grid(row=6, column=1, columnspan=1, sticky=NW)
        # Save button
        self.save_button = Button(self, text="Save", command=self.save_encounter)
        self.save_button.grid(row=7, column=0)

    def save_encounter(self):
        mons = []
        mons.extend([self.en1.get(), self.eb1.get(), self.en2.get(), self.eb2.get(), self.en3.get(), self.eb3.get(), self.en4.get(), self.eb4.get()])
        name = self.file_entry.get()
        name += ".csv"
        file = open(name, 'w')
        mons = iter(mons)
        for x in mons:
            if x:
                file.write(x)
                file.write(", ")
                file.write(next(mons))
                file.write("\n")
        file.close()
        self.destroy()
