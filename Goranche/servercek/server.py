from flask import Flask, render_template

app = Flask(__name__)

# just another page
@app.route('/demo')
def test():
    return render_template('demo.html')

# defining root page
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
