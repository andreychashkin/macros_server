from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class TerminalMacrosForm(FlaskForm):
    ipTerminal = StringField('Terminal Ip', default='10.1.0.129')
    pause = SubmitField('Pause')
    volumeUp = SubmitField('V+')
    volumeDown = SubmitField('V-')
    camPlus = SubmitField('+')
    camMinus = SubmitField('-')
    up = SubmitField('Up')
    left = SubmitField('Left')
    down = SubmitField('Down')
    right = SubmitField('Right')
    ok = SubmitField('Ok')
    home = SubmitField('Home')
    back = SubmitField('Back')
    save = SubmitField('Save')
    call = SubmitField('Call')
    backSpace = SubmitField('Dell')
    callOff = SubmitField('Off')
    button_1 = SubmitField('1')
    button_2 = SubmitField('2')
    button_3 = SubmitField('3')
    button_4 = SubmitField('4')
    button_5 = SubmitField('5')
    button_6 = SubmitField('6')
    button_7 = SubmitField('7')
    button_8 = SubmitField('8')
    button_9 = SubmitField('9')
    button_0 = SubmitField('0')
    button_dot = SubmitField('.*')
    button_dog = SubmitField('#@')
    pc = SubmitField('pc')
    far = SubmitField('far/near')
    layout = SubmitField('layout')
    micOff = SubmitField('MicOff')
