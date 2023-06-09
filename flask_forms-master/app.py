from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///form.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='ad93fd6444102555b147adbb803ad13d'
db=SQLAlchemy(app)
app.app_context().push()

class info(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    subject=db.Column(db.String(50), nullable=False)
    message=db.Column(db.String(200))


@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    form = RegistrationForm()
    if request.method=='POST':
        name = form.name.data
        email = form.email.data
        sub  = form.subject.data
        mes = form.message.data
        post1 =info(name=name, email=email, subject=sub, message=mes)
        db.session.add(post1)
        db.session.commit()
        return redirect(url_for('submission'))
    
    return render_template('index.html', form=form)

@app.route('/submission')
def submission():
    return render_template('done.html')


if __name__ == "__main__":
    app.run(debug=True)