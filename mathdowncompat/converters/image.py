from sympy import preview
import os


def initialize_arguments(parser):
     parser.add_argument('--image-assets', help='path to assets', 
                         default='assets')
     parser.add_argument('--image-url-prefix', help='prefix for all image urls',
                         default='')


def convert(left, expr, right, args, i):
     """Render all images and save on local disk or upload."""
     global count

     filename = '{}.png'.format(i)
     filepath = os.path.join(args.image_assets, filename)
     markdown = '![{}]({})'.format(i, os.path.join(args.image_url_prefix, filepath))

     expr = '{}{}{}'.format(left, expr, right)
     if not os.path.exists(args.image_assets):
         os.makedirs(args.image_assets, exist_ok=True)
     preview(expr, viewer='file', filename=filepath, euler=False)
     return markdown
