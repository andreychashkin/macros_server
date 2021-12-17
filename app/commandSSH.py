from flask import redirect, make_response
from app.forms import TerminalMacrosForm, PlayTest
import paramiko
import time


def command_to_terminal(command):
    form = TerminalMacrosForm()
    form2 = PlayTest()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=str(form.ipTerminal.data), username=str('admin'), password=str('123'), port=22)
    with client.invoke_shell() as ssh:
        if 'SaveIp' in command or 'setTest' in command:
            resp = make_response(redirect('/terminal'))
            resp.set_cookie('ipTerminal', f'{form.ipTerminal.data}', max_age=60 * 60 * 24 * 30)
            resp.set_cookie('selectTest', f'{form2.selectTest.data}', max_age=60 * 60 * 24 * 30)
            return resp
        else:
            ssh.send(command)
        time.sleep(0.3)
    return
