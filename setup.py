import os

from setuptools import setup, find_packages
from treeadmin import __version__ as version

setup(
    name = 'ls-django-treeadmin',
    version = version,
    description = 'Tree UI for mptt-managed models, extracted from FeinCMS',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author = 'Scott Sharkey, Matthias Kestenholz  et al.',
    author_email = 'ssharkey@lanshark.com',
    url = 'https://github.com/lanshark/ls-django-treeadmin',
    download_url = 'https://github.com/lanshark/ls-django-treeadmin/tarball/0.4.2',
    packages = find_packages(),
    zip_safe=False,
    include_package_data = True,
    install_requires=[
        'Django>=1.7',
        'django-mptt>=0.5',
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)
