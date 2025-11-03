from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"

# ------------------------
# Sample Projects Data
# ------------------------
projects = [
    {
        "title": "Portfolio Website",
        "description": "A personal portfolio website built with Flask, HTML, CSS, and JavaScript.",
        "image": "images/project1.png",
        "link": "https://example.com/portfolio"
    },
    {
        "title": "E-commerce App",
        "description": "A full-stack e-commerce application with user authentication and payment integration.",
        "image": "images/project2.png",
        "link": "https://example.com/ecommerce"
    },
    {
        "title": "Blog Platform",
        "description": "A responsive blog platform with CRUD functionality and Markdown support.",
        "image": "images/project3.png",
        "link": "https://example.com/blog"
    },
]

# ------------------------
# Routes
# ------------------------
@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About Me")

@app.route("/projects")
def projects_page():
    return render_template("projects.html", title="Projects", projects=projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Validation
        if not name or not email or not message:
            flash("Please fill in all fields!", "error")
            return redirect(url_for("contact"))

        # Save message
        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n{'-'*40}\n")

        flash("Message sent successfully!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html", title="Contact Us")

# ------------------------
# Main
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)
