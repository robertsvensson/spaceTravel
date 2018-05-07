from flask import Flask, render_template
from flaskext.markdown import Markdown

import getGeneralInformation
import getExosphereInstruction
import getSpacemap
import getFanMessageContent
import sendFanMessage

app = Flask(__name__)

Markdown(app)

@app.route('/')
def hello_space():
    space_crew_info = getGeneralInformation.getGeneralInformation()
    return render_template('index.html', space_crew_info = space_crew_info)

@app.route('/exosphere/<username>')
def exosphereInfo(username):
    localized_instruction = getExosphereInstruction.getExosphereInstruction(username)
    return render_template('exosphere.html', localized_instruction = localized_instruction)

@app.route('/spacemap')
def showSpacemap():
    spacemap = getSpacemap.getSpacemap()
    return render_template('spacemap.html', spacemap = spacemap)

@app.route('/fanmessage')
def sendMessageToFans():
    fan_message = getFanMessageContent.getFanMessageContent()
    send_fan_message_to_space_fans = sendFanMessage.sendFanMessage(fan_message)
    return 'nothing'
