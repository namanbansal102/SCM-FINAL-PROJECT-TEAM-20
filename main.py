from flask import Flask,render_template
app=Flask(__name__)
print("Running Flask app")
@app.route('/')
def returnIndex():
    print("Running Index Page")
    return render_template('index.html')
@app.route('/polling.html')
def returnPoll():
    print("Getting poll Page ")
    return render_template('polling.html')
@app.route('/about.html')
def returnAbout():
    print("Running About page")
    return render_template('about.html')
@app.route('/contact_us.html')
def returnContact():
    print("Running Contact Us page")
    return render_template('contact_us.html')

@app.route('/login.html')
def returnLogin():
    print("Running Contact Us page")
    return render_template('login.html')

@app.route('/favourites.html')
def returnFav():
    print("Running Contact Us page")
    return render_template('favourites.html')

app.run(debug=True)