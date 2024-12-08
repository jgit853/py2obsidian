# Py2Obsidian

A simple tool to automatically archive Python files into Obsidian vault with proper categorization and documentation.

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- Automatically archive desktop Python files to designated folders
- Generate Markdown documentation in Obsidian vault
- Smart categorization of Python files
- Complete source code preservation
- Duplicate file detection
- Customizable categorization rules

## Installation

```bash
# Clone the repository
git clone https://github.com/jgit853/tupao.git
cd tupao/py2obsidian

# Install requirements
pip install -r requirements.txt
```

## Quick Start

1. Configure your paths in `config.py`:
```python
SOURCE_PATH = r"path/to/your/desktop"
ARCHIVE_PATH = r"path/to/your/archive"
OBSIDIAN_PATH = r"path/to/your/obsidian/vault"
```

2. Run the script:
```bash
python src/py2obsidian.py
```

## Directory Structure After Archive

```
Python-Tools/
├── Data-Processing/
├── Text-Processing/
└── Utility/
```

## Configuration

You can customize the tool by modifying these settings:

- File categories
- Archive paths
- Documentation templates
- File processing rules

See `examples/example_config.py` for detailed configuration options.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first.

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- jgit853

## Acknowledgments

This project is part of the "tupao" tools collection, aimed at improving daily efficiency.
