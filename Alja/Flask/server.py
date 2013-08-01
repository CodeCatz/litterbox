from kalkulator import overall_score
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def komplikator():
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        status = request.form['status']
        ignorance = request.form['ignorance']
        money_have = request.form['money_have']
        money_wants = request.form['money_wants'] 
        money_spent = request.form['money_spent']
        popularity_online = request.form['popularity_online']
        rl_friends = request.form['rl_friends']
        if age.isdigit() and ignorance.isdigit() and money_have.isdigit() and money_spent.isdigit() and money_wants.isdigit() and popularity_online.isdigit():
            money = (int(money_have) - int(money_spent)) - int(money_wants)
            return render_template('komplikator_result.html', complexity = overall_score(int(age), int(gender), int(status), int(ignorance), money, int(popularity_online), int(rl_friends)))
        else:
            return render_template('komplikator_error.html', message = "Age, Ignorance, Money have, Money wants, Money spent and Klout score must be digits without special signs!")
    else:
        return render_template('komplikator_form.html')

if __name__ == "__main__":
    app.run(debug = True)