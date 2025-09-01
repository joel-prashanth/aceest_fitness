from flask import Flask, request, render_template, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "devsecret"  # needed for flash messages

# In-memory storage
workouts = []


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add_workout", methods=["POST"])
def add_workout():
    workout = request.form.get("workout")
    duration = request.form.get("duration")
    calories = request.form.get("calories")
    reps = request.form.get("reps")

    if workout and duration:
        workouts.append({
            "workout": workout,
            "duration": int(duration),
            "calories": int(calories) if calories else None,
            "reps": int(reps) if reps else None,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        flash(f"Workout '{workout}' added successfully!", "success")
    return redirect(url_for("view_workouts"))


@app.route("/workouts")
def view_workouts():
    return render_template("workouts.html", workouts=workouts)


@app.route("/reset", methods=["POST"])
def reset_workouts():
    workouts.clear()
    flash("All workouts have been reset!", "warning")
    return redirect(url_for("view_workouts"))


if __name__ == "__main__":
    app.run(debug=True)  # for local dev only
