from multiprocessing.queues import Queue
from urllib.parse import urlparse


def queue_to_list(q):
    """
    Transforms a multiprocessing queue into an array
    :param q: multiprocessing Queue object
    :return: list with the elements from the queue
    """
    if not isinstance(q, Queue):
        raise TypeError('Argument must be a multiprocessing Queue')

    arr = []
    while not q.empty():
        arr.append(q.get())
    return arr


def remove_query_string(url):
    """
    Removes query string from a url
    :param url: string with a url
    :return: clean base url
    """
    if not isinstance(url, str):
        raise TypeError('Argument must be a string')
    return url.split('?')[0]


def validate_url(url):
    """
    Checks that the given string contains valid url
    :param url: string with a url
    :return: True if url is valid, False otherwise
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except (ValueError, TypeError, AttributeError):
        return False
