from flask import Flask,request,render_template,jsonify
from utilities import Fish_Weight
import config

app=Flask(__name__)

@app.route("/")
def app_home():
    return render_template("index.html")

@app.route("/prediction",methods=["post"])
def get_weight():
    data=request.form
    Length1=float(data['Length1'])
    Length2=float(data['Length2'])
    Length3=float(data['Length3'])
    Height=float(data['Height'])
    Width=float(data['Width'])
    Species=data['Species']

    wt=Fish_Weight(Length1,Length2,Length3,Height,Width,Species)
    weight=wt.get_predicted_weight()

    #return jsonify({'Result':weight})
    return render_template("index.html" , Result=weight)

if __name__=="__main__":
    app.run(debug=True, port=config.PORT, host=config.HOST)



