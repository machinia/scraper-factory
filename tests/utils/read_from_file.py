import os
import ast
from scrapy.http import HtmlResponse, Request


def response_from_file(filename, url=None):
    """
    Creates a HtmlResponse object based in the content of a html file
    :param filename: filename or path to a html file
    :return: HtmlResponse object with the data fetched from a file
    """
    if not url:
        url = 'http://www.fakeurl.com'

    request = Request(url=url)
    if not filename[0] == '/':
        responses_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "htmls"))
        file_path = os.path.join(responses_dir, filename)
    else:
        file_path = filename

    file_content = open(file_path, 'r').read()

    response = HtmlResponse(
        url=url, request=request, body=file_content, encoding='utf-8')
    return response


def read_results_from_file(filename):
    """
    Reads results saved in a file and returns an array with a dictionary
    (if the result is a valid json) or string otherwise
    :param filename: file name where results are stored
    :return: list of results, which may be either str or dict
    """
    if not filename[0] == '/':
        responses_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "scraped_data"))
        file_path = os.path.join(responses_dir, filename)
    else:
        file_path = filename

    arr = []
    with open(file_path, 'r') as f:
        for line in f:
            try:
                item = ast.literal_eval(line)
            except (ValueError, SyntaxError):
                item = str(line)
            arr.append(item)

    return arr
