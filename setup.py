import os
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*folders):
    with codecs.open(os.path.join(here, *folders), encoding='utf-8') as f:
        return f.read()


def get_requirements(file_name):
    requires_file = read('requirements', file_name)
    return requires_file.splitlines()


long_description = read('README.rst')

setup(
    name='scraper-factory',

    version='0.2.1',

    description='Scraping library to retrieve data from useful pages, such as Amazon wishlists',
    long_description=long_description,

    url='https://github.com/machinia/scraper-factory',

    author='Pablo Ahumada, Jorge Capona',
    author_email='pablo.ahumadadiaz@gmail.com, jcapona@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: System',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='scraping wishlist amazon',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=get_requirements('default.txt'),
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
    test_suite='tests',
    setup_requires=get_requirements('tests.txt'),
)