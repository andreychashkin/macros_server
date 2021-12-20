from flask_wtf import FlaskForm
from flask import session
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
import os


class TerminalMacrosForm(FlaskForm):
    ipTerminal = StringField('Terminal Ip')
    saveIp = SubmitField('SaveIp')
    pause = SubmitField('Pause')
    focus = SubmitField('focus')
    system = SubmitField('Sys')
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

    def set_ip_terminal(self):
        if 'ipTerminal' in session:
            self.ipTerminal.data = session['ipTerminal']
        else:
            session['ipTerminal'] = ''
            self.ipTerminal.data = ''
        return


class NewFileForm(FlaskForm):
    nameTest = StringField('nameTest')
    newTest = SubmitField('newTest')

    def new_file(self):
        if self.nameTest.data:
            f = open('macros/' + self.nameTest.data, 'w+')
            f.close()
        return


class PlayTest(FlaskForm):
    current_dir = os.path.abspath('.').partition('//')
    current_dir = current_dir[0] + '/macros/'
    selectTest = SelectField('selectTest')
    playTest = SubmitField('playTest')
    deleteTest = SubmitField('deleteTest')
    textForm = TextAreaField(default='')
    recCommand = SubmitField('recCommand')
    clearCommand = SubmitField('clearCommand')
    repeat = IntegerField('repeat', default=1)

    def load_test_in_select(self):
        self.selectTest.choices = self.load_txt()

    def load_txt(self):
        rez = []
        for file in os.listdir(self.current_dir):
            if file.endswith(".txt"):
                rez.append(file)
        return rez

    def delete_test(self):
        os.remove(f'macros/{self.selectTest.data}')

    def load_command(self, line=['']):
        for i in line:
            self.textForm.data = self.textForm.data + i + '\n'

    def rec(self):
        file = open(f'macros/{self.selectTest.data}', 'w+')
        file.write(self.textForm.data)
        file.close()