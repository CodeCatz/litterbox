from flask import Flask, render_template

app = Flask(__name__)

@app.route('/sandbox')
def sandbox():
	return render_template('sandbox.html')

@app.route('/demo')
def demo():
	return render_template('demo.html')

@app.route('/calc_p2')
def calc_p2():
	return render_template('calc_p2.html')

@app.route('/test')
def test():
	return "this is just a test"

@app.route('/')
def home():
	return render_template('home.html')

if __name__ =='__main__':
	app.run(debug = True)