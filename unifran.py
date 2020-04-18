from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def unifran():
    return render_template('unifran.html')
if __name__ == '__main__':
    app.run()