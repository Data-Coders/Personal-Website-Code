from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import datetime
import json
userr  = 0
yo =1

with open('config.json', 'r') as c:
    params = json.load(c)['params']

app = Flask(__name__)
app.secret_key = 'I am Alex Mercer'
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['guser'],
    MAIL_PASSWORD=params['gpass']
)
mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/root'
db = SQLAlchemy(app)


class Contact(db.Model):
    '''sno, msg, phno, name, last, email, subject, date, month'''
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(80), nullable=False)
    phno = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    last = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=False)
    month = db.Column(db.String(120), nullable=True)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(220), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    img_file = db.Column(db.String(20), nullable=True)
    posted = db.Column(db.String(20), nullable = True)


class Users(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(220), nullable=False)
    gender = db.Column(db.String(20), nullable=True)
    contri = db.Column(db.String(20), nullable=True)

@app.route('/')
def hello_world():
    if 'user' in session:
        nonlogin = 'LogOut'
        form = 'Logout'
    else:
        nonlogin = 'member'
        form = 'Login'
    return render_template('index.html', params=params, form=form, nonlogin=nonlogin)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if 'user' in session:
        nonlogin = 'LogOut'
        form = 'Logout'
    else:
        nonlogin = 'member'
        form = 'Login'
    if request.method == 'POST':
        msg = request.form.get('message')
        phno = request.form.get('phno')
        name = request.form.get('name')
        last = request.form.get('last')
        email = request.form.get('email')
        subject = request.form.get('subject')
        date = datetime.datetime.now()
        entry = Contact(msg=msg, phno=phno, name=name, last=last, email=email, subject=subject, date=date)
        db.session.add(entry)
        db.session.commit()
        mail.send_message(name + ' is trying to Contact you via your Website',
                          sender=email,
                          recipients=[params['guser']],
                          body=msg + '\nPhone Number = ' + phno)

    return render_template('contact.html', params=params, form=form, nonlogin=nonlogin)


@app.route('/service')
def service():
    if 'user' in session:
        nonlogin = 'LogOut'
        form = 'Logout'
    else:
        nonlogin = 'member'
        form = 'Login'
    return render_template('service.html', params=params, form=form, nonlogin=nonlogin)


@app.route("/post/<string:post_slug>", methods=['GET'])
def postblog(post_slug):
    if 'user' in session:
        nonlogin = 'LogOut'
        form = 'Logout'
    else:
        nonlogin = 'member'
        form = 'Login'
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', post=post, params=params, form=form, nonlogin=nonlogin)


@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def editing(sno):
    if sno == '0':
        val = 'Add'
    elif sno > '0':
        val = 'Edit'
    if 'user' in session:
        nonlogin = 'LogOut'
        form = 'Logout'
    else:
        nonlogin = 'member'
        form = 'Login'

    if request.method == 'POST':
        req_title = request.form.get('tit')
        req_slug = request.form.get('slu')
        req_content = request.form.get('cont')
        req_imgfle = request.form.get('fi')
        date = datetime.datetime.now()
        poste = session['user']

        if sno == '0':
            post = Posts(title=req_title, slug=req_slug, content=req_content, date=date, img_file=req_imgfle, posted=poste)
            print(poste)
            db.session.add(post)
            db.session.commit()
        else:
            post = Posts.query.filter_by(srno=sno).first()
            post.title = req_title
            post.slug = req_slug
            post.content = req_content
            post.imgfile = req_imgfle
            post.date = date
            db.session.commit()
    post = Posts.query.filter_by(sno=sno).first()
    return render_template('edit.html', params=params, post=post, sno=sno, val=val, form=form, nonlogin=nonlogin)

@app.route('/edit/blog')
def velle():
    redirect('/blog')

@app.route('/check')
def checkc():
    if 'user' in session:
        print(session['user'])
        return redirect('/edit/0')
    else:
        return redirect('/member')

@app.route('/logout')
def logout():
    session.pop('user')
    global userr
    userr = 0
    print(userr)
    return redirect('/')

@app.route('/LogOut')
def memlogout():
    session.pop('user')
    return redirect('/')


@app.route('/portfolio')
def portfolio():
    if 'user' in session:
        nonlogin = 'LogOut'
        form = 'Logout'
    else:
        nonlogin = 'member'
        form = 'Login'
    return render_template('portfolio.html', params=params, form=form, nonlogin=nonlogin)


@app.route('/about')
def about():
    if 'user' in session:
        nonlogin = 'LogOut'
        form = 'Logout'
    else:
        nonlogin = 'member'
        form = 'Login'
    return render_template('about.html', params=params, form=form, nonlogin=nonlogin)

@app.route('/dashboard')
def user_dashboard():
    if 'user' in session:
        nonlogin = 'LogOut'
        form = 'Logout'
        sno = Posts.query.order_by(-Posts.sno).first()
        posts = Posts.query.filter_by(posted=session['user'])
        print(userr)
        return render_template('user_dashboard.html', params=params, posts=posts, form=form, nonlogin=nonlogin, sno=sno)
    else:
        return render_template('member.html', params=params)

@app.errorhandler(500)
def internal_error(error):
    return render_template('404.html')


@app.route('/blog')
def blog():
    if 'user' in session:
        nonlogin = 'LogOut'
        form = 'Logout'
    else:
        nonlogin = 'member'
        form  = 'Login'
    posts = Posts.query.filter_by().all()[-3:]
    return render_template('blog.html', params=params, posts=posts, form=form, nonlogin=nonlogin)

@app.route('/offer')
def offers():
    return render_template('offer.html', params=params)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        usr = request.form.get('usrnme')
        psd = request.form.get('psswdd')
        emai = request.form.get('emai')
        ne = Users(username=usr, password = psd, email=emai)
        db.session.add(ne)
        db.session.commit()

        nonlogin = 'LogOut'
        form = 'Logout'
        session['user'] = usr
        global userr
        userr = userr + 1
        return render_template('index.html', params=params, form=form, nonlogin=nonlogin, user=userr)

    return render_template('userlogin.html', params=params)


@app.route('/login', methods=['GET', 'POST'])
def adminlog():
    global userr
    if 'user' in session and session['user'] == params['admin']:
        posts = Posts.query.filter_by().all()
        sno = Posts.query.order_by(-Posts.sno).first()
        print(userr)
        return render_template('dashboard.html', params=params, posts=posts, sno=sno,  user=userr)

    if request.method == 'POST':
        username = request.form.get('usrnme')
        password = request.form.get('psswdd')
        if username == params['admin'] and password == params['adminpass']:
            session['user'] = username
            posts = Posts.query.filter_by().all()
            sno = Posts.query.order_by(-Posts.sno).first()
            return render_template('dashboard.html', params=params, posts=posts, sno=sno, user=userr)
    else:
        return render_template('login.html', params=params)

    return render_template('login.html', params=params)

@app.route('/adminlogs')
def adminlogs():
    posts = Posts.query.filter_by().all()
    form = 'Logout'
    nonlogin = 'logout'
    return render_template('admin.html', params=params, posts=posts, form=form, nonlogin=nonlogin)

@app.route('/userlogs', methods=['GET', 'POST'])
def userposts():
    text='userlogs'
    if request.method == 'POST':
        usernme = request.form.get('usrnme')
        passwd = request.form.get('psswdd')
        usr = Users.query.filter_by(username=usernme).first()
        if (usr):
            if (usr.password == passwd):
                session['user'] = usernme
                form = 'Logout'
                nonlogin = 'LogOut'
                posts = Posts.query.filter_by(posted=usernme).all()
                return render_template('userlogs.html', params=params, form=form, nonlogin=nonlogin, posts=posts, text=text, user=usernme)
            else:
                msg =  'Password is Incorrect'
                return render_template('forusername.html', params=params, msg=msg, text=text)
        else:
            msg = 'UserName Is Incorrect'
            return render_template('forusername.html', params=params, msg=msg, text=text)
    msg = 'Enter Your Credentials'
    return render_template('forusername.html', params=params, msg = msg, text=text)


@app.route('/member', methods = ['GET', 'POST'])
def member():
    text='member'
    if request.method == 'POST':
        usernme = request.form.get('usrnme')
        passwd = request.form.get('psswdd')
        usr = Users.query.filter_by(username=usernme).first()
        if (usr):
            if (usr.password == passwd):
                session['user'] = usernme
                form = 'Logout'
                nonlogin = 'LogOut'
                return render_template('index.html', params=params, form=form, nonlogin=nonlogin)
            else:
                msg = 'Password is Incorrect'
                return render_template('member.html', params=params, msg=msg,text=text)
        else:
            msg = 'UserName Is Incorrect'
            return render_template('member.html', params=params, msg=msg, text=text)
    msg = 'Enter Your Credentials'
    return render_template('member.html', params=params, msg=msg, text=text)

app.run()
