from app import app
from flask import render_template, redirect, request
from app.forms import TerminalMacrosForm
import paramiko
import time

button_terminal = {'Pause': 'Pause','V+': 'F9', 'V-': 'F8','+' : 'F7',
                   '-': 'F6', 'Up': 'Up', 'Left': 'Left', 'Down': 'Down',
                   'Right': 'Right', 'Ok': 'Return', 'Home': 'F4','Back': 'Escape',
                   'Save': 'F12', 'Call': 'F1', 'Dell': 'BackSpace','Off': 'F2',
                   '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
                   '7': '7', '8': '8', '9': '9', '0': '0', '.*': 'Dot', '#@': 'Dog',
                   'pc': 'F5', 'far/near': 'ScrollLock', 'layout': 'F10', 'MicOff': 'F3'}


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/terminal')
def terminal():
    form = TerminalMacrosForm()
    return render_template('macros_page.html', form=form)


@app.route('/click',  methods=['POST'])
def click():
    command = (request.form.to_dict()).popitem()[1]
    command = button_terminal[command]
    print(command)
    form = TerminalMacrosForm()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=str(form.ipTerminal.data), username=str('admin'), password=str('123'), port=22)
    with client.invoke_shell() as ssh:
        ssh.send(f'button "{command}"' + "\n")
        time.sleep(0.3)
    return redirect('/terminal')
