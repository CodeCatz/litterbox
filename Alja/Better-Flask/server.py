from flask import Flask, request, render_template
from complicator import overall_score, check_level

app = Flask(__name__)


# just a simple test page
@app.route('/test')
def test():
	return "This is just a test."

@app.route('/cats')
def cats():
	return render_template('cats.html')

@app.route('/hipster')
def hipster():
	return render_template('hipster.html')

@app.route('/grumpy')
def grumpy():
	return render_template('grumpy.html')

@app.route('/faq')
def faq():
	return render_template('faq.html')

@app.route('/moar')
def moar():
	return render_template('moar.html')

@app.route("/complicator", methods=['GET', 'POST'])
def complicator():
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
            score = overall_score(int(age), int(gender), int(status), int(ignorance), money, int(popularity_online), int(rl_friends))
            return render_template('complicator_result.html', complexity = score, level = check_level(score))
        else:
            return render_template('complicator_error.html', message = "Age, Ignorance, Money have, Money wants, Money spent and Klout score must be digits without special signs!")
    else:
        return render_template('complicator_form.html')

# defining root page
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

