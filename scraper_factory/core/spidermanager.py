import os
import re
import ast
import importlib.util
from scraper_factory.core import base_spider

HERE = os.path.abspath(os.path.dirname(__file__))
DEFAULT_PATH = os.path.join(HERE, os.path.pardir, 'spiders')


class SpiderManager(object):
    VALID_FILE_REGEX = r'(([a-zA-Z0-9]+)|-|_)+[^__]\.py'

    def __init__(self):
        path = os.getenv('SPIDER_PATH', DEFAULT_PATH)
        if not os.path.isdir(path):
            raise AttributeError('Invalid path {}'.format(path))

        self.spiders = {}
        self.load(path)

    def load(self, path):
        """
        Loads all the valid spiders found in the path received
        :param path: string with the path to a folder where spiders are stored
        :return: Nothing
        """
        self.spiders = {}
        for f in os.listdir(path):
            if not re.match(self.VALID_FILE_REGEX, f):
                continue

            spider_file = os.path.join(path, f)
            try:
                sp = self.__load_spider_from_file(spider_file)
                metadata = sp.metadata
                self.spiders[metadata['name']] = sp.metadata
                self.spiders[metadata['name']]['instance'] = sp
            except (AttributeError, ImportError) as e:
                print('Skipped {}: {}'.format(f, e))
                continue

    def __load_spider_from_file(self, filename):
        """
        Loads a spider from a certain file. The file must contain
        only one class, derived from BaseSpider
        :param filename: string containing the path to the definition
        of a spider
        :return: constructor of the class if it was properly loaded,
        None otherwise
        """
        with open(filename) as f:
            node = ast.parse(f.read())

        classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
        if len(classes) > 1:
            raise AttributeError('File can\'t contain more than one class')
        spider_name = classes[0].name

        spec = importlib.util.spec_from_file_location(
            spider_name, filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.__validate_module(module, spider_name)

        return getattr(module, spider_name)

    def __validate_module(self, module, classname):
        """
        Validates that the module received is a valid spider definition
        :param module: python module
        :return: Nothing. Raises exception on failure.
        """
        cls = getattr(module, classname)
        base_spider.BaseSpider.check_metadata(cls.metadata)

        if not issubclass(cls, base_spider.BaseSpider):
            msg = '{} found doesn\'t derive from BaseSpider'.format(classname)
            raise ImportError(msg)

        base_spider.BaseSpider.check_metadata(cls.metadata)

    def instance(self, name):
        """
        Returns the constructor to the class with a given name.
        :param name: string with the spider name
        : return: constructor of the desired class. None on error.
        """
        sp = self.spiders.get(name)
        if not sp:
            return None

        return sp.get('instance')

    def get_spiders(self):
        """
        Returns a list with the metadata of all available spiders
        :return: list of dicts containing spider metadata
        """
        arr = []
        for name, metadata in self.spiders.items():
            arr.append(
                {k: v for k, v in metadata.items() if k not in 'instance'})
        return arr
