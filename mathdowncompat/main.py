"""Amends markdown file for math environment support"""

from mathdowncompat.converters import mathml
from mathdowncompat.converters import image
import argparse
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to markdown file')
    parser.add_argument('--converter', choices=('mathml', 'image'),
                        help='math converter to apply', default='image'),
    parser.add_argument('--out', help='path to output markdown file',
                        default=None)
    parser.add_argument('--verbose', action='store_true')

    mathml.initialize_arguments(parser)
    image.initialize_arguments(parser)
    args = parser.parse_args()

    # Define potential math environments
    inline = (r"\$([^\n\$]+?)\$", '$', '$')
    outline = (r"\$\$([\s\S]+?)\$\$", '$$', '$$')

    # List of converters
    converters = {
        'mathml': mathml,
        'image': image
    }

    # List of denotations to replace, using which converters
    # math env, converter
    denotations = (
        (outline, converters[args.converter].convert),
        (inline, converters[args.converter].convert))

    i = 0
    with open(args.path) as f:
        content = f.read()
        for (pattern, left, right), convert in denotations:
            expr = re.compile(pattern)
            for  match in expr.finditer(content):

                old_string = match.group(0)
                if old_string not in content:
                    continue

                i += 1
                new_string = convert(left, match.group(1), right, args, i)
                content = content.replace(old_string, new_string)
                if args.verbose:
                    print('[{}] {}'.format(i, old_string))

    if args.out is None:
        args.out = '{}.converted'.format(args.path)
    with open(args.out, 'w') as f:
        f.write(content)
    print('* Converted successfully: {}'.format(args.out))

if __name__ == '__main__':
    main()
