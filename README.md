# GildedRose-Refactoring-Kata-Python

This repository contains my implementation of the GildedRose-Refactoring-Kata in Python
that you can find here: [https://github.com/emilybache/GildedRose-Refactoring-Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata).

The code respects the following requirements: [https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/GildedRoseRequirements.txt](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/GildedRoseRequirements.txt).

## Requirements

- Python3

## Quick start

To create the virtual environment and install the dependencies:

```bash
make init
```

### Unit tests

You can run the tests by executing:

```bash
make test
```

### TextTest

If you wish to run the `TextTest`, you need to install it first.
Depending on your OS, you can follow the instructions [here](http://texttest.sourceforge.net/index.php?page=download) and [here](http://texttest.sourceforge.net/index.php?page=documentation_trunk&n=install_texttest).  
You basically need to install PyGTK and texttest.

(On OSX, it can be as simple as `brew install pygtk` and `pip2 install texttest`)

Then run it:

```bash
TEXTTEST_HOME=$(pwd)/texttests texttest -a gr
```

### Coverage

To get the coverage report, run:

```bash
make coverage
```

It will generate the HTML report in `htmlcov`.

## Formatter

The code is formatted using `yapf`: [https://github.com/google/yapf](https://github.com/google/yapf).
