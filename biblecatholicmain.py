from flask import Flask, render_template
import json
app = Flask(__name__)

f = open('biblequotedata.json', encoding='utf8')
data = json.load(f)

@app.route('/')
def mainpage():
    return render_template("index.html")

@app.route('/challengelist')
def challenge_list():
    return render_template('challenge_list.html', biblechallenges=data)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/challengelist/<challenge>')
def return_specific_challenge(challenge):
    quotes = []
    picture = ''
    for q in data:
        if q['challenge'] == challenge:
            quotes = q['quotes']
            picture = q['picture']
        
    return render_template('challenge.html',biblechallenge=challenge, biblequotes=quotes, challengepicture=picture)

    


if __name__ == "__main__":
    app.run(debug=True)
