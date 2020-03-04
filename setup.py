from setuptools import setup
from os import path

version = '0.1.0'

repo_base_dir = path.abspath(path.dirname(__file__))

# Long description
readme = path.join(repo_base_dir, 'README.md')
with open(readme) as f:
    long_description = f.read()

setup(
    name='powerline-cpu-temp',
    version=version,
    description='A Powerline segment to show CPU temperature',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='DCsunset',
    author_email='DCsunset@protonmail.com',
    license='MIT',
    url='https://github.com/DCsunset/powerline-cpu-temp',

    install_requires=['psutil'],
    # Add to lib so that it can be included
    py_modules=['powerline_cpu_temp'],

    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)
