from sympy import preview
import os
count = 0


def initialize_arguments(parser):
     parser.add_argument('--image-assets', help='path to assets', 
                         default='assets')
     parser.add_argument('--image-url-prefix', help='prefix for all image urls',
                         default='')


def convert(left, expr, right, args):
     """Render all images and save on local disk or upload."""
     global count
     count += 1

     filename = '{}.png'.format(count)
     markdown = '![{}]({}{})'.format(count, args.image_url_prefix, filename)

     expr = '{}{}{}'.format(left, expr, right)
     filename = os.path.join(args.image_assets, '{}.png'.format(count))
     if not os.path.exists(args.image_assets):
         os.makedirs(args.image_assets, exist_ok=True)
     preview(expr, viewer='file', filename=filename, euler=False)
     return markdown
