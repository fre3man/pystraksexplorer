from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

version = '1.1.0'

install_requires = [
    'requests',
]


setup(name='pystraksexplorer',
    version=version,
    description="Python wrapper for STRAKS block explorer api",
    long_description=README,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='straks blockexplorer crypto api',
    author='Freeman',
    author_email='fr3eman@protonmail.com',
    url='',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['pystraksexplorer=pystraksexplorer:main']
    }
)
