from flask import Flask, redirect, render_template,request, url_for
from form import HealthDataForm
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///health_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class HealthData(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date = db.Column(db.Date, nullable=False)
    exercise = db.Column(db.Integer, nullable=False)
    meditation = db.Column(db.Integer, nullable=False)
    sleep = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<HealthData {self.id}>'


#define homepage route and index() view function
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form',methods=['POST','GET'])
def form():
    form=HealthDataForm()
    if form.validate_on_submit():
        new_data=HealthData(
            date=form.date.data,
            exercise=form.exercise.data,
            sleep=form.sleep.data,
            meditation=form.meditation.data
        )
        
        db.session.add(new_data)
        db.session.commit()    
        
        return redirect(url_for('dashboard'))
    return render_template('form.html',form=form)
   
@app.route('/dashboard')
def dashboard():
    
    all_data=HealthData.query.all()
    return render_template('dashboard.html',data=all_data)

#run the app in debug mode
if __name__== '__main__':
    app.run(debug=True)