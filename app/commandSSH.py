from flask import session
from app.forms import TerminalMacrosForm
from PIL import Image, ImageFont, ImageDraw
import paramiko
import time
import requests


def command_to_terminal(command):
    form = TerminalMacrosForm()
    if 'SaveIp' in command:
        session['ipTerminal'] = form.ipTerminal.data
        return
    elif 'Screen' in command:
        #request_connect(form, form2)
        return
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=str(form.ipTerminal.data), username=str('admin'), password=str('123'), port=22)
        with client.invoke_shell() as ssh:
            ssh.send(command + '\n')
            time.sleep(0.2)
    except:
        print("Не удалось отправить команду терминалу")
    return


# функция подключения к странице скриншота терминала для получения изображения
def request_connect(ipTerminal, testName, text='ММММММ ХУЕТА'):
    try:
        with requests.Session() as session:
            url = "http://" + ipTerminal + "/auth/login"  # URL с формами логина
            response = session.get(url, verify=False)  # Получаем страницу с формой логинаhttps://10.1.0.100/auth/logout
            token = response.text
            token = token[response.text.find('"csrf-token"') + 22: response.text.find('"csrf-token"') + 70]#поиск по html коду нужной строчки токена

            dann = dict(method="vinteo", lang="ru", target="", csrf=token, username='admin', password='123')  # Данные для конекта в виде словаря
            session.post(url, dann)  # Отправляем данные в POST, в session записываются наши куки
            name_screen = testName.split('.')[0] # парсим имя терминала и забираем все до "."
            font = ImageFont.truetype("./app/font/20016.ttf", size=30) #параметры шрифта на скрине
            r = session.get("https://" + ipTerminal + "/terminal/desktop", verify=False) # используя ранее установленное соединение получаем страницу со скрином
            way = "./screen/" + name_screen + "_" + time.strftime("%d-%H-%M-%S", time.localtime()) + '.png'
            out = open(way, "wb" )#создаем файл для записи в него скрина
            out.write(r.content)#пишем картинку в файл
            out.close()  # закрываем файл с созранением скрина

            img = Image.open(way)# открываем только что записанный файл
            draw = ImageDraw.Draw(img)# объект позвляющий рисовать на картинке
            draw.text((10, 10), text=text, fill=(200, 30, 30), font=font)# записываем текст на картинку
            img.save(way)# сохраняем изменения на картинкее
    except:
        return
