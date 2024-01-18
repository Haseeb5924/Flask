from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///delegates.db'
db = SQLAlchemy(app)

class Delegate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    ambassador = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    preference1 = db.Column(db.String(100), nullable=False)
    preference2 = db.Column(db.String(100), nullable=False)
    observer = db.Column(db.String(3), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_delegate = Delegate(
            name=request.form['name'],
            picture=request.form['picture'],
            email=request.form['email'],
            phone=request.form['phone'],
            city=request.form['city'],
            school=request.form['school'],
            ambassador=request.form['ambassador'],
            grade=request.form['grade'],
            preference1=request.form['preference1'],
            preference2=request.form['preference2'],
            observer=request.form['observer']
        )

        db.session.add(new_delegate)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
