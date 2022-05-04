from flask import Flask, request, render_template, redirect, url_for
import info

# make simple flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', tweet=info.getTweet()[0])

if __name__ == '__main__':
    app.run(debug=True)









