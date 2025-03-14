# MLCoder

MLCoder is a Python package that provides a collection of frequently used code snippets for Machine Learning, offering a command-line interface (CLI) to search and copy files from its built-in repository. Users can easily install it via PyPI or GitHub and leverage its simple commands to quickly access useful scripts.

## Why This Repository?

Every developer maintains their own collection of familiar code snippets for various purposes. Typically, these snippets are stored in platforms like GitHub, requiring developers to manually search, open a browser, and copy the needed code—wasting valuable time. This repository streamlines that process by allowing developers to quickly search for and copy their code directly into their working directory. Additionally, developers can clone this project, customize it with their own codebase, and publish it to PyPI, enabling seamless access to their personal code library as a PyPI-backed module.

## Installation

You can install MLCoder from PyPI:

```sh
pip install mlcoder
```

Alternatively, install it directly from GitHub:

```sh
pip install git+https://github.com/hissain/mlcoder.git
```

## Usage

MLCoder provides a CLI utility to search and copy files from the package's `files` directory.

### Commands

- **`search`**: Search for files in the package's `files` directory.
- **`copy`**: Copy a specified file from the package's `files` directory to the current working directory.

### Examples

#### Search for a file

To search for files containing a specific term:

```sh
mlcoder search <search_term>
```

**Example:**

```sh
mlcoder search pretty
```

#### Copy a file

To copy a file from the package's `files` directory to the current working directory:

**Example:**

```sh
mlcoder copy pretty_print.py
```

## Project Links

- **GitHub:** [MLCoder Repository](https://github.com/hissain/mlcoder)
- **PyPI:** [MLCoder Package](https://pypi.org/project/mlcoder)

## License

This project is licensed under the MIT License.

