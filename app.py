from flask import Flask , request, render_template

app= Flask(__name__)

app.route("/")
def Home():
    return render_template("home.html")


app.route("/predict",["GET","POST"])
def predict():
    if request.method==["GET"]:
        return render_template("home.html")

        custom_Data = CustomData()
    df = custom_Data.receiveDataFromWeb(
        Airline=request.form.get("Airline"),
        Date_of_Journey=request.form.get("Dep_Time"),
        Source=request.form.get("Source"),
        Destination=request.form.get("Destination"),
        Arrival_Time=request.form.get("Arrival_Time"),
        Total_Stops=request.form.get("Total_Stops"),
    )

    output = custom_Data.clean_data(df)
    return render_template(
        "home.html",
        prediction_text=f"Your Flight price is Rs. {output}",
    )

if __name__== "__main__":
    app.run(host="0.0.0.0",debug=True)