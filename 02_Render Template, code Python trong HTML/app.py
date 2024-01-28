from flask import Flask, render_template 

app = Flask(__name__) 

@app.route('/') 
def home() : 
    return render_template('index.html') 

@app.route('/content')
def show_content(): 
    # Trong HTML, để hiện thị nội dung biến 'content' sử dụng {{content}}
    return render_template('show.html', 
                           content = 'UocNguyenThi',
                           names = ["UocNguyen", "YenVu", "QuangThuc"]) 
if __name__ == '__main__': 
    app.run(debug = True)       