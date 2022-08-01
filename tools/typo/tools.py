# TOKENS MODEL

STYLE = {
    'font': None,
    'typeface': None,
    'font_size': None,
    'line_height': None,
    'letter_spacing': None,
    'paragraph_spacing': None,
    'text_case': None,
    'open_type': None,
    'text_decoration': None,
}


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

CUSTOM_TYPES = {
    'open_type': {
        'name': 'openType',
        'type': 'openType',
    },
}


def make_token(value, token_type):
    # TODO: generate descriptions

    token_systems = [FT_TYPES, CUSTOM_TYPES]

    for token_system in token_systems:
        try:
            return {
                token_system[token_type]['name']: {
                    'value': value,
                    'type': token_system[token_type]['type']
                }
            }
        except KeyError:
            if token_system == token_systems[-1]:
                raise Exception(f'No such token: {token_type}')


# TOOLS FOR GENERATING TOKENS

def get_sizes(base_font_size, base_line_height, increment, size):
    font_size = base_font_size + increment * size
    line_height = base_line_height + increment * size * 2
    return int(font_size), int(line_height)
