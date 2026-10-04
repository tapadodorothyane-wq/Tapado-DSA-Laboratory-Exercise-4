from flask import Flask, render_template, request, session
import math

app = Flask(__name__)
app.secret_key = "nectar_dsa_secret"

profile_data = {
    "name": "Dorothy Ane Tapado",
    "title": "Student",
    "location": "Santa Maria, Bulacan",
    "email": "tapadodorothyane@gmail.com",
    "phone": "09773330164",
    "about": "I am a computer engineering student who finds fun in seeing cute things and thought of combining what I love in my works, including this site.",
    "education": "Bachelor of Science in Computer Engineering",
    "interests": ["Photography", "Movies", "K-drama", "Anime", "Foods", "Chiikawas"]
}

@app.route("/")
def index():
    return render_template("index.html", profile=profile_data)

@app.route("/profile")
def profile():
    return render_template("profile.html", profile=profile_data)

@app.route("/works", methods=["GET", "POST"])
def works():
    result = None
    if request.method == "POST":
        text = request.form.get("inputString", "").strip()
        result = text.upper()
    return render_template("works.html", result=result, profile=profile_data)

@app.route("/works/area/circle", methods=["GET", "POST"])
def acircle():
    result = None
    radius = ""
    if request.method == "POST":
        radius = request.form.get("radius", "").strip()
        try:
            r = float(radius)
            if r < 0:
                result = "Radius must be positive."
            else:
                result = round(math.pi * r * r, 2)
        except ValueError:
            result = "Please enter a valid number."
    return render_template("circle.html", profile=profile_data, result=result, radius=radius)

@app.route("/works/area/triangle", methods=["GET", "POST"])
def atriangle():
    result = None
    base = ""
    height = ""
    if request.method == "POST":
        base = request.form.get("base", "").strip()
        height = request.form.get("height", "").strip()
        try:
            b = float(base)
            h = float(height)
            if b < 0 or h < 0:
                result = "Base and height must be positive."
            else:
                result = round(0.5 * b * h, 2)
        except ValueError:
            result = "Please enter valid numbers."
    return render_template("triangle.html", profile=profile_data, result=result, base=base, height=height)

@app.route("/works/linked-list", methods=["GET", "POST"])
def linked_list():
    if "linked_list" not in session:
        session["linked_list"] = ["Bloom", "Ink", "Canvas", "Sketch"]

    items = session["linked_list"]
    message = None

    if request.method == "POST":
        action = request.form.get("action")
        value = request.form.get("value", "").strip()

        if action == "add":
            if value:
                if value not in items:
                    items.append(value)
                    message = f"Added '{value}' to the sketchpad."
                else:
                    message = f"'{value}' is already on the page."
            else:
                message = "Please enter a name."

        elif action == "delete":
            if value and value in items:
                items.remove(value)
                message = f"Removed '{value}' from the sketchpad."
            else:
                message = "Item not found."

        elif action == "clear":
            items.clear()
            message = "Sketchpad cleared."

        session["linked_list"] = items

    return render_template("linked_list.html", profile=profile_data, linked_list=items, message=message)

@app.route("/contact")
def contact():
    return render_template("contact.html", profile=profile_data)

if __name__ == "__main__":
    app.run(debug=True)