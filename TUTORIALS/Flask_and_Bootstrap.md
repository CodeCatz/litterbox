# Flask and Bootstrap are awesome

### Step 1: install Flask 

[Flask](http://flask.pocoo.org) is a lightweight framework for Python web apps.

To install it, just run `pip install flask` in your Terminal.

### Step 2: create basic folders for your new app

Create a new directory with your app's name with two subdirectories:

		app/	
			templates/  # will be used for content files
			static/		# will be used for images and other stuff that doesn't really change that often

### Step 3: create a basic web app with Flask

Create a file called `server.py` in you main project folder (`app/`):

---

	from flask import Flask, render_template

	app = Flask(__name__)
	
	@app.route('/')
	def index():
		return "Hi there!"
	
	if __name__ == '__main__':
		app.run(debug=True)
	
---

From Terminal, run `server.py` with python (`python server.py`). Make sure you're in the right directory.

Open `http://localhost:5000` in your browser to see your web app.

You can add other app routes. For example:

	@app.route('/test')
	def test():
		return "This is just a test" 

### Step 4: create a basic template for your web app

Create a basic HTML file. Call it `base.html`, save it in your `templates/ folder`.

	<!DOCTYPE html>
	<html>
		<head>
			<title>My fancy new app</title>
		</head>
		<body>
		<h1>This is a big heading</h1>
	
		<div class="container">
			{% block content %}
			{% endblock %}
		</div>
	
		</body>
	</html>

### Step 5: create some other templates

Now that you have your base, you can create html files with content for each page of your web app. You'll need a starting page first. Create a file named `index.html` in your `templates` folder:

	{% extends "base.html" %}
	{% block content %}
	<p>Hello world.</p>
	{% endblock %}

Now tell your `server.py` page to render this template:

	@app.route('/')
	def index():
		return render_template('index.html')

Rinse and repeat for every page you want to add. Create more files in your `templates` folder with names like: `page_name.html`, following the structure of `index.html`. When you're done, don't forget to tell `server.py` how you want your app to route. Example:

	@app.route('/page_name')
	def page_name():
		return render_template('page_name.html')

Hint: your new page name appears three times in the code above. Don't forget to change all references when adding a new page.

### Step 6: add Boostrap for a better look

Want your web app to look better without much effort? Download [Bootstrap](http://getbootstrap.com). Unzip. Rename directory to `bootstrap`, move it to folder `app/static`.

Edit your `base.html` again; you have to tell our basic template where your CSS file is located and we're also adding the meta viewport tag to make the web app behave well on mobile devices:

	<!DOCTYPE html>
	<html>
		<head>
			<meta name="viewport" content="width=device-width, initial-scale=1.0">

			<link href="{{ url_for('.static', filename='bootstrap/css/bootstrap.css') }}" rel="stylesheet" />

			<title>Beautiful web</title>
		</head>

### Step 7: explore Bootstrap

[Bootstrap CSS documentation](http://getbootstrap.com/css/) is your new best friend.

Some cool things you can do:

- Use the [grid system](http://getbootstrap.com/css/#grid) to create rows with div boxes taking up to 12 columns per row. For instance, you can have a row with just one large box:

	`<div class="row">
        <div class="col-lg-12">Some content</div>
	</div>`

- A row divided in half with two boxes:

	`<div class="row">
		<div class="col-lg-6">First half</div>
		<div class="col-lg-6">Second half</div>
	</div>`

- … and [much more](http://examples.getbootstrap.com/grid/). 

- Add a cool looking [navigation bar](http://getbootstrap.com/components/#navbar) on top of every page. 

### Step 8: add JavaScript from Bootstrap

To make the page even more awesome and dynamic, you can also use Bootstrap's JavaScript. Add the following code right before your ending `</body>` tag in `base.html`:

	<script src="{{ url_for('.static', filename='bootstrap/js/bootstrap.js') }}"></script>

And you'll also need to [download jquery](http://jquery.com/download/). Create a `js` folder in `app/static` and move the downloaded `jquery-1.10.2.min.js` in there. In `base.html`, add this line before the Bootstrap JavaScript tag:

	<script src="{{ url_for('.static', filename='js/jquery-1.10.2.min.js') }}"></script>

The final lines of your `base.html` should now look like this:

		<script src="{{ url_for('.static', filename='js/jquery-1.10.2.min.js') }}"></script>
		<script src="{{ url_for('.static', filename='bootstrap/js/bootstrap.js') }}"></script>
	
		</body>
	</html>

### Step 9: play with Bootstrap's jquery plugins

Take a look at available [jquery plugins](http://getbootstrap.com/javascript/). Choose one, copy the example code and have fun with it!

### Step 10: custom CSS

Want to change the size of paragraphs, the color of a class or something else? Add your own custom CSS to override Bootstrap's defaults. Create a `css` folder in `app/static` and a new, blank `custom.css` file. Add any custom CSS definition:

	p {
		color:#FF40FF;
	}

Edit `base.html` and add the following link to your custom CSS file after the link to Bootstrap's CSS in the `<head>` part of the file:

	<link href="{{ url_for('.static', filename='css/custom.css') }}" rel="stylesheet" />

### What next?

Make it pretty, play with it, have fun!
