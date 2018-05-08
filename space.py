from flask import Flask, render_template
from flaskext.markdown import Markdown

import get_general_information
import get_exosphere_instruction
import get_spacemap
import get_fan_message_content
import send_fan_message

app = Flask(__name__)

Markdown(app)

@app.route('/')
def hello_space():
    space_crew_info = get_general_information.get_general_information()
    return render_template('index.html', space_crew_info = space_crew_info)

@app.route('/exosphere/<username>')
def exosphere_info(username):
    localized_instruction = get_exosphere_instruction.get_exosphere_instruction(username)
    return render_template('exosphere.html', localized_instruction = localized_instruction)

@app.route('/spacemap')
def show_spacemap():
    spacemap = get_spacemap.get_spacemap()
    return render_template('spacemap.html', spacemap = spacemap)

@app.route('/fanmessage')
def send_message_to_fans():
    fan_message = get_fan_message_content.get_fan_message_content()
    send_fan_message_to_space_fans = send_fan_message.send_fan_message(fan_message)
    return 'nothing'
