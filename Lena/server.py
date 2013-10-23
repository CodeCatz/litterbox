from kalkulator import calculate_score
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def komplikator():
    if request.method == 'POST':
        gender = request.form['spol']
        age = request.form['age']
        if age.isdigit():
            if gender == "male" or gender == "female":
                return render_template('komplikator_result.html', complexity = calculate_score(gender, int(age)))
            else:
                return render_template('komplikator_error.html', message = "spol ni pravilen!")
        else:
            return render_template('komplikator_error.html', message = "starost mora biti stevilka!")
    else:
        return render_template('komplikator_form.html')

if __name__ == "__main__":
    app.run(debug = True)