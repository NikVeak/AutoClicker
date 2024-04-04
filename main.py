from pywinauto.application import Application
from pywinauto import findwindows
from pywinauto.keyboard import send_keys
from pywinauto.mouse import move
import keyboard

# Получение списка всех окон
windows = findwindows.find_elements()
print("---------------------------------")
# Вывод списка окон
for window in windows:
    print(window)
print("---------------------------------")

app = Application(backend='win32').connect(title='kali [Работает] - Oracle VM VirtualBox')
# Получение списка окон приложения
windows = app.windows()
# Вывод информации обо всех окнах
for window in windows:
    print(window.window_text())

window = app.window(title='kali [Работает] - Oracle VM VirtualBox')
window.set_focus()
window.draw_outline()

# Симуляция нажатия Right Ctrl + F
send_keys('^{F}')  # ^ - обозначение для Control (Ctrl), {F} - обозначение для клавиши F

# Получение списка всех элементов окна
elements = window.children()

# Указание координат x и y для перемещения курсора мыши
window_rect = window.rectangle()
window_width = window_rect.width()
window_height = window_rect.height()

# Вычисление координат центра окна
center_x = window_rect.left + (window_width // 2)
center_y = window_rect.top + (window_height // 2)

# Перемещение курсора мыши в центр окна
move(coords=(center_x, center_y))
send_keys('ggwpeasy')
keyboard.send('a')
