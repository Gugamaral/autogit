import pyautogui as auto
import time

auto.hotkey('ctrl', 'j')
auto.hotkey('ctrl', 'j')
auto.press('enter')
auto.write('git init')
auto.press('enter')
auto.write('git add .')
auto.press('enter')
auto.write('git config --global user.name "Gugamaral"')
auto.press('enter')
auto.write('git config --global user.email "guamaral@gmail.com"')
auto.press('enter')
auto.write('git commit -m "Versão 1.0"')
auto.press('enter')
auto.write('git branch -M main')
auto.press('enter')
auto.write('git remote add origin https://github.com/Gugamaral/autogit.git')
auto.press('enter')
auto.write('git push -u origin main')
auto.press('enter')

auto.press('tb')
auto.press('tb')
auto.press('tb')
auto.press('tb')
auto.press('tb')
auto.press('enter')

auto.write('pip install cx_Freeze')
auto.press('enter')

auto.write('cxfreeze main.py --target-dir pasta-autoguit')
auto.press('enter')


