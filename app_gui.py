from encounter_creator import *


class TurnGUI(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Turn Tracker")
        self.geometry("300x300")
        menu = Menu(self)
        self.config(menu=menu)

        # Menu
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.new)
        filemenu.add_command(label="New Encounter", command=self.makeMons)

        # Function buttons
        self.greet_button = Button(self, text="Add", command=self.greet)
        self.greet_button.grid(row=0, column=3, columnspan=1)

        self.close_button = Button(self, text="Next turn", command=self.quit)
        self.close_button.grid(row=0, column=4, columnspan=1)

        self.entry_test = Entry(self)
        self.entry_test.grid(row=1, column=1)

    def greet(self):
        print("aids")

    def new(self):
        print("start new combat")

    def makeMons(self):
        window = EncounterBox(self)

    def loadChars(self):
        print("will load players")
