from flask import Flask,render_template
app=Flask(__name__)

@app.route('/food munch/')
def index():
    return render_template('food munch.html')


if __name__=='__main__':
    app.run(debug = True)
