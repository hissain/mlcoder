# setup.py

from setuptools import setup, find_packages

setup(
    name='mlcoder',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    author='Md. Sazzad Hissain Khan',
    author_email='hissain.khan@gmail.com',
    description='Get the collection of Python code used frequently in Machine Learning using pip package :).',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hissain/mlcoder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)