from homestay import app, bcrypt, db
from flask import render_template, url_for, flash, redirect
from .forms import SigninForm, SingupForm


#pylint:disable=E1101

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')



# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     pass
    # form = SingupForm()
    # if form.validate_on_submit():
    #     # create hashed password 
    #     id = str(uuid.uuid4())
    #     first_name = form.first_name.data
    #     last_name = form.last_name.data
    #     phone_number = form.phone_number
    #     email = form.email.data
    #     hashed_password = bcrypt.generate_password_hash(form.password1.data).decode('utf-8')
        # user = User(id=id, email=email, hash_password=hashed_password)
        # user.user_profile = UserProfile(phone_number=phone_number)
        # user_profile = UserProfile(
        #     user_id=id, first_name=first_name, last_name=last_name, phone_number=phone_number)
        
        # print(user)
        # db.session.add(user)
        # db.session.add(user_profile)
    #     db.session.commit()
    #     flash(f'Tài khoản của bạn đã tạo thành công! Có thể đăng nhập', 'success')
    #     return redirect(url_for('signin'))
    # return render_template('signup.html', title='Đăng kí', form=form)

# @app.route('/signin', methods=['GET', 'POST'])
# def signin():
#     form = SigninForm()
#     return render_template('signin.html',title='Đăng nhập', form=form)
