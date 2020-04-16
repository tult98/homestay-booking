from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SingupForm(FlaskForm):
    email = StringField('Địa chỉ email', validators=[DataRequired(), Email(), Length(max=255)])
    phone_number = StringField("Số điện thoại", validators=[
                               DataRequired(), Length(max=255)])
    first_name = StringField(
        "Tên", validators=[DataRequired(), Length(max=255)])
    last_name = StringField("Họ và tên đệm", validators=[
                            DataRequired(), Length(max=255)])
    password1 = PasswordField("Mật khẩu", validators=[
                              DataRequired()])
    password2 = PasswordField("Xác nhận mật khẩu mới", validators=[
                              DataRequired(), EqualTo('password1')])
    submit = SubmitField('Đăng kí')

class SigninForm(FlaskForm):
    email = StringField('Địa chỉ email', validators=[
                        DataRequired(), Email(), Length(max=255)])
    password = PasswordField("Mật khẩu", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Đăng nhập")
