from crypt import methods
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import os
!pip install openai
import openai
import ipywidgets as widgets
import textwrap as tw
import re
openai.api_key = "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"


app = Flask(__name__)

invitation = ""

def gpt3_invite_update(prompt):
  global invitation
  completion = openai.Completion.create(engine="text-davinci-002", max_tokens=256, prompt=prompt)
  r = re.split('\n', completion.choices[0].text.strip())
  print("the prompt was: ", prompt)
  print("the result was:", r[0])
  invitation = r[0]

def basic_invitation(date=None, time=None, location=None):
  prompt = "Create a basic invitation for an event "
  if date:
    prompt += "happening on " + date + " "
  if location:
    prompt += "happening at " + location + ". "
  if time:
    prompt += "at " + time 
  gpt3_invite_update(prompt)

def correction(c):
  global invitation
  prompt = f"rewrite the inviation '{invitation}' with these changes '{c}'"
  gpt3_invite_update(prompt)

def context(event_type = None, tone = None, theme=None):
  global invitation
  prompt = "rewrite the invitation '" + invitation + "' "
  if event_type:
    prompt += "with the event being " + event_type + ". "
  if tone:
    prompt += "Make the invite have a tone of " + tone
  if theme:
    prompt += "and make the invite " + theme + " themed."
  gpt3_invite_update(prompt)

def additional_info(info):
  global invitation
  prompt = f"rewrite the invitation '{invitation}' with this additional information '{info}'"
  gpt3_invite_update(prompt)


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

#AJAX functions
@app.route('/basic', methods=["POST"])
def basic():
   global invitation
   json_data = request.get_json() 
   #assumes only get date, location, time if the user inputred something, 
   #when working on javascript we might decide to change this
   d = None
   if "date" in json_data:
      d = json_data["date"]
   t = None
   if "time" in json_data:
      t = json_data["time"]
   if "location" in json_data:
      l = json_data["location"]
   basic_invitation(date=d, time=t,location=l)
   return jsonify(invitation = invitation)


if __name__ == '__main__':
    app.run(debug= True)