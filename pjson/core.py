import json
import sys
if sys.version_info[0] == 2:
    from StringIO import StringIO
else:
    from io import StringIO
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
        output = StringIO()

        json.dump(obj, output, sort_keys=True, indent=2)
        return output.getvalue()


def color_yo_shit(code, lexer):
    """
    Calls pygments.highlight to color yo shit
    """
    return highlight(code, lexer, TerminalFormatter())
