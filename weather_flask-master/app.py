from flask import Flask, render_template, request, url_for
from weather import main as get_weather

app= Flask(__name__)

@app.route("/", methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    data=None
    if request.method == 'POST':
        city= request.form['cityname']
        state= request.form['statename']
        country= request.form['countryname']
        data = get_weather(city, state, country)
        return render_template('result.html', data=data)
    
    return render_template('home.html')




if __name__ == "__main__":
    app.run(debug=False)