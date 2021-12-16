from flask_wtf import FlaskForm
from flask import request, make_response
from wtforms import StringField, SubmitField, SelectField, Label
import os, threading


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
        cookie = request.cookies.get('ipTerminal')
        if cookie != None:
            self.ipTerminal.data = cookie
            make_response().set_cookie('ipTerminal', '', max_age=0)
        else:
            print("not cookie")
            self.ipTerminal.data = '10.1.0.129'
        return


class NewFileForm(FlaskForm):
    nameTest = StringField('nameTest')
    newTest = SubmitField('newTest')

    def new_file(self):
        if not(self.nameTest.data is None):
            f = open('macros/'+ self.nameTest.data, 'w+')
            f.close()
        return


class PlayTest(FlaskForm):
    selectTest = SelectField('selectTest')
    playTest = SubmitField('playTest')
    deleteTest = SubmitField('deleteTest')
    statusTest = Label('deleteTest', 'Status Test')

    def load_test_in_select(self):
        self.selectTest.choices = self.load_txt()

    def load_txt(self):
        rez = []
        current_dir = os.path.abspath('.').partition('//')
        current_dir = current_dir[0] + '/macros/'
        for file in os.listdir(current_dir):
            if file.endswith(".txt"):
                rez.append(file)
        return rez

    def delete_test(self):
        os.remove(f'macros/{self.selectTest.data}')
        return
