import tkinter as tk
from PIL import Image, ImageTk, ImageOps, ImageDraw

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

# Set the background color to black-purple
root.configure(bg='#301934')

# Create a canvas to draw the circle
canvas = tk.Canvas(root, width=600, height=600, bg='#301934', highlightthickness=0)
canvas.pack()

# Load your photo
photo_path = 'C:/Users/mrkas/OneDrive/Desktop/Kasra_Kombat/WIN_20240612_17_49_44_Pro.jpg'
photo_image = Image.open(photo_path)
photo_image = ImageOps.fit(photo_image, (300, 300), Image.Resampling.LANCZOS)

# Create a circular mask
mask = Image.new('L', (300, 300), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + mask.size, fill=255)

# Apply the mask to the photo
photo_image.putalpha(mask)

# Convert the Image object into a TkPhoto object
tk_photo = ImageTk.PhotoImage(photo_image)

# Draw a circle with your photo
circle_center_x = 300
circle_center_y = 300
circle_radius = 150
canvas.create_image(circle_center_x, circle_center_y, image=tk_photo)

# Add a label to show the counter
counter_label = tk.Label(root, text=str(counter), bg='#301934', fg='white', font=('Helvetica', 24))
counter_label.pack()


# Bind the click event to the circle
canvas.bind("<Button-1>", on_circle_click)

# Keep a reference to the image object
root.photo_image = tk_photo

# Start the GUI loop
root.mainloop()
