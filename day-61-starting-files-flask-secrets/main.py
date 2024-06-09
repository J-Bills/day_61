from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired,Email,Length
from flask_wtf.csrf import CSRFProtect


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class loginForm(FlaskForm):
    password = fields.PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message='password too short')])
    email = fields.StringField(label='Email', validators=[DataRequired(), Email()])
    submit = fields.SubmitField(label='Log in')
    


app = Flask(__name__)
app.secret_key = "randomjunk"
csrf = CSRFProtect(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'password':
            print('succ')
            return render_template('success.html')
        else:
            print('fail')
            return render_template('denied.html')
    return render_template('login.html', form=form)

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
