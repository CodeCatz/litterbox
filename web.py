from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('test.html', name="Metallica")

@app.route('/post', methods=['POST'])
def post_test():
	return request.form['test']

if __name__ == "__main__":
    app.run(debug=True)
