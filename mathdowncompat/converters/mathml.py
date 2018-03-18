import asciimathml
from xml.etree.ElementTree import tostring


def initialize_arguments(_):
     pass


def convert(_, expr, __, ___, i):
     """Converts expression into MathML

     As of time of writing, MathML is only supported by Firefox and Safari.
     Chrome support has been proposed.
     """
     return tostring(asciimathml.parse(expr)).decode('utf-8')
