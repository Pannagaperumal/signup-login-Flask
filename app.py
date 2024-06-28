from flask import Flask,request,jsonify

app=Flask(__name__)

users={}



@app.route('/signup',methods=['POST'])
def signup():
    data =request.json
    username = data.get("username")
    password1 = data['password1']
    password2 = data['password2']

    if password1!=password2:
        return jsonify({"status":"Failed","message":"passwords should be same"})
    
    if password1 =="" or password2 =="" or username=="":
        return jsonify({"status":"Failed","message":"username or password cant be empty"})

    if username in users:
        return jsonify({"status":"Failed","message":"User exists login "})

    users[username]=password1

    return jsonify({"status":"Success","message":f"user {username} created successfully"})

@app.route('/login',methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password=data.get("password")

    if username not in users:
        return jsonify({"status":"Failed","message":f"user {username} Not present please signup"})
    
    if users[username]==password:
        return jsonify({"status":"Success","message":f"user {username} logged in"})


if __name__ =="__main__":
    app.run(debug = True)