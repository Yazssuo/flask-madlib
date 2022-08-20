from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "this-is-a-key"

debug = DebugToolbarExtension(app)

@app.route('/form')
def make_form():
    return render_template('form.html', prompts=story.prompts)

@app.route('/story')
def make_story():
    return render_template('story.html', gen_story=story.generate(request.args))