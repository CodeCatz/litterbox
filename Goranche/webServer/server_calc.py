from calculator_new import complexity_calc
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def calculator_new():
	if request.method == 'POST':
		gender = request.form['spol']
        age = request.form['age']
        status = request.form['relationship_status']
        ignorance = request.form['points']
        money_have = request.form['money_have']
        money_want = request.form['money_want']
        klaut = request.form['fbfriends']
        rl_friends = request.form['rlfriends']


  		if age.isdigit():
            if gender == "male" or gender == "female":
            	if status == "single" or status == "in relationship" or status == "in open relationship" or status == "it's complicated" or status == "I'm a pizza" or status == "depends":
            		if money_have.isdigit():
            			if money_want.isdigit():
            				if klaut.isdigit():
            					if rlfriends.isdigit():
                					return render_template('komplikator_result.html', complexity = complexity_calc(gender, int(age), status, ignorance, int(money_have), int(money_want), klaut, rl_friends)))
           						else:
                					return render_template('komplikator_error.html', message = "spol ni pravilen!")
        					else:
            					return render_template('komplikator_error.html', message = "starost mora biti stevilka!")
    					else:
        					return render_template('calculator.html')

if __name__ == "__main__":
    app.run(debug = True)