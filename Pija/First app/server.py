from flask import Flask, request, render_template
from calculator_new import total_calc, check_level, interpret_score

app = Flask(__name__)

@app.route('/complicator', methods=['GET', 'POST'])
def komplikator():
	if request.method == 'POST':
		have_error = False
		gender = request.form['gender']
		age = request.form['age']
		status = request.form['status']
		ignorance = request.form['ignorance']
		money_have = request.form['money_have']
		money_wants = request.form['money_wants']
		popularity_online = request.form['popularity_online']
		rl_friends = request.form['rl_friends']
		nick = request.form['type_name']

		errors = dict(name = nick,
						age = age,
						ignorance = ignorance,
						money_have = money_have,
						money_wants = money_wants,
						popularity_online = popularity_online,
						rl_friends = rl_friends)

		if nick.isdigit():
			errors['error_name'] = "Name should consist of letters only."
			have_error = True

		if not age.isdigit():
			errors['error_age'] = "Age should be a whole number, written with digits!"
			have_error = True
		
		#if age.isdigit() > 120:
			#errors['error_age'] = "Aren't you dead already? ;P Please type in your real age."
			#have_error = True

		if not ignorance.isdigit():
			errors['error_ignorance'] = "Estimate your ignorance on a scale from 0 to 100."
			have_error = True

		if not money_have.isdigit():
			errors['error_money_have'] = "Estimate the amount you currently have with numbers."
			have_error = True

		if not money_wants.isdigit():
			errors['error_money_wants'] = "Estimate the amount you currently want with numbers."

		if not popularity_online.isdigit():
			errors['error_pop_online'] = "Estimate the amount of friends you have on FB or/and Twitter with numbers."
			have_error = True

		if not rl_friends.isdigit():
			errors['error_rl_friends'] = "Estimate the amount of friends you have in real life with numbers."
			have_error = True

		if have_error:
			return render_template('calc_p2.html', **errors)
		else:
		#if age.isdigit() and ignorance.isdigit() and money_have.isdigit() and money_wants.isdigit() and popularity_online.isdigit() and rl_friends.isdigit():
			score = total_calc(int(age), int(gender), int(status), int(ignorance), int(money_have), int(money_wants), int(popularity_online), int(rl_friends))
			return render_template('komplikator_result.html', name = nick, complexity = score, level = check_level(score), message = interpret_score(score))
		#else:
			#return render_template('komplikator_error.html', message = "You have to type in numbers without any special signs ;)")
	else:
		return render_template('calc_p2.html')


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/test')
def test():
	return "this is just a test"

@app.route('/demo')
def demo():
	return render_template('demo.html')

@app.route('/sandbox')
def sandbox():
	return render_template('sandbox.html')

@app.route('/calc_p2')
def calc_p2():
	return render_template('calc_p2.html')

@app.route('/newstuff')
def newstuff():
	return render_template('newstuff.html')

if __name__ =='__main__':
	app.run(debug = True)