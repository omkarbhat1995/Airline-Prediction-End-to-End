from flask import Flask , request, render_template
from src.pipeline.prediction_pipeline import CustomData

app= Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html")


@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="GET":
        return render_template("home.html")

    custom_Data = CustomData()
    output = custom_Data.receiveDataFromWeb(
        Airline=request.form.get("Airline"),
        Date_of_Journey=request.form.get("Dep_Time"),
        Source=request.form.get("Source"),
        Destination=request.form.get("Destination"),
        Arrival_Time=request.form.get("Arrival_Time"),
        Total_Stops=request.form.get("Total_Stops"),
    )
    print(output)

    return render_template("home.html",
        prediction_text=f"Your Flight price is Rs. {output[0]:.2f}")

if __name__== "__main__":
    app.run(host="0.0.0.0",debug=True)