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

import sys
import signal
from sys import exit
from xml.etree import ElementTree as ET

__version__ = '1.0'


def _main():
    """
    Main function to execute everything in order
    """
    import argparse
    from pygments.lexers import JsonLexer, XmlLexer
    from pjson.core import format_code, color_yo_shit

    parser = argparse.ArgumentParser(description="Command-line tool to "
                                     "validate and pretty-print JSON and XML")
    parser.add_argument("-x", action="store_true", help="Data is XML")
    parser.add_argument("-b", action="store_true", help="Read data in chunks")
    parser.add_argument("-t", action="store_true", help="Colorize regardless "
                        "if output is a terminal")
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

def main():
    """
    Wrapper main function that handles broken pipes and keyboard interrupts.
    """
    # Lifted from pep8.py located here:
    # https://github.com/jcrocholl/pep8/blob/1.6.2/pep8.py#L2095-L2099
    # Many thanks!
    # Handle "Broken pipe" gracefully
    try:
        signal.signal(signal.SIGPIPE, lambda signum, frame: sys.exit(1))
    except AttributeError:
        pass    # not supported on Windows

    try:
        _main()
    except KeyboardInterrupt:
        exit(1)
