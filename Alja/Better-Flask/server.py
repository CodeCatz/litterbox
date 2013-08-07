from flask import Flask, render_template

app = Flask(__name__)


# just another test page
@app.route('/test')
def test():
	return "This is just a test."

@app.route('/cats')
def demo():
	return render_template('cats.html')


# defining root page
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

