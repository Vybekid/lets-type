import turtle

# Set up screen
screen = turtle.Screen()
screen.title("Spiritual & Health Benefits Selector")
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")

# Create turtle for drawing buttons and text
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Dictionaries for benefits
semen_retention_benefits = {
    1: "Ojas nourishes the brain, sharpening intellect.",
    2: "Brahmacharya helps control the mind and senses.",
    3: "Avoiding pleasure helps focus on Krishna.",
    4: "True strength is free from attachment.",
    5: "Celibacy opens the door to Moksha.",
    6: "Transforms physical energy into spiritual power.",
    7: "Boosts determination and willpower.",
    8: "Gives Krishna a special place in the heart.",
    9: "Helps overcome the fire of lust.",
    10: "Leads to spiritual perfection through hearing."
}

drug_cessation_benefits = {
    11: "Improved physical and mental wellbeing.",
    12: "Reduced risk of organ damage and death.",
    13: "Better relationships with loved ones.",
    14: "Reconnect with your true emotions.",
    15: "Increased natural energy.",
    16: "Deeper, more restful sleep.",
    17: "A more youthful, healthy appearance.",
    18: "Save significant money over time.",
    19: "Boosted immune function.",
    20: "Sharper memory and better focus."
}

# Function to display benefit
def display_benefit(x, y, number):
    writer.clear()
    if 1 <= number <= 10:
        benefit = semen_retention_benefits[number]
        title = "Semen Retention Benefit"
    else:
        benefit = drug_cessation_benefits[number]
        title = "Drug Cessation Benefit"

    writer.goto(0, 200)
    writer.write(f"{title} #{number}", align="center", font=("Arial", 20, "bold"))

    writer.goto(0, 150)
    writer.write(benefit, align="center", font=("Arial", 14, "normal"))

# Create buttons
def create_button(number, x, y):
    button = turtle.Turtle()
    button.penup()
    button.hideturtle()
    button.goto(x, y)
    button.shape("square")
    button.color("black", "white")
    button.shapesize(stretch_wid=2, stretch_len=3)
    button.showturtle()
    button.write(str(number), align="center", font=("Arial", 14, "bold"))
    screen.onclick(lambda x_click, y_click: check_click(x_click, y_click, x, y, number))

def check_click(x_click, y_click, x, y, number):
    if abs(x_click - x) < 30 and abs(y_click - y) < 20:
        display_benefit(x_click, y_click, number)

# Draw all buttons
start_x = -250
start_y = 50
gap_x = 60
gap_y = 60

for i in range(1, 21):
    col = (i - 1) % 5
    row = (i - 1) // 5
    create_button(i, start_x + col * gap_x, start_y - row * gap_y)

# Keep the window open
turtle.done()
