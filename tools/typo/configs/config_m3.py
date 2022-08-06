# НАСТРОЙКИ НАТИВНОЙ ТИПОГРАФИКИ M3
#
# Переменные настроены в соответствии с Material 3, и с их помощью можно
# сгенерировать набор токенов для Figma

##############################################################################


# Какие шрифты будут использоваться в проекте?
FONT_FAMILIES = [
    'Roboto',
]

# Структура типографики
TYPOGRAPHY_STRUCTURE = {
    'display': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'display': {
                'typeface': 'Regular',
            },
        },
        'sizes': {
            'size_pairs': [400, 500, 600],
            'font_size': [36, 45, 57],
            'line_height': [44, 52, 64],
            'paragraph_spacing': 0,
            'tracking': 0,
            'font_size_increment': 1,
            'line_height_increment': 4,
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
    'headline': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'headline': {
                'typeface': 'Regular',
            },
        },
        'sizes': {
            'size_pairs': [400, 500, 600],
            'font_size': 36,
            'line_height': 28,
            'paragraph_spacing': 0,
            'tracking': 0,
            'font_size_increment': 4,
            'line_height_increment': 4,
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
    'title': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'title': {
                'typeface': 'Regular',
            },
        },
        'sizes': {
            'size_pairs': [400, 500, 600],
            'font_size': [14, 16, 22],
            'line_height': 24,
            'paragraph_spacing': 0,
            'tracking': ['0.1%', '0.15%', 0],
            'font_size_increment': 1,
            'line_height_increment': 4,
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
    'label': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'label': {
                'typeface': 'Medium',
            },
        },
        'sizes': {
            'size_pairs': [400, 500, 600],
            'font_size': [11, 12, 14],
            'line_height': [16, 16, 20],
            'paragraph_spacing': 0,
            'tracking': ['0.5%', '0.5%', '0.1%'],
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
            'size_pairs': [400, 500, 600],
            'font_size': 14,
            'line_height': 20,
            'paragraph_spacing': 0,
            'tracking': ['0.4%', '0.25%', '0.5%'],
            'font_size_increment': 2,
            'line_height_increment': 4,
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
