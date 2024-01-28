from flask import Flask, redirect, url_for 

app = Flask(__name__) 

# Return thẻ HTML
@app.route('/') 
def home(): 
    return '<h1> Welcome </h1>'

# Truyền biến
# @app.route('/user/<name>') 
# def hello_user(name) : 
#     return f'<h2> Hello {name} </h2>'

# Chuyển hướng trang
@app.route('/admin') 
def hello_admin(): 
    return '<h2> Hello Admin </h2>' 

@app.route('/user/<name>') 
def hello_user(name) : 
    if name == 'admin' : 
        # Để chuyển hướng trang sử dụng redirect, url_for 
        return redirect(url_for('hello_admin'))
    return f'<h2> Hello {name} </h2>'

if __name__ == '__main__': 
    app.run(debug = True)       