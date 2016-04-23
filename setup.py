from setuptools import setup, find_packages
import prboard


def read(path):
    with open(path, 'rb') as f:
        return f.read().decode('utf-8')


setup(
    name="prboard",
    version=prboard.__version__,
    url="https://github.com/kumarvaradarajulu/prboard",
    author="Kumar Varadarajulu",
    author_email="kumarvaradarajulu@gmail.com",
    description=prboard.__description__,
    long_description='\n' + read('README.md'),
    download_url=(
        'https://github.com/kumarvaradarajulu/prboard/tag/v'
        + prboard.__version__
    ),
    include_package_data=True,
    packages=find_packages(),
    package_data={'prboard': ['README.md']},
    zip_safe=False,
    install_requires=[
        'prboard',
        'argparse',
        'PyGithub',
        'six',
        'mock',
    ],
    entry_points={
        'console_scripts': [
            'prboard=prboard.main:main'
        ]
    },
    dependency_links=[]
)