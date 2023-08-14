from flask import Flask, render_template

app = Flask(__name__, '/static')

@app.route("/")
def display_curriculum():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()