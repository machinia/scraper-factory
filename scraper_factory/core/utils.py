from multiprocessing.queues import Queue


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
    return url.split('?')[0]
