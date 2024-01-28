from flask import Flask, render_template, request, redirect, url_for 

app = Flask(__name__) 

@app.route('/user/<name>') 
def hello_user(name) : 
    return f'<h2> Hello {name} </h2>'

@app.route('/login', methods =  ['POST', 'GET'])
def login (): 
    if request.method == 'POST': 
        username = request.form['username'] 
        if username : 
            return redirect(url_for('hello_user', name = username))
    return render_template('index.html') 

if __name__ == '__main__': 
    app.run(debug = True)       