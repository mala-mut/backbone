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
    'SF Pro'
]

# Структура типографики
TYPOGRAPHY_STRUCTURE = {
    'headline': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'headline': {
                'typeface': 'Regular',
            },
            'headline-accent': {
                'typeface': 'SemiBold',
            },
        },
        'sizes': {
            'size_pairs': [500, 600, 700, 800, 900],
            'font_size': [17, 20, 22, 28, 34],
            'line_height': [22, 25, 28, 34, 41],
            'paragraph_spacing': 0,
            'tracking': [-0.43, -0.45, -0.26, 0.38, 0.40],
            'font_size_increment': 1,
            'line_height_increment': 1,
            'paragraph_spacing_increment': 1,
            'text_case': 'none',
            'text_decoration': 'none',
            'open_type': []
        },
        'dense': {
            'enabled': False,
            'line_height_increment': -4,
            'ignore_sizes': [],
            'open_type': []
        },
        'sparse': {
            'enabled': False,
            'line_height_increment': 4,
            'ignore_sizes': [],
            'open_type': []
        },
    },
    'body': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'body': {
                'typeface': 'Regular',
            },
        },
        'sizes': {
            'size_pairs': [500, 400, 300, 100],
            'font_size': 17,
            'line_height': 22,
            'paragraph_spacing': 0,
            'tracking': [-0.43, -0.31, -0.23, -0.08],
            'font_size_increment': 1,
            'line_height_increment': 1,
            'paragraph_spacing_increment': 1,
            'text_case': 'none',
            'text_decoration': 'none',
            'open_type': []
        },
        'dense': {
            'enabled': False,
            'line_height_increment': -4,
            'ignore_sizes': [],
            'open_type': []
        },
        'sparse': {
            'enabled': False,
            'line_height_increment': 4,
            'ignore_sizes': [],
            'open_type': []
        },
    },
    'caption': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'caption': {
                'typeface': 'Regular',
            },
        },
        'sizes': {
            'size_pairs': [500, 400],
            'font_size': 12,
            'line_height': 16,
            'paragraph_spacing': 0,
            'tracking': [0, 0.06],
            'font_size_increment': 1,
            'line_height_increment': 3,
            'paragraph_spacing_increment': 1,
            'text_case': 'none',
            'text_decoration': 'none',
            'open_type': []
        },
        'dense': {
            'enabled': False,
            'line_height_increment': -4,
            'ignore_sizes': [],
            'open_type': []
        },
        'sparse': {
            'enabled': False,
            'line_height_increment': 4,
            'ignore_sizes': [],
            'open_type': []
        },
    },
}
