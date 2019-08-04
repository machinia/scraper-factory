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
    while q.qsize() != 0:
        arr.append(q.get())
    return arr
