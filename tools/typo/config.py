# Какие шрифты будут использоваться в проекте?
FONT_FAMILIES = [
    'Inter',
]

# Структура типографики
TYPOGRAPHY_STRUCTURE = {
    'headline': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'headline-accent': {
                'typeface': 'Semi Bold',
            },
            'headline': {
                'typeface': 'Light',
            },
        },
        'sizes': {
            'size_pairs': [500, 600, 700, 800, 900],
            'font_size': [18, 24, 32, 40, 64],
            'line_height': [24, 32, 40, 48, 72],
            'paragraph_spacing': 0,
            'tracking': ['-0.26 px', '-0.47 px', '-0.69 px', '-0.89 px',
                         '-1.43 px'],
            'font_size_increment': 0,
            'line_height_increment': 0,
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
                'typeface': 'Regular',
            },
        },
        'sizes': {
            'size_pairs': [300, 400, 500, 600],
            'font_size': 18,
            'line_height': 28,
            'paragraph_spacing': 8,
            'tracking': ['-0.09 px', '-0.18 px', '-0.26 px', '-0.33 px'],
            'font_size_increment': 2,
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
    'compact': {
        'font': FONT_FAMILIES[0],
        'styles': {
            'compact': {
                'typeface': 'Regular',
            },
        },
        'sizes': {
            'size_pairs': [300, 400, 500, 600],
            'font_size': 18,
            'line_height': 24,
            'paragraph_spacing': 8,
            'tracking': ['-0.09 px', '-0.18 px', '-0.26 px', '-0.33 px'],
            'font_size_increment': 2,
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
}
