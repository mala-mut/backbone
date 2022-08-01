import argparse
import json
import os

dirname = os.path.dirname(__file__)

parser = argparse.ArgumentParser(description='Get tokens pointing at the same core colors')
parser.add_argument('--path', metavar='P', type=argparse.FileType('r'),
                    help='path to JSON file')
args = parser.parse_args(args=[])

if vars(args)['path']:
    path_in = vars(args)['path']
else:
    path_in = '../../../WebstormProjects/Design System/tokens/colors/bx_colors.json'

path_out = '../data/color_usage.json'

with open(os.path.join(dirname, path_in)) as f:
    j = json.load(f)

j_keys = list(j.keys())
core_colors = []
color_usage = {}

for item, sub_dict in j.items():
    try:
        if next(iter(sub_dict)) == 'core':
            colors = sub_dict[next(iter(sub_dict))]
            core_color_groups = list(colors.keys())
            for color_group, data in colors.items():
                data_list = list(data.keys())
                if data_list[0] == 'value':
                    core_colors.append(f'core.{color_group}')
                else:
                    for color in data_list:
                        core_colors.append(f'core.{color_group}.{color}')

            color_usage = {k: [] for k in core_colors}
        else:
            try:
                theme_colors = sub_dict[next(iter(sub_dict))]
                theme = next(iter(sub_dict))

                for color_group, colors in theme_colors.items():
                    for color, data in colors.items():
                        token = f'{theme}.{color_group}.{color}'
                        value = data['value'][1:-1]
                        if value in color_usage.keys():
                            color_usage[value].append(token)
            except:
                pass
    except:
        pass

for key, value in color_usage.items():
    print(f'{key}: {len(value)}')

with open(os.path.join(dirname, path_out), 'w') as outfile:
    json.dump(color_usage, outfile)
