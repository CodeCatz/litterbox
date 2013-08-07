from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/demo')
def demo():
		return  render_template ('demo.html')
		

@app.route('/test')
def test():
		return "this is just a test"


@app.route('/')
def home(): 
		return render_template('home.html')
	
if __name__ == '__main__':
		app.run(debug=True)
		
