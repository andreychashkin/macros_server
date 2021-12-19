from app import app
from flask import render_template, redirect, request, session
from app.forms import TerminalMacrosForm, NewFileForm, PlayTest
from app.commandSSH import command_to_terminal
import time, paramiko


button_terminal = {'Pause': 'button "Pause"\n',
                   'V+': 'button "F9"\n',
                   'V-': 'button "F8"\n',
                   '+': 'button "F7"\n',
                   '-': 'button "F6"\n',
                   'Up': 'button "Up"\n',
                   'Left': 'button "Left"\n',
                   'Down': 'button "Down"\n',
                   'Right': 'button "Right"\n',
                   'Ok': 'button "Return"\n',
                   'Home': 'button "F4"\n',
                   'Back': 'button "Escape"\n',
                   'Save': 'button "F12"\n',
                   'Call': 'button "F1"\n',
                   'Dell': 'button "BackSpace"\n',
                   'Off': 'button "F2"\n',
                   '1': 'button "1"\n', '2': 'button "2"\n', '3': 'button "3"\n',
                   '4': 'button "4"\n', '5': 'button "5"\n', '6': 'button "6"\n',
                   '7': 'button "7"\n', '8': 'button "8"\n', '9': 'button "9"\n',
                   '0': 'button "1"\n', '.*': 'button "Dot"\n', '#@': 'button "Dog"\n',
                   'pc': 'button "F5"\n', 'far/near': 'button "ScrollLock"\n', 'layout': 'button "F10"\n',
                   'MicOff': 'button "F3"\n', 'Sys': 'button -t 2 "Pause"\n',
                   'focus': 'focus\n', 'SaveIp': 'SaveIp', 'Clear': 'Clear'}


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
    command = (request.form.to_dict()).popitem()[1]
    command = button_terminal[command]
    command_to_terminal(command)
    if 'arr' in session:
        l = session.get('arr')
        l.append(command)
        session['arr'] = l
    else:
        session['arr'] = []
    return redirect('/terminal')


@app.route('/newTest', methods=['POST'])
def new_test():
    form = NewFileForm()
    form.new_file()
    return redirect('/terminal')


@app.route('/playTest', methods=['POST'])
def play_test():
    form = PlayTest()
    command = (request.form.to_dict())
    if 'deleteTest' in command:
        form.delete_test()
    elif 'playTest' in command:
        file = open(f'macros/{form.selectTest.data}', 'r')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=str(session['ipTerminal']), username=str('admin'), password=str('123'), port=22)
        with client.invoke_shell() as ssh:
            for line in file.readlines():
                ssh.send(line)
                time.sleep(0.3)
    elif 'clearCommand' in command:
        session['arr'] = []
    elif 'recCommand' in command:
        form.rec()
    return redirect('/terminal')
