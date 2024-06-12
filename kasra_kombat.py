import tkinter as tk

def on_circle_click(event):
    global counter
    # Check if the click is within the circle's radius
    if (event.x - circle_center_x)**2 + (event.y - circle_center_y)**2 < circle_radius**2:
        counter += 1
        counter_label.config(text=str(counter))

# Initialize the counter
counter = 0

# Create the main window
root = tk.Tk()
root.title("Click the Circle")

# Create a canvas to draw the circle
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw a circle
circle_center_x = 200
circle_center_y = 200
circle_radius = 50
canvas.create_oval(circle_center_x - circle_radius, circle_center_y - circle_radius,
                   circle_center_x + circle_radius, circle_center_y + circle_radius,
                   fill='blue')

# Add a label to show the counter
counter_label = tk.Label(root, text=str(counter))
counter_label.pack()

# Bind the click event to the circle
canvas.bind("<Button-1>", on_circle_click)

# Start the GUI loop
root.mainloop()
