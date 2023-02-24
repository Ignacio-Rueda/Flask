from flask import Flask,jsonify,request
#jsonify nos permite convertir un objeto a json típico del navegador
#request proporciona los datos que me envian por peticiones http

app= Flask(__name__)

from productos import products

#Create a Flask Instance
#Las rutas por defecto funcionan con el método GET,no es necesario indicarlo
@app.route("/ping")
def ping():
    return jsonify({"message":"pong"})

#Va a devolver la lista de prodcutos que tenemos
@app.route("/products",methods=["GET"])
def getProducts():
    return jsonify({"products":products,"message":"Product list"})


#Obtener un producto de mi lista de productos
@app.route("/product/<string:product_name>")
def getProduct(product_name):
    product_found=[product for product in products if product ["name"]==product_name]
    if (len(product_found)>0):
        return jsonify({"message":"received","product":product_found[0]})
    return({"message":"not found"})

#Crear datos 
@app.route("/products",methods=["POST"])
def addProduct():
    #print(request.json)
    new_product = {
        "name":request.json["name"],
        "price":request.json["price"],
        "quantity":request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message":"productos actualizados correctamente","products":products})

#Actualizar datos
@app.route("/products/<string:product_name>",methods=["PUT"])
def editProduct(product_name):
    product_found=[product for product in products if product["name"]==product_name]
    if (len(product_found)>0):
        product_found[0]['name']=request.json['name']
        product_found[0]['price']=request.json['price']
        product_found[0]['quantity']=request.json['quantity']
        return jsonify(

            {
                "message":"product found",
                "producto actualizado":product_found[0]
            }
        )
    return jsonify({
        "message":"Lo siento, algo ha salido mal"
    })
#Eliminar datos
@app.route("/products/<string:product_name>",methods=["DELETE"])
def deleteProduct(product_name):
    product_found=[product for product in products if product ['name']==product_name]
    if(len(product_found)>0):
        products.remove(product_found[0])
        return jsonify(
            {
                "message":"Lista actualizada",
                "products":products
            }

        )
    return jsonify({
        "message":"Producto no encontrado"
    })


#Si el archivo ejecutado es el programa principal ejecuta la aplicación
if __name__=='__main__':
    app.run(debug=True,port=5000) #debug=True,port=5000) Modo depurador, si hacemos algún cambio lo podemos ir viendo
