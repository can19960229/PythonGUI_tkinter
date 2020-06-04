import tkinter as tk


class Window:
    def __init__(self, handle):
        self.win = handle
        self.createwindow()
        self.run()

    def createwindow(self):
        self.win.geometry('400x400')
        # label 1
        self.label_text = tk.StringVar()
        self.label_text.set("----")
        self.lable = tk.Label(self.win,
                              textvariable=self.label_text,
                              font=('Arial', 11), width=15, height=2)
        self.lable.pack()

        # text_contrl
        self.entry_text = tk.StringVar()
        self.entry = tk.Entry(self.win, textvariable=self.entry_text, width=30)
        self.entry.pack()

        # button
        self.button = tk.Button(self.win, text="set label to text", width=15, height=2, command=self.setlabel)
        self.button.pack()

    def setlabel(self):
        print(self.entry_text.get())
        self.label_text.set(self.entry_text.get())

    def run(self):
        try:
            self.win.mainloop()
        except Exception as e:
            print("*** exception:\n".format(e))


def main():
    window = tk.Tk()
    window.title('hello tkinter')
    Window(window).run()


if __name__ == "__main__":
    main()
