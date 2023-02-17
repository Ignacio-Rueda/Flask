from flask import Flask
app= Flask (__name__)

@app.route("/")
def index():
    return "Hola Nachete!"

#Si el archivo ejecutado es el programa principal ejecuta la aplicación
if __name__=='__main__':
    app.run(debug=True,port=5000)