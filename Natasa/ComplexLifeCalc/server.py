from FunctionsforCOL import calculate_score
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def komplikator():
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        status = request.form['status']
        ignorance = request.form['ignorance']
        money_have = request.form['money_have']
        money_wants = request.form['money_wants']
        money_spent = request.form['money_spent']
        online_popularity = request.form['online_popularity']
        rl_friends = request.form['rl_friends']

        if age.isdigit() and money_have.isdigit() and money_spent.isdigit() and money_wants.isdigit() and online_popularity.isdigit() and rl_friends.isdigit():
            return render_template('komplikator_result.html', complexity = calculate_score(gender, age, status, ignorance, money_have, money_wants, money_spent, online_popularity, rl_friends))
        else:
            return render_template('komplikator_error.html', message = "Age, Ignorance, Money have, Money wants, Money spent and Klout score must be digits without special signs!")
    else:
        return render_template('komplikator_form.html')

if __name__ == "__main__":
    app.run(debug = True)