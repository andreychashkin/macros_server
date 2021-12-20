from app import app
from flask import render_template, redirect, request, session
from app.forms import TerminalMacrosForm, NewFileForm, PlayTest
from app.commandSSH import command_to_terminal
import time, paramiko


button_terminal = {'Pause': 'button "Pause"',
                   'timeSleepButton': 'timeSleepButton',
                   'V+': 'button "F9"',
                   'V-': 'button "F8"',
                   '+': 'button "F7"',
                   '-': 'button "F6"',
                   'Up': 'button "Up"',
                   'Left': 'button "Left"',
                   'Down': 'button "Down"',
                   'Right': 'button "Right"',
                   'Ok': 'button "Return"',
                   'Home': 'button "F4"',
                   'Back': 'button "Escape"',
                   'Save': 'button "F12"',
                   'Call': 'button "F1"',
                   'Dell': 'button "BackSpace"',
                   'Off': 'button "F2"',
                   '1': 'button "1"', '2': 'button "2"', '3': 'button "3"',
                   '4': 'button "4"', '5': 'button "5"', '6': 'button "6"',
                   '7': 'button "7"', '8': 'button "8"', '9': 'button "9"',
                   '0': 'button "1"', '.*': 'button "Dot"', '#@': 'button "Dog"',
                   'pc': 'button "F5"', 'far/near': 'button "ScrollLock"', 'layout': 'button "F10"',
                   'MicOff': 'button "F3"', 'Sys': 'button -t 2 "Pause"',
                   'focus': 'focus', 'SaveIp': 'SaveIp', 'Clear': 'Clear'}


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
    if 'arr' in session:
        form3.load_command(session['arr'])
    return render_template('macros_page.html', form=form, form2=form2, form3=form3)


@app.route('/click',  methods=['POST'])
def click():
    command = request.form.to_dict().popitem()[1]
    command = button_terminal[command]
    if 'arr' in session:
        l = session.get('arr')
        l.append(command)
        session['arr'] = l
    else:
        session['arr'] = []
    command_to_terminal(command)
    return redirect('/terminal')


@app.route('/newTest', methods=['POST'])
def new_test():
    form = NewFileForm()
    form.new_file()
    return redirect('/terminal')


@app.route('/playTest', methods=['POST'])
def play_test():
    form = PlayTest()
    command = request.form.to_dict()
    if 'deleteTest' in command:
        form.delete_test()
    elif 'playTest' in command:
        file = open(f'macros/{form.selectTest.data}', 'r')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=str(session['ipTerminal']), username=str('admin'), password=str('123'), port=22)
        with client.invoke_shell() as ssh:
            for i in range(0, form.repeat.data):
                file = open(f'macros/{form.selectTest.data}', 'r')
                for line in file.readlines():
                    if 'sleep' in line:
                        t = int(line.split(' ')[1])
                        time.sleep(t)
                    ssh.send(line)
                    time.sleep(0.3)
                time.sleep(2)

    elif 'clearCommand' in command:
        session['arr'] = []
    elif 'recCommand' in command:
        q = form.textForm.data
        session['arr'] = [q]
        form.rec()
    return redirect('/terminal')
