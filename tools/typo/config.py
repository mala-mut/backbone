# НАСТРОЙКИ ТИПОГРАФИКИ
#
# Здесь нужно настроить переменные, с помощью которых можно сгенерировать
# набор токенов для Figma
#
# TODO: конвертация токенов под платформы
# TODO: letter_spacing в % и px

##############################################################################


# 1. Какие шрифты будут использоваться в проекте?
FONT_FAMILIES = [
    'Manrope',
]


# 2. Каким будет основной наборный текст?
BODY = {
    'font': FONT_FAMILIES[0],
    'font_size': 16,
    'line_height': 24,
    'letter_spacing': '1.4%',
    'paragraph_spacing': 8,
}


# 3. Нужны ли второстепенный или более крупный наборные стили?
BODY_SIZE_INCREMENT = 2
BODY_SIZES = {
    '400',
    '500',
    '600',
}


# 4. Какие начертания нужны для основного текста?
BODY_STYLES = {
    'body': {
        'typeface': 'Medium',
    },
    'body-accent': {
        'typeface': 'Bold',
    },
}


# 5. Будут ли в проекте таблицы и ячейки?
BODY_DENSE = True
BODY_DENSE_LINE_HEIGHT_DECREMENT = 4
BODY_TABULAR = True


# 6. Нужны ли в проекте наборные шрифты с более разреженным межстрочником?
BODY_SPARSE = True
BODY_SPARSE_LINE_HEIGHT_INCREMENT = 4
