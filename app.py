from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

class SampleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form_page():
    form = SampleForm()
    if form.validate_on_submit():
        # Process form data here
        return redirect(url_for('home'))
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)