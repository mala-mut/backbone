# TOOLS FOR FIGMA TOKENS CONVERSION

FT_TYPES = {
    'font': {
        'name': 'fontFamily',
        'type': 'fontFamilies',
    },
    'typeface': {
        'name': 'fontWeight',
        'type': 'fontWeights',
    },
    'font_size': {
        'name': 'fontSize',
        'type': 'fontSizes',
    },
    'letter_spacing': {
        'name': 'letterSpacing',
        'type': 'letterSpacing',
    },
    'line_height': {
        'name': 'lineHeight',
        'type': 'lineHeights',
    },
    'paragraph_spacing': {
        'name': 'paragraphSpacing',
        'type': 'paragraphSpacing',
    },
    'text_case': {
        'name': 'textCase',
        'type': 'textCase',
    },
    'text_decoration': {
        'name': 'textDecoration',
        'type': 'textDecoration',
    },
}


def make_ft_token(value, token_type):
    # TODO: catch wrong types
    # TODO: generate descriptions
    return {
        FT_TYPES[token_type]['name']: {
            'value': value,
            'type': FT_TYPES[token_type]['type']
        }
    }
