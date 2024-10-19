from flask import Flask
# must always install flask first, its the framework.
# check if any the file can run.

from flask import render_template, request
#backend

app = Flask(__name__) #object name
#launching a program in the handphone.
#evidence of the person launching this program in the website. Render will look for this person ie the registered user of github workspaces.

@app.route("/",methods=["GET","POST"])
#backend program (born in 1985). this is standard flask style. Get = Request. Post = from backend to frontend.
#frontend 
#Back USA = flask. Get = Request from front. and Post (RT) to back
#Front China = HTML, CSS, JS
#Protocol = WSGI to communicate btw front and backend
#use the command pip install gunicorn.py

def index():
    #to insert the model. do a float.
    return(render_template("index.html"))
#page to enter the score

#create second page to get the reprediction
@app.route("/prediction_DBS",methods=["GET","POST"])
def prediction_DBS():
    q = float(request.form.get("q"))
    return(render_template("prediction_DBS.html",r=90.2+(-50.6*q)))

if __name__ == "__main__":
    app.run()
#__ means clearance check to confirm again the user name


