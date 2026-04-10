from flask import Flask, render_template, request
import pickle
import numpy as np
from career_logic import get_career_info, skill_gap

app = Flask(__name__)

# Load model
model = pickle.load(open("model/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_data = {
        "Python": int(request.form["python"]),
        "Java": int(request.form["java"]),
        "SQL": int(request.form["sql"]),
        "ML": int(request.form["ml"]),
        "DSA": int(request.form["dsa"]),
        "Web": int(request.form["web"]),
        "Cloud": int(request.form["cloud"]),
        "Networking": int(request.form["networking"]),
        "Linux": int(request.form["linux"]),
        "Git": int(request.form["git"]),
        "MathInterest": int(request.form["math"]),
        "DesignInterest": int(request.form["design"]),
        "DataInterest": int(request.form["data"]),
        "ManagementInterest": int(request.form["management"]),
        "Communication": int(request.form["communication"]),
        "Leadership": int(request.form["leadership"]),
        "Creativity": int(request.form["creativity"])
    }

    features = np.array([list(user_data.values())])
    
    prediction = model.predict(features)[0]

    info = get_career_info(prediction)
    gaps = skill_gap(user_data, info.get("skills", []))

    return render_template(
        "result.html",
        career=prediction,
        description=info.get("description"),
        skills=info.get("skills",[]),
        gaps=gaps
    )

if __name__ == "__main__":
    app.run(debug=True)
