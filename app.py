# Import Tkinter
import tkinter as tk

# Define the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the root window
root = tk.Tk()
root.title("My Web Application")

# Set the BG Color to Black
root.configure(bg="black")

# Set the size of the window and center it on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (WINDOW_WIDTH/2))
y = int((screen_height/2) - (WINDOW_HEIGHT/2))
root.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, x, y))

# Start the main event loop
root.mainloop()