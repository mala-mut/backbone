import json
import os

import config
import params
import tools

# Setting output folder with tokens
dirname = os.path.dirname(__file__)
path_out = '../../raw/typography.json'

# Setting up base style to initialize everything else
base_style = dict(tools.STYLE)

for key, value in config.BODY.items():
    base_style[key] = value

base_style['text_case'] = params.TEXT_CASE['none']
base_style['open_type'] = params.OPEN_TYPE['default']
base_style['text_decoration'] = params.TEXT_DECORATION['none']

body_styles = list(config.BODY_STYLES.keys())
typography = {'typography': dict.fromkeys(body_styles)}

for level in config.BODY_SIZES:
    for style in body_styles:
        style_dict = dict()
        raw_base_style = dict(base_style)
        size = (int(level) - 500) / 100

        # Getting values for font size and line height
        raw_base_style['font_size'], raw_base_style['line_height'] = \
            tools.get_sizes(
                base_style['font_size'],
                base_style['line_height'],
                config.BODY_SIZE_INCREMENT,
                size
            )

        # Getting typeface
        raw_base_style['typeface'] = config.BODY_STYLES[style]['typeface']

        # Generating FT for all values
        for key, value in raw_base_style.items():
            style_dict.update(tools.make_token(value, key))

        style_dict = {
            'value': style_dict,
            'type': 'typography'
        }

        try:
            typography['typography'][style].update({level: style_dict})
        except AttributeError:
            typography['typography'][style] = {level: style_dict}


with open(os.path.join(dirname, path_out), 'w') as outfile:
    json.dump(typography, outfile)
