# НАСТРОЙКИ ТИПОГРАФИКИ
#
# Здесь нужно настроить переменные, с помощью которых можно сгенерировать
# набор токенов для Figma
#
# TODO: конвертация токенов под платформы
# TODO: настройка исключений
# TODO: варианты для text_decoration и text_case
# TODO: description к стилям

##############################################################################


# Какие шрифты будут использоваться в проекте?
FONT_FAMILIES = [
    'Manrope',
    'JetBrains Mono'
]

# Структура типографики
TYPOGRAPHY_STRUCTURE = {
    'body': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'body': {
                'typeface': 'Medium',
            },
            'body-accent': {
                'typeface': 'Bold',
            },
        },
        'sizes': {
            'size_pairs': [400, 500, 600],
            'font_size': 16,
            'line_height': 24,
            'paragraph_spacing': 8,
            'tracking': ['1.5%', '1.4%', '1.3%'],
            'font_size_increment': 2,
            'line_height_increment': 4,
            'paragraph_spacing_increment': 1,
            'text_case': 'none',
            'text_decoration': 'none',
            'open_type': []
        },
        'dense': {
            'enabled': True,
            'line_height_increment': -4,
            'ignore_sizes': [],
            'open_type': []
        },
        'sparse': {
            'enabled': True,
            'line_height_increment': 4,
            'ignore_sizes': [],
            'open_type': []
        },
    },
}
