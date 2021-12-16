from app import app
from flask import render_template, redirect, request, make_response
from app.forms import TerminalMacrosForm, NewFileForm, PlayTest
from app.commandToTerminal import commandToTerminal


button_terminal = {'Pause': 'Pause', 'V+': 'F9', 'V-': 'F8','+' : 'F7',
                   '-': 'F6', 'Up': 'Up', 'Left': 'Left', 'Down': 'Down',
                   'Right': 'Right', 'Ok': 'Return', 'Home': 'F4', 'Back': 'Escape',
                   'Save': 'F12', 'Call': 'F1', 'Dell': 'BackSpace', 'Off': 'F2',
                   '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
                   '7': '7', '8': '8', '9': '9', '0': '0', '.*': 'Dot', '#@': 'Dog',
                   'pc': 'F5', 'far/near': 'ScrollLock', 'layout': 'F10', 'MicOff': 'F3', 'Sys': 'sys',
                   'focus': 'focus', 'SaveIp': 'SaveIp'}


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/terminal')
def terminal():
    form = TerminalMacrosForm()
    form.set_ip_terminal()
    form2 = NewFileForm()
    form3 = PlayTest()
    form3.load_test_in_select()
    return render_template('macros_page.html', form=form, form2=form2, form3=form3)


@app.route('/click',  methods=['POST'])
def click():
    command = (request.form.to_dict()).popitem()[1]
    command = button_terminal[command]
    return commandToTerminal(command)
