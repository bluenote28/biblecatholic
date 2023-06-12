from flask import Flask, render_template
import json
app = Flask(__name__)

f = open('biblequotedata.json', encoding='utf8')
data = json.load(f)



def build_quotes_list(quotes_string):
    curr_index = 1
    end_index = quotes_string.index(']')
    quote_list = []
    new_string = ""


    while curr_index < end_index:
        if quotes_string[curr_index] == ',' and quotes_string[curr_index - 1] == '\"' or quotes_string[curr_index] == ',' and quotes_string[curr_index - 1] == '\'':
            quote_list.append(new_string)
            new_string = ""
            curr_index += 1
        else:
            new_string += quotes_string[curr_index]
            curr_index +=1
    quote_list.append(new_string)
    return quote_list

@app.route('/')
def mainpage():
    return render_template("index.html")

@app.route('/challengelist')
def challenge_list():
    return render_template('challenge_list.html', biblechallenges=data)
        
@app.route('/proof/<challenge>/<quotes>')
def create_link(challenge, quotes):
    quotes_list = build_quotes_list(quotes)
    print(type(quotes_list))
    return render_template("challenge.html", challenge_name=challenge, bible_quotes=quotes_list)

@app.route('/about')
def about_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()