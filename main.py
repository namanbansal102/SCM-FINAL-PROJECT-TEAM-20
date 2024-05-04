from flask import Flask,render_template
app=Flask(__name__)
print("Running Flask app")
@app.route('/')
def returnIndex():
    print("Running Index Page")
    return render_template('index.html')