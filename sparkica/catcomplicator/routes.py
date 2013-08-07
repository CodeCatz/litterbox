from flask import Flask, render_template, request
from catcomplexity import calculate_score

app = Flask(__name__)

@app.route('/complicate', methods=['GET', 'POST'])
def get_catcomplexity_score():
	if request.method == 'POST':
		gender = request.form['gender']
		age = request.form['age']
		return render_template('catcomp_result.html', complexity = calculate_score(gender, int(age)))

	return render_template('catcomp.html')


@app.route('/')
def home():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)