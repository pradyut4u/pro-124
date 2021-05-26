from flask import Flask,jsonify,request

app = Flask(__name__)
task = [{
    'id':1,
    'title':"postman",
    'contact':"0123654789"
    },
    {
        'id':2,
        'title':"flask",
        'contact':"3698520147"
    }
]
@app.route("/")
def route_1():
    return "created by Pradhyut"

@app.route("/get-data")
def route_2():
    return jsonify({
        "data":task
    })

@app.route("/add-data",methods = ["POST"])
def route_3():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data."
        },400)
    t = {
        "id":task[-1]['id']+1,
        'title':request.json.get("title",""),
        'contact':request.json['contact'] 
    }    
    task.append(t)
    return jsonify({
        "status":"success",
        "message":"Data is added"
    })

if(__name__=="__main__"):
    app.run(debug=True)