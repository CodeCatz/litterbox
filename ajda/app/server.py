from flask import Flask, render_template

app = Flask(__name__) #dva podcrtaja skupaj 2x

@app.route('/test')
def test():
	return "this is just as test"


@app.route('/') #to pomeni, ce v browserju vpisemo "http://127.0.0.1:5000/" brez kaksnega dela za tem URL-jem nam pozene index
def home():
	return render_template('home.html')


@app.route('/demo')
def demo():
	return render_template('demo.html')



#vse funkcije moras definirat pred tem delom if __name__ ...
if __name__ == '__main__':
	app.run(debug=True) #debug=true --> napisemo,da se mora app zagnat v nacinu, da nam pove vse napake

