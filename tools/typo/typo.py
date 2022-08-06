import json
import os

import config
import tools

# Setting output folder with tokens
dirname = os.path.dirname(__file__)
path_out = '../../raw/typography.json'

typography = dict()

# Looping over all typography categories

for category, category_dict in config.TYPOGRAPHY_STRUCTURE.items():
    base_style = dict(tools.STYLE)

    # initializing base_style with 500 params
    base_style['font'] = category_dict['font']
    base_style['paragraph_spacing'] = category_dict['sizes'][
        'paragraph_spacing'] * category_dict['sizes'][
        'paragraph_spacing_increment']
    base_style['text_case'] = category_dict['sizes']['text_case']
    base_style['text_decoration'] = category_dict['sizes']['text_decoration']
    base_style['open_type'] = category_dict['sizes']['open_type']

    for style, style_dict in category_dict['styles'].items():
        typography.update({style: {}})
        base_style['typeface'] = style_dict['typeface']
        for i, size in enumerate(category_dict['sizes']['size_pairs']):
            level = (size - 500) / 100

            # Getting line heights, font sizes and increments
            size_values = []
            params = ('font_size', 'line_height', 'font_size_increment',
                      'line_height_increment')

            for param in params:
                size_values.append(tools.get_value(category_dict['sizes'][
                    param], i))

            # Getting tracking
            base_style['tracking'] = tools.get_value(category_dict['sizes'][
                'tracking'], i)

            # Getting values for font size and line height
            base_style['font_size'], base_style['line_height'] = \
                tools.get_sizes(*size_values, level)

            # Generating FT for all values
            try:
                typography[style].update(
                    tools.make_typography(size, base_style))
            except AttributeError:
                typography[style] = dict(
                    tools.make_typography(size, base_style))

            # Checking for dense and sparse
            for option in ['dense', 'sparse']:
                if category_dict[option]['enabled'] and size not in \
                        category_dict[option]['ignore_sizes']:
                    option_style = dict(base_style)
                    option_style['line_height'] = tools.get_value(
                        category_dict[option]['line_height_increment'],
                        i) + base_style['line_height']

                    option_style['open_type'] = category_dict[option][
                        'open_type']
                    typography[style].update(tools.make_typography(
                        f'{size}-{option}', option_style))


# Dumping tokens for FT
with open(os.path.join(dirname, path_out), 'w') as outfile:
    json.dump(typography, outfile)
