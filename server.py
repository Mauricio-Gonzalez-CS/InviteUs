from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import os


app = Flask(__name__)


@app.route('/')
def layout():
   return render_template('home.html')   

@app.route('/details-draft')
def details():
   return render_template('details-draft.html')  

@app.route('/theme')
def theme():
   return render_template('theme.html')

@app.route('/theme-draft')
def themeDraft():
   return render_template('theme-draft.html')

@app.route('/add-info')
def add():
   return render_template('add-info.html')

@app.route('/add-info-draft')
def addDraft():
   return render_template('add-info-draft.html')

@app.route('/correction-or-add')
def addOrCorrect():
   return render_template('correction-or-add.html')

@app.route('/desc-add-draft')
def descAdd():
   return render_template('desc-add-draft.html')

@app.route('/desc-correct-draft')
def descCorrect():
   return render_template('desc-correct-draft.html')

if __name__ == '__main__':
    app.run(debug= True)