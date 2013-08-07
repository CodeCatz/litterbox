from flask import Flask, render_template

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

# defining root page
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

