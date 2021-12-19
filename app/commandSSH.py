from flask import session
from app.forms import TerminalMacrosForm
import paramiko
import time


def command_to_terminal(command):
    form = TerminalMacrosForm()
    if 'SaveIp' in command:
        session['ipTerminal'] = form.ipTerminal.data
        return
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=str(form.ipTerminal.data), username=str('admin'), password=str('123'), port=22)
        with client.invoke_shell() as ssh:
            ssh.send(command)
            time.sleep(0.3)
    except:
        print("Не удалось отправить команду терминалу")
    return
