# НАСТРОЙКИ НАТИВНОЙ ТИПОГРАФИКИ iOS
#
# Переменные настроены в соответствии с HIG (дефолтный размер Large),
# с помощью которых можно сгенерировать набор токенов для Figma

##############################################################################


# Какие шрифты будут использоваться в проекте?
FONT_FAMILIES = [
    'SF Pro',
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
                'typeface': 'Semibold',
            },
        },
        'sizes': {
            'size_pairs': [500, 300, 400, 500],
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
            'line_height_increment': -2,
            'ignore_sizes': [],
            'open_type': []
        },
        'sparse': {
            'enabled': False,
            'line_height_increment': 2,
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
            'size_pairs': [100, 300, 400, 500],
            'font_size': 17,
            'line_height': 22,
            'paragraph_spacing': 0,
            'tracking': [-0.08, -0.23, -0.31, -0.43],
            'font_size_increment': 1,
            'line_height_increment': 2,
            'paragraph_spacing_increment': 1,
            'text_case': 'none',
            'text_decoration': 'none',
            'open_type': []
        },
        'dense': {
            'enabled': False,
            'line_height_increment': -2,
            'ignore_sizes': [],
            'open_type': []
        },
        'sparse': {
            'enabled': False,
            'line_height_increment': 2,
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
            'size_pairs': [400, 500],
            'font_size': 12,
            'line_height': 16,
            'paragraph_spacing': 0,
            'tracking': [0.06, 0],
            'font_size_increment': 1,
            'line_height_increment': 3,
            'paragraph_spacing_increment': 1,
            'text_case': 'none',
            'text_decoration': 'none',
            'open_type': []
        },
        'dense': {
            'enabled': False,
            'line_height_increment': -2,
            'ignore_sizes': [],
            'open_type': []
        },
        'sparse': {
            'enabled': False,
            'line_height_increment': 2,
            'ignore_sizes': [],
            'open_type': []
        },
    },
}
