from flask import Flask,request,render_template,jsonify
from src.pipelines.prediction_pipeline import custumData,PredictionPipeline

application = Flask(__name__)

app = application

@app.route('/',methods=['GET','POST'])
def predict_data():
    if request.method=='GET':
        return render_template('index.html')
    else:
        data = custumData(
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        final_new_data = data.get_data_as_DataFrame()
        predict_pipline= PredictionPipeline()
        pred = predict_pipline.predict(final_new_data)
        
        result = round(pred[0],2)
        
        return render_template('index.html',final_result = result)
    
if __name__=='__main__':
    application.run()
