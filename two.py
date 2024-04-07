import tkinter as tk

class WindowOne:
    def __init__(self, root):
        self.root = root
        self.root.title("Window One")

        # Create buttons to switch to Window Two and Window Three
        self.button_to_window_two = tk.Button(self.root, text="Go to Window Two", command=self.open_window_two)
        self.button_to_window_two.pack(pady=10)

        self.button_to_window_three = tk.Button(self.root, text="Go to Window Three", command=self.open_window_three)
        self.button_to_window_three.pack(pady=10)

    def open_window_two(self):
        # Close current window and open Window Two
        self.root.destroy()
        window_two = tk.Tk()
        WindowTwo(window_two)

    def open_window_three(self):
        # Close current window and open Window Three
        self.root.destroy()
        window_three = tk.Tk()
        WindowThree(window_three)

class WindowTwo:
    def __init__(self, root):
        self.root = root
        self.root.title("Window Two")

        # Create buttons to switch to Window One and Window Three
        self.button_to_window_one = tk.Button(self.root, text="Go to Window One", command=self.open_window_one)
        self.button_to_window_one.pack(pady=10)

        self.button_to_window_three = tk.Button(self.root, text="Go to Window Three", command=self.open_window_three)
        self.button_to_window_three.pack(pady=10)

    def open_window_one(self):
        # Close current window and open Window One
        self.root.destroy()
        window_one = tk.Tk()
        WindowOne(window_one)

    def open_window_three(self):
        # Close current window and open Window Three
        self.root.destroy()
        window_three = tk.Tk()
        WindowThree(window_three)

class WindowThree:
    def __init__(self, root):
        self.root = root
        self.root.title("Window Three")

        # Create buttons to switch to Window One and Window Two
        self.button_to_window_one = tk.Button(self.root, text="Go to Window One", command=self.open_window_one)
        self.button_to_window_one.pack(pady=10)

        self.button_to_window_two = tk.Button(self.root, text="Go to Window Two", command=self.open_window_two)
        self.button_to_window_two.pack(pady=10)

    def open_window_one(self):
        # Close current window and open Window One
        self.root.destroy()
        window_one = tk.Tk()
        WindowOne(window_one)

    def open_window_two(self):
        # Close current window and open Window Two
        self.root.destroy()
        window_two = tk.Tk()
        WindowTwo(window_two)

if __name__ == "__main__":
    # Create the main window (Window One)
    root = tk.Tk()
    app_one = WindowOne(root)

    # Start the Tkinter event loop
    root.mainloop()