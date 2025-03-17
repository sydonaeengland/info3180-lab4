from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed
from wtforms import FileField, SubmitField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    file = FileField("Upload File", validators=[
        InputRequired(),
        FileAllowed(['jpg', 'png'], "Only JPG and PNG images are allowed!")  
    ])
    submit = SubmitField("Upload")