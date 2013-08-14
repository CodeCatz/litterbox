from calculator_new import complexity_calc
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
        popularity_online = request.form['popularity_online']
        rl_friends = request.form['rl_friends']

        if gender == "male" or gender == "female":
            if age.isdigit() and ignorance.isdigit() and money_have.isdigit() and money_wants.isdigit() and popularity_online.isdigit() and rl_friends.isdigit():
                return render_template('komplikator_result.html', complexity = complexity_calc(gender, int(age), int(status), int(ignorance), int(money_have), int(money_wants) int(popularity_online), int(rl_friends)))
            else:
                return render_template('komplikator_error.html', message = "Age, Ignorance, Money have, Money wants, Popularity online and Real life friends score must be digits!")
        else:
            return render_template('calculator.html')

if __name__ == "__main__":
    app.run(debug = True)


  		
        """    if gender == "male" or gender == "female":
            	if status == "single" or status == "in relationship" or status == "in open relationship" or status == "it's complicated" or status == "I'm a pizza" or status == "depends":
            		
                					return render_template('komplikator_result.html', complexity = complexity_calc(gender, int(age), status, ignorance, int(money_have), int(money_want), klaut, rl_friends)))
           						else:
                					return render_template('komplikator_error.html', message = "spol ni pravilen!")
        					else:
            					return render_template('komplikator_error.html', message = "starost mora biti stevilka!")
    					else:
        					return render_template('calculator.html') """

