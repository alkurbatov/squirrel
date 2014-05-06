Options:
    * -p TIME, --period=TIME       - rotating period, e.g.: 1d10h20m;
                                     omit this option to start rotation immediately;
    * -w SRC, --work-dir=SRC       - path to working directory;
                                     you can specify several directories using ';' symbol as a separator;
    * -s DST, --storage-dir=DST    - path to storage directory;
    * --keep                       - do not delete files, only compress them;
    * -c CONFIG, --config=CONFIG   - path to configuration file;
                                     by default your current directory will be used;
    * -h, --help                   - brief help;
    * --version                    - show program's version number and exit.

Dev Options:
    * -d, --debug                  - stop from hiding Python exceptions.

Configuration:
    Squirrel has ability to use configuration files (examples can be found in 'conf' directory). Please pay attention that command line options have higher priority and will be used instead of ones specified in configuration file.

Dependencies:
    * python >= 2.6.6 (3.0+ is not supported) - http://www.python.org

    Optional:
        * pyinstaller 2.1 - http://www.pyinstaller.org

Supported platforms:
    * Linux
    * Windows

Coding style:
    * Maximum line length is 100 symbols.
    * No tabs only spaces.
    * Padding width is 4 spaces.
    * Trailing spaces are forbidden.
    * Each file must end with a blank line.

Commit rules:
    Each commit must have one of the following prefixes:
        * MINOR Small changes in the code.
        * MAJOR Significant changes in the code.
        * BUGFIX Fixed a bug.
        * REFACTORING Code refactoring.
        * STYLE Fixed indentation, removed trailing spaces and so on.
        * DOC Changes in documentation.

