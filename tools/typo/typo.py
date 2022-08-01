import config

import json

import os

dirname = os.path.dirname(__file__)
path_out = '../../raw/typography.json'

# Text-case options
TEXT_CASE = {
    'none': 'none',
    'uppercase': 'uppercase',
    'lowercase': 'lowercase',
    'capitalize': 'capitalize'
}

# Text-decoration options
TEXT_DECORATION = {
    'none': 'none',
    'underline': 'underline',
    'line-through': 'line-through'
}

# OpenType feature groups
# TODO: заполнить OT-features
OPEN_TYPE = {
    'default': [],
    'tabular': []
}


base_style = dict(config.BODY)
base_style['text_case'] = TEXT_CASE['none']
base_style['open_type'] = OPEN_TYPE['default']
base_style['text_decoration'] = TEXT_DECORATION['none']

typography = {
    'body': {}
}

for style in config.BODY_SIZES:
    current_size = (int(style) - 500) / 100
    style_dict = dict(base_style)
    style_dict['font_size'] = int(base_style['font_size'] +
                                  config.BODY_SIZE_INCREMENT * current_size)
    style_dict['line-height'] = int(base_style['line_height'] +
                                    config.BODY_SIZE_INCREMENT *
                                    current_size * 2)
    typography['body'][style] = {}
    typography['body'][style]['value'] = style_dict
    typography['body'][style]['type'] = 'typography'

for style, params in config.BODY_ACCENT.items():
    typography[f'body-{style}'] = {}
    style_dict = dict(base_style)

    for size in config.BODY_SIZES:
        current_size = (int(size) - 500) / 100
        style_dict = dict(base_style)
        style_dict['font_size'] = int(base_style['font_size'] +
                                      config.BODY_SIZE_INCREMENT * current_size)
        style_dict['line-height'] = int(base_style['line_height'] +
                                        config.BODY_SIZE_INCREMENT *
                                        current_size * 2)
        for param, value in params.items():
            style_dict[param] = value
        typography[f'body-{style}'][size] = {}
        typography[f'body-{style}'][size]['value'] = style_dict
        typography[f'body-{style}'][size]['type'] = 'typography'

with open(os.path.join(dirname, path_out), 'w') as outfile:
    json.dump(typography, outfile)
