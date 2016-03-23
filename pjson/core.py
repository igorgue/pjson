import json
import sys
from pygments import highlight
from pygments.formatters import TerminalFormatter
from xml.etree import ElementTree as ET
import xmlformatter


def format_code(data, is_xml=False):
    """
    Parses data and formats it
    """
    if is_xml:
        ET.fromstring(data)  # Make sure XML is valid
        formatter = xmlformatter.Formatter(indent=2, indent_char=' ',
                                           encoding_output='UTF-8',
                                           preserve=['literal'])
        return formatter.format_string(data)
    else:
        obj = json.loads(data)

        return json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False).encode('UTF-8')


def color_yo_shit(code, lexer):
    """
    Calls pygments.highlight to color yo shit
    """
    if sys.version_info >= (3, 0):
        text = str(code, 'UTF-8')
    else:
        text = unicode(code, 'UTF-8')

    return highlight(text, lexer, TerminalFormatter())
