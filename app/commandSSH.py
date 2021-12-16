from flask import redirect, make_response
from app.forms import TerminalMacrosForm
import paramiko
import time


def command_to_terminal(command):
    form = TerminalMacrosForm()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=str(form.ipTerminal.data), username=str('admin'), password=str('123'), port=22)
    with client.invoke_shell() as ssh:
        if 'focus' in command:
            ssh.send(f'{command}' + "\n")
        elif 'sys' in command:
            ssh.send('button -t 2 "Pause"' + "\n")
        elif 'SaveIp' in command:
            resp = make_response(redirect('/terminal'))
            resp.set_cookie('ipTerminal', f'{form.ipTerminal.data}', max_age=60 * 60 * 24 * 30)
            return resp
        else:
            ssh.send(f'button "{command}"' + "\n")
        time.sleep(0.3)
    return
