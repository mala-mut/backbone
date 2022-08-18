# TOKENS MODEL

STYLE = {
    'font': None,
    'typeface': None,
    'font_size': None,
    'line_height': None,
    'tracking': None,
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
    'tracking': {
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


def make_tokens(raw_styles):
    style_dict = dict()

    for key, value in raw_styles.items():
        style_dict.update(make_token(value, key))

    return style_dict


def make_typography(level, raw_styles):
    return {
        level: {
            'value': make_tokens(raw_styles),
            'type': 'typography'
        }
    }


# TOOLS FOR GENERATING TOKENS

def get_sizes(base_font_size, base_line_height,
              base_paragraph_spacing, fs_increment, lh_increment, ps_increment,
              level):
    font_size = base_font_size + fs_increment * level
    line_height = base_line_height + lh_increment * level
    paragraph_spacing = base_paragraph_spacing + ps_increment * level
    return int(font_size), int(line_height), int(paragraph_spacing)


# HELPER TOOLS
def get_value(storage, index):
    if type(storage) != list:
        return storage
    else:
        return storage[index]
