from flask import Flask,jsonify,request


app = Flask (__name__)
from meals import meal

@app.route("/")
def init():
    return jsonify(

        {
            "message":"Welcome!"
        }
    )
@app.route("/meals",methods=["GET"])
def meals():
    return jsonify(
        {
            "message":"Available meals:",
            "meals":meal

        }
    )

#Get a product of my list
@app.route("/meals/<string:product_name>")
def getMeal(product_name):
   productFound=[one_meal for one_meal in meal if one_meal["name"]==product_name]
   if(len(productFound)>0):
    return jsonify(
        {
            "Your meal":productFound[0]
        }
    )

#Create meal
@app.route("/meals",methods=["POST"])
def addMeal():
    #print(request.json)
    new_meal={
        "name":request.json["name"],
        "kcal":request.json["kcal"],
        "quantity":request.json["healthy"]
    }
    meal.append(new_meal)
    return jsonify(
        {
            "Updates meals":meal
        }
    )

#Updates meals
@app.route("/meals/<string:product_name>",methods=["PUT"])
def editMeal(product_name):
    product_found=[one_meal for one_meal in meal if one_meal ["name"]== product_name]
    if(len(product_found)>0):
        product_found[0]["name"]=request.json["name"]
        product_found[0]["kcal"]=request.json["kcal"]
        product_found[0]["healthy"]=request.json["healthy"]
        return jsonify(
            {
                "message":"update meal!",
                "update meal":product_found[0]
            }
        )
    return jsonify(
        {
            "message":"Mistake!"
        }
    )
#Delete meals
@app.route("/meals/<string:product_name>",methods=["DELETE"])
def deleteMeal(product_name):
    product_found = [one_meal for one_meal in meal if one_meal ["name"] == product_name]
    if (len(product_found)>0):
        meal.remove(product_found[0])
        return jsonify(
            {
                "message":"Update meals",
                "meals":meal
            }
        )
    return jsonify(
        {
            "message":"mistake"
        }
    )
    


if __name__ == "__main__":
    app.run(debug=True,port=5000)