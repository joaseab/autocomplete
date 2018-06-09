# Autocomplete

Simple autocomplete python program.

## Running the Program

You can run the program interactively in two ways:

### 1. In a web browser (`appweb.py`)

```
	python appweb.py --corpus <filepath>
```

where *filepath* is the path to the corpus file (.csv).

Optional script arguments:

	--casesensitive

		This flag sets case-sensitive search. default is case-insensitive.

	--nmin <N> 
		
		sets the minimum number of letters for calling the search. (default is 1)

	--help 

		shows the possible arguments

####
Example:

```
	python appweb.py --corpus data/6500titles.csv
```

Run this command at the root of the autocomplete folder. Open with a browser
the link that shows at the terminal.


**At the browser, insert in the text box the query string.**
**You must press the submit button (or enter return), and the list of completions are shown.**


Calling:

```
	python appweb.py --corpus data/6500titles.csv --casesensitive
```

Will make the search case-sensitive.


### 2. At the terminal (`appcomm.py`)

This is a mockup test. The script arguments are the same as for appweb.py.

Example:

```
	python appcomm.py --corpus data/6500titles.csv
```

Run this command at the root of the autocomplete folder. 
Insert a query string and press enter. The list of completions are shown.


## Running the unitary tests

To run the tests, call at the terminal

```
	python -m unittest -v tests
```

## Dependencies

You need to have flask installed (e.g. install it via pip).


## Description of the contents

### trie.py

This module implements the Prefix Tree.

### autocomplete.py

This module implements the AutoComplete engine, responsible for loading the
corpus, setting up the prefix tree, and for providing a method that retrieves completions.

### appweb.py

This module uses flask and the AutoComplete engine to launch a simple
web app that retrieves completions when queried.

### appcomm.py

This module is a mockup test of the webapp, to be used at the 
terminal.

### parsecommands.py

This module contains utils for parsing the commandline arguments.

### tests.py

This module uses unittest to test both the trie.py and autocomplete.py

### templates/autocomplete.html

This is the html template used by flask to receive queries and return results.

### data/*.csv

Contains corpus test data.


## Authors

* **Joao Seabra** - (https://github.com/joaseab)
