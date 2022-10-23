from flask import Flask, render_template
import os
import hmodule as hmodule
from wtforms import Form, StringField,SubmitField,SelectField
from flask_wtf import FlaskForm
import pickle
import numpy as np
import joblib
meta = joblib.load('MetaModelFifa_predictors.mdl')
app = Flask(__name__)
app.secret_key = os.urandom(24)

class Form(FlaskForm):
    home_team = SelectField('home_team', choices=meta['country'])
    away_team = SelectField('away_team', choices=meta['country'])
    submit = SubmitField("submit")


@app.route('/',methods=['GET', 'POST'])
def index():
    fname = None
    lname = None
    winner=None
    form = Form()
    if form.validate_on_submit():
        home_team=form.home_team.data
        away_team=form.away_team.data
        match=hmodule.get_match(home_team, away_team,meta['predictors'] ,meta['xcols'] )
       # features = features.astype(np.float)
        print(meta['name'])
        pred= meta['model'].predict(match)[0]
        print(pred)
        if pred=='home_lose':
            winner=away_team
            return render_template('winner.html',winner=winner)

        elif pred=='draw':
            winner = "NO winner results is draw"
            return render_template('winner.html',winner=winner)

        else:
            winner=home_team
            return render_template('winner.html',winner=winner)
    return render_template('home.html',fname=fname,lname=lname,form=form)


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

