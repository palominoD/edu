from  flask import Flask, render_template

app = Flask(__name__)

@app.router('/')
def home():
    return render_template('index.html')

@app.router('/index.html')
def index():
    return render_template('index.html')

if __name__ == '__main__':
app.run(host = '0.0.0.0', port = 1010)

