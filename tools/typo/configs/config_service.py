# Какие шрифты будут использоваться в проекте?
FONT_FAMILIES = [
    'Manrope',
    'JetBrains Mono'
]

# Структура типографики
TYPOGRAPHY_STRUCTURE = {
    'headline': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'headline': {
                'typeface': 'Bold',
            },
        },
        'sizes': {
            'size_pairs': [500, 600, 700, 800],
            'font_size': 20,
            'line_height': 28,
            'paragraph_spacing': 0,
            'tracking': ['0.8%', '0.4%', 0, 0],
            'font_size_increment': 8,
            'line_height_increment': 8,
            'paragraph_spacing_increment': 0,
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
                'typeface': 'Medium',
            },
        },
        'sizes': {
            'size_pairs': [400, 500, 600],
            'font_size': 20,
            'line_height': 28,
            'paragraph_spacing': 12,
            'tracking': ['1.4%', '0.8%', '0.4%'],
            'font_size_increment': 4,
            'line_height_increment': 4,
            'paragraph_spacing_increment': 4,
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
    'code': {
        'font': FONT_FAMILIES[1],
        'styles': {
            'code': {
                'typeface': 'Regular',
            },
        },
        'sizes': {
            'size_pairs': [400, 500, 600],
            'font_size': 20,
            'line_height': 28,
            'paragraph_spacing': 0,
            'tracking': 0,
            'font_size_increment': 4,
            'line_height_increment': 4,
            'paragraph_spacing_increment': 0,
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
