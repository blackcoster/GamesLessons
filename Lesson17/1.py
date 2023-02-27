# # Полный путь
# import my_package.primitive.text
#
# my_package.primitive.text.printer()

# # Загрузка конкретного подмодуля
# from my_package.primitive import text
#
# text.printer()
#
# Загрузка конкретной функции из подмодуля
from my_package.primitive.text import printer

printer()
