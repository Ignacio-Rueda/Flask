from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tools.db' #users is the name of the table
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False#optional

db=SQLAlchemy(app)


class tools(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tool_name = db.Column(db.String(200))
    

    def __init__(self,tool_name):
        self.tool_name=tool_name

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/create-tool",methods=['POST'])
def create():
    tool = tools(tool_name=request.form['tool_name'])
    db.session.add(tool)
    db.session.commit()
    return "ok"

if __name__== "__main__":
    db.create_all()
    app.run(debug=True,port=5000)
