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
            'font_size': 16,
            'line_height': 20,
            'paragraph_spacing': 0,
            'tracking': ['1.4%', '1%', '0.6%', '0.2%'],
            'font_size_increment': [0, 2, 4, 4],
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
    'body': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'body': {
                'typeface': 'Medium',
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
            'size_pairs': [400, 500],
            'font_size': 16,
            'line_height': 24,
            'paragraph_spacing': 0,
            'tracking': 0,
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
