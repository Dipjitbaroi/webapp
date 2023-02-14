from flask import Flask, render_template, url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '2001582bed503f7dd7b38a98832de733'
posts = [
    {
        'author': 'Dip Jit Baroi',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Feb 05,2023'
    },
    {
        'author': 'Abul Basar',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'Feb 06,2023'
    }
]

@app.route('/')
# def empty():
#     return '<h1>This is khailla page</h1>'

@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    form1 = RegistrationForm()
    return render_template('register.html',title='Register',form=form1)

@app.route('/login')
def login():
    form2 = LoginForm()
    return render_template('login.html',title='Login',form=form2)

if __name__ == '__main__':
    app.run(debug=True)
