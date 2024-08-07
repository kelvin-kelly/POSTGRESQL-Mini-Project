
# supa_pass = ('SUPABBASEsupabase')

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate()


db = SQLAlchemy(app)

migrate.init_app(app,db)

class Register(db.Model):
    __tablename__ = 'reg'
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    pet = db.Column(db.String(40))
    
    def __init__(self, fname, lname, pet):
        self.fname = fname
        self.lname = lname
        self.pet = pet
        

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods = ['GET' , 'POST'])
def submit():
    
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        pet = request.form['pet']
        
        reg = Register(fname, lname, pet)
        db.session.add(reg)
        db.session.commit()
        
        regResult = db.session.query(Register).filter(Register.id ==1)
        for result in regResult :
            print(result.fname)
            
    return render_template('success.html', data = fname)

if __name__ == '__main__':
    app.run(debug=True)
