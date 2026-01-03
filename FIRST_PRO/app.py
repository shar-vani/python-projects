from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("log_model.pk1", "rb"))

@app.route('/', methods=["GET", "POST"])
def index():
    prediction = ""
    if request.method == "POST":
        GENDER = int(request.form["Gender"])
        AGE = int(request.form["AGE"])
        SMOKING = int(request.form["SMOKING"])
        YELLOW_FINGERS = int(request.form["YELLOW_FINGERS"])
        ANXIETY = int(request.form["ANXIETY"])
        PEER_PRESSURE = int(request.form["PEER_PRESSURE"])
        CHRONIC_DISEASE = int(request.form["CHRONIC DISEASE"])
        FATIGUE = int(request.form["FATIGUE"])
        ALLERGY = int(request.form["ALLERGY"])
        WHEEZING = int(request.form["WHEEZING"])
        ALCOHOL_CONSUMING = int(request.form["ALCOHOL_CONSUMING"])
        COUGHING = int(request.form["COUGHING"])
        SHORTNESS_OF_BREATH = int(request.form["SHORTNESS_OF_BREATH"])
        SWALLOWING_DIFFICULTY = int(request.form["SWALLOWING_DIFFICULTY"])
        CHEST_PAIN = int(request.form["CHEST_PAIN"])

        data = [[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, 
                 CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, 
                 COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]]
        res = model.predict(data)
        
        if res[0] == 1:
            prediction = "LUNG CANCER"
        else:
            prediction = "NO CANCER"

    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run()
    