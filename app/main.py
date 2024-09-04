from  flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/meetings.html')
def meetings():
    return render_template('meetings.html')

@app.route('/meeting-details.html')
def meeting():
    return render_template('meeting-details.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 1010)

