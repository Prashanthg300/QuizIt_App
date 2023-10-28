from tkinter import *
from tkinter import ttk

class InputWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("QuizIt App")
        self.root.geometry("850x600")
        title = Label(self.root, text="QuizIt Application",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)

        # Create a label with some text
        label=Label(self.root, text="""1. General Knowledge
        2. Entertainment: Books
        3. Entertainment: Film
        4. Entertainment: Music
        5. Entertainment: Musicals & Theatres
        6. Entertainment: Television
        7. Entertainment: Video Games
        8. Entertainment: Board Games
        9. Science & Nature
        10. Science: Computers
        11. Science: Mathematics
        12. Mythology
        13. Sports
        14. Geography
        15. History
        16. Politics
        17. Art
        18. Celebrities
        19. Animals
        20. Vehicles
        21. Entertainment: Comics
        22. Science: Gadgets
        23. Entertainment: Japanese Anime & Manga
        24. Entertainment: Cartoon & Animations
        """,
        font=("Courier 10 bold"))
        label.pack(padx=6, pady=60)

        # Create an Entry box for input
        self.entry = Entry(self.root)
        self.entry.pack(pady = 0)

        # Functionality to create a button
        button = Button(self.root, text="Get Value", command=self.get_input)
        button.pack()

    def get_input(self):
        self.value = self.entry.get()  # Retrieve the value from the Entry
        self.root.destroy()  # Close the window

    def return_value(self):
        return self.value if hasattr(self, 'value') else None

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    input_window = InputWindow()
    input_window.start()