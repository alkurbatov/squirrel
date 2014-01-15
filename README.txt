Options:
    * -p TIME, --period=TIME       - rotating period, e.g.: 1d10h20m;
    * -w PATH, --work-dir=PATH     - path to working directory;
    * -h, --help                   - brief help;
    * --version                    - show program's version number and exit.

Dev Options:
    * -d, --debug                  - stop from hiding Python exceptions;
    * --dry-run                    - do not delete files, only compress them.

Dependencies:
    * python 2.7.5 - http://www.python.org

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

