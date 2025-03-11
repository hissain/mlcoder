# setup.py

from setuptools import setup, find_packages

setup(
    name='mlcoder',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Define your command line scripts here
        ],
    },
    author='Md. Sazzad Hissain Khan',
    author_email='hissain.khan@gmail.com',
    description='Fun utilities to write piece of Python codes used frequently in Machine Learning',
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