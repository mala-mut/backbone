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


# Generating body styles

for level in config.BODY_SIZES:
    for style in body_styles:
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
        try:
            typography['typography'][style].update(
                tools.make_typography(level, raw_base_style))
        except AttributeError:
            typography['typography'][style] = dict(
                tools.make_typography(level, raw_base_style))

        if config.BODY_SPARSE:
            raw_sparse_style = dict(raw_base_style)
            raw_sparse_style['line_height'] += \
                config.BODY_SPARSE_LINE_HEIGHT_INCREMENT

            typography['typography'][style].update(
                tools.make_typography(level + '-sparse', raw_sparse_style))

        if config.BODY_DENSE:
            raw_dense_style = dict(raw_base_style)
            raw_dense_style['line_height'] -= \
                config.BODY_DENSE_LINE_HEIGHT_DECREMENT
            if config.BODY_TABULAR:
                raw_dense_style['open_type'] = params.OPEN_TYPE['tabular']

            typography['typography'][style].update(
                tools.make_typography(level + '-dense', raw_dense_style))


# Dumping tokens for FT

with open(os.path.join(dirname, path_out), 'w') as outfile:
    json.dump(typography, outfile)
