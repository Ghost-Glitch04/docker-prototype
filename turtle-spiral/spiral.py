import turtle

# --- Canvas setup ---
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Colorful Spiral")

# --- Turtle setup ---
t = turtle.Turtle()
t.hideturtle()
t.speed(0)    # fastest drawing speed
t.width(2)

# --- Animated spiral ---
# tracer is ON (default) so each step renders visibly
# speed(0) makes it draw as fast as the display can refresh
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "magenta"]

for i in range(300):
    t.color(colors[i % len(colors)])
    t.forward(i * 0.6)
    t.right(91)

# Keep the window open after drawing completes
screen.mainloop()
