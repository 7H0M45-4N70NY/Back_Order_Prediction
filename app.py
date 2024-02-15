from flask import Flask,render_template,request
import os
import numpy as np
import pandas as pd
from src.Back_Order.pipeline.prediction_stage import PredictionPipeline,CustomData
from src.Back_Order.exception.exception import customexception
import sys

app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index2.html")

#@app.route("/",methods=["GET","POST"])
#def home():
    #return render_template("form.html")

@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def predict():
    if request.method == 'POST':
        try:
            data=CustomData(
            #  reading the inputs given by the user
                national_inv =float(request.form.get('national_inv')),
                lead_time =float(request.form.get('lead_time')),
                in_transit_qty =float(request.form.get('in_transit_qty')),
                forecast_3_month =float(request.form.get('forecast_3_month')),
                sales_1_month =float(request.form.get('sales_1_month')),
                min_bank =float(request.form.get('min_bank')),
                pieces_past_due =float(request.form.get('pieces_past_due')),
                perf_6_month_avg =float(request.form.get('perf_6_month_avg')),
                local_bo_qty =float(request.form.get('local_bo_qty')),
                potential_issue =str(request.form.get('potential_issue')),
                deck_risk =str(request.form.get('deck_risk')),
                oe_constraint =str(request.form.get('oe_constraint')),
                ppap_risk =str(request.form.get('ppap_risk')),
                stop_auto_buy =str(request.form.get('stop_auto_buy')),
                rev_stop =str(request.form.get('rev_stop'))
            )
            data =data.get_data_as_dataframe()
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            raise customexception(e,sys)

    else:
        return render_template('index.html')




if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080,debug=True)