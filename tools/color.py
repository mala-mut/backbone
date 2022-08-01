import argparse
from functools import reduce
import json

import matplotlib.colors


def hex_to_rgba(color):
    raw_rgba = tuple(map(lambda x: round(x, 3), matplotlib.colors.to_rgba(color)))
    return {
        'raw': raw_rgba,
        'rgb': raw_rgba[:-1],
        'opacity': raw_rgba[-1]
    }


def parsed_rgb_a(hex_color):
    color = hex_to_rgba(hex_color)
    if color['opacity'] != 1.0:
        return 'rgba{}'.format(str(color['raw']).replace(' ', ''))
    else:
        return 'rgb{}'.format(str(color['rgb']).replace(' ', ''))


def iterate_json(dict_obj):
    for key, value in dict_obj.items():
        if isinstance(value, dict):
            for pair in iterate_json(value):
                yield key, *pair
        else:
            if len(value) and value[0] == '#':
                dict_obj[key] = parsed_rgb_a(value)
            yield key, value


def iterate_json(dict_obj):
    for key, value in dict_obj.items():
        if isinstance(value, dict):
            for _ in iterate_json(value):
                pass
        else:
            if len(value) and value[0] == '#':
                dict_obj[key] = parsed_rgb_a(value)


# parser = argparse.ArgumentParser(description='Convert HEX-colors in JSON to RGB(a)')
# parser.add_argument('path', metavar='P', nargs=1, help='path to JSON file')
#
# args = parser.parse_args()
# path = vars(args)['path'][0]

path = '../../WebstormProjects/Design System/tokens/colors/bx_colors.json'

f = open(path)
j = json.load(f)

for pair in iterate_json(j):
    value = pair[-1]
    if len(value) and value[0] == '#':
        path = pair[:-1]
        rgba_color = parsed_rgb_a(value)
        reduce(lambda seq, key: seq[key], path, j)
