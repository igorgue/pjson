#!/usr/bin/env python

"""
Command-line tool to validate and pretty-print JSON and XML.

Based on `python -mjson.tool` but without the crap.

Usage::

    $ echo '{"json":"obj"}' | pjson
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | pjson
    Expecting property name: line 1 column 2 (char 2)


Author: Igor Guerrero <igfgt1@gmail.com>, 2012
"""

import json
import sys
if sys.version_info[0] == 2:
    from StringIO import StringIO
else:
    from io import StringIO
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import JsonLexer, XmlLexer
from xml.etree import ElementTree as ET
import xmlformatter
import argparse

__version__ = '0.5'

def format_code(data, is_xml=False):
    """
    Parses data and formats it
    """
    if is_xml:
        ET.fromstring(data)  # Make sure XML is valid
        formatter = xmlformatter.Formatter(indent=2, indent_char=' ', encoding_output='UTF-8', preserve=['literal'])
        return formatter.format_string(data)
    else:
        obj = json.loads(data)
        output = StringIO()

        json.dump(obj, output, sort_keys=True, indent=2)
        return output.getvalue()

def color_yo_shit(code, lexer):
    """
    Calls pygments.highlight to color yo shit
    """
    return highlight(code, lexer, TerminalFormatter())

def main():
    """
    Main function to execute everything in order
    """
    parser = argparse.ArgumentParser(description="Command-line tool to validate and pretty-print JSON and XML")
    parser.add_argument("-x", action="store_true", help="Data is XML")
    parser.add_argument("-b", action="store_true", help="Read data in chunks")
    parser.add_argument("-t", action="store_true", help="Colorize regardless if output is a terminal")
    args = parser.parse_args()

    if args.x and args.b:
        sys.stderr.write("-x and -b cannot be used simultaneously\n")
        parser.print_usage(sys.stderr)
        exit(1)

    colorize = args.t or sys.stdout.isatty()

    if args.b:
        for line in sys.stdin:
            text = format_code(line)
            if colorize:
                text = color_yo_shit(text, JsonLexer())
            print(text)
    else:
        data = sys.stdin.read()
        try:
            text = format_code(data, args.x)
            if colorize:
                text = color_yo_shit(text, XmlLexer() if args.x else JsonLexer()).rstrip('\r\n')
            print(text)
        except (ValueError, ET.ParseError) as e:
            message = str(e)
            if colorize:
                red = '\x1b[31;m'
                reset_colors = '\x1b[0;m'
                message = ''.join([red, message, reset_colors])
            sys.stderr.write(message+'\n')
            exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(1)
