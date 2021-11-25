# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
long_description = "ParcourSup.py : un clone en Python 3 de ParcoursSup, écrit à but didactique"
README = path.join(here, "README.rst")
if not path.exists(README):
    README = path.join(here, "..", "README.rst")
if not path.exists(README):
    README = path.join(here, "README.md")
if not path.exists(README):
    README = path.join(here, "..", "README.md")
if path.exists(README):
    with open(README, encoding="utf-8") as f:
        long_description = f.read()
        # print("Using a long_description of length,", len(long_description), "from file", README)  # DEBUG


version = "1.0.0"
try:
    from parcoursup import __version__ as version
except ImportError:
    print("Error: cannot import version from parcoursup.")
    print("Are you sure you are building in the correct folder?")

setup(name="parcoursup",
    version=version,
    description="ParcourSup.py : un clone en Python 3 de ParcoursSup, écrit à but didactique",
    long_description=long_description,
    author="Lilian Besson",
    author_email="naereen AT crans DOT org".replace(" AT ", "@").replace(" DOT ", "."),
    url="https://github.com/ravindu01manoj/ParcourSup.py/releases/",
    download_url="https://github.com/ravindu01manoj/ParcourSup.py/releases/",
    license="MIT",
    platforms=["GNU/Linux"],
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="parcoursup, python3, clone-libre, open-source, france, exemple, lycee, education-nationale, visualisations, algorithmes",
    # py_modules=["parcoursup"],
    packages=[
        "parcoursup",
        "parcoursup.ordreappel",
        "parcoursup.propositions",
    ],
    install_requires=[
        "numpy",
        "tqdm >= 4.0",
        "jupyter",
        "ipython",
        "watermark",
        "ipythonblocks",
        "sphinx",
        "sphinx_rtd_theme",
        "recommonmark",
    ],
    package_data={
        'parcoursup': [
            'LICENSE',
            'README.md',
            # FIXME add the xml data used in the tests
            'donnees/*.xml',
            'donnees/*.json',
        ]
    },
    
)

# End of setup.py
