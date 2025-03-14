from setuptools import setup, find_packages

setup(
    name='mlcoder',
    version='0.1.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
    ],
    author='Md. Sazzad Hissain Khan',
    author_email='hissain.khan@gmail.com',
    description='MLCoder is a Python package that provides a collection of frequently used code snippets for Machine Learning, offering a command-line interface (CLI) to search and copy files from its built-in repository. Users can easily install it via PyPI or GitHub and leverage its simple commands to quickly access useful scripts.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hissain/mlcoder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    package_data={
        "mlcoder": ["files/**/*"],
    },

    entry_points={
        'console_scripts': [
            'mlcoder=mlcoder.cli:main',
        ],
    },
)
