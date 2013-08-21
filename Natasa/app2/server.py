from flask import Flask, render_template
#render template bo vzel te nase template in jih zdruzil

app = Flask(__name__)
#ko bomo poklicali app kr direktno v root --> "/" dobimo tole
@app.route('/')
def home():
	return render_template("home.html")
#povemo naj zrendrira template in povemo tud kterga

@app.route('/demo')
def demo():
	return render_template("demo.html")

@app.route('/about')
def about():
	return render_template("about.html")



if __name__ == '__main__':
	app.run(debug=True)
#to damo potem stran ko damo na server ker pokaze vse napake - v namen debugginga
