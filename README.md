 

# pyjdwp: Python JDWP Library for Debugging Java Programs

`pyjdwp` is an Python library designed for debugging Java programs through the Java Debug Wire Protocol (JDWP). 
This is a fork of the original repo ([https://github.com/csuter/pyjdb](https://github.com/csuter/pyjdb)) updated for Python 3 compatibility and extended to support the specification files of later OpenJDK versions. 
Currently, the library debugs Java versions 6 to 23.

## Changes to the original repo

- **Python 3 Support**: Updated for compatibility with Python 3.
- **Extended JDWP Specification Support**: Includes JDWP specifications for OpenJDK versions 6 through 23.
- **Structure**: Changed project structure for ease of navigation and extension. Renamed pyjdp folder to pyjdwp as it is more faithful to what the library does.


## Project Structure

```
pyjdwp/
├── pyjdwp/                 # Main library modules
│   ├── __init__.py
│   ├── pyjdb.py
│   ├── pyjdwp.py
│   ├── sexpr_helpers.py
│   └── specs/              # JDWP specifications by JDK versions
│       ├── jdwp.spec_openjdk_[6-23]
├── tests/                  # Unit and functional tests
│   ├── __init__.py
│   ├── pyjdb_test.py
│   └── pyjdwp_test.py
├── README.md
├── setup.py                # Installation script
└── test.sh                 # Script to run tests
```


## Dependencies

- JDK (version corresponding to your target application)
- Python 3.9 or newer
- pyparsing

## Installation

Clone this repository and run the `setup.py` script to install `pyjdwp`:

```bash
git clone https://github.com/yourusername/pyjdwp.git
cd pyjdwp
python setup.py install
```

## Running Tests

To verify the installation and functionality, you can run the provided test script:

```bash
./test.sh
```

Ensure you have the necessary JDK and Python versions installed before running the tests.
 