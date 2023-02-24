from flask import Flask,render_template,request,jsonify


app = Flask(__name__)

@app.route("/")
def home():
    return "Tu audio es xxxxx xxxxx xxxx"
@app.route("/post",methods=['POST'])
def send():
    producto = {
        "path":request.json["path"],
        "word":request.json["word"]
    }
    print(producto)
    return"recibido"

if __name__=='__main__':
    app.run(debug=True,port=5000)