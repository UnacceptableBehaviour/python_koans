# python_koans
get up to speed on python with koans test driven learning

to run tests:
read README.rst

## Setup and run first test for (python 3):
```
$ cd /lang/python/repos/                    # repo directory
$ git clone https://github.com/gregmalcolm/python_koans
$ cd python3                                # to do the python3 test suite
$ python3 -m venv venv                      # setup environment
$ . venv/bin/activate                       # activate it
$ chmod +x ./contemplate_koans.py           # set permission to executable
$ ./contemplate_koans.py                    # execute tests


Thinking AboutAsserts
test_assert_truth has damaged your karma.

You have not yet reached enlightenment ...
AssertionError: False is not true           # <<    ERROR msg fro unit test

Please meditate on the following code:
File "/Users/simon/a_syllabus/lang/python/repos/python_koans/python3/koans/about_asserts.py", line 17, in test_assert_truth
self.assertTrue(False) # This should be True


You have completed 0 (0 %) koans and 0 (out of 37) lessons.
You are now 302 koans and 37 lessons away from reaching enlightenment.

Beautiful is better than ugly. (but I have the bottle opener!)
```
python sandbox - for testing python knowledge - simple scripts etc

## Auto run test after code change saved (README.rst):
```
$ . venv/bin/activate
$ pip install sniffer
$ pip install MacFSEvents                   # osx
$ sniffer                                   # have in a separeate report console - auto update
```
## Don't forget to modify .gitignore
```
*.pyc
*.swp
.DS_Store
answers
.hg
.idea
/python3/venv/
```


# REFERENCES:
## L1-3
### Unit test Framework - Python3
https://docs.python.org/3/library/unittest.html#

### Unit test methods
https://docs.python.org/3/library/unittest.html#assert-methods

### Decorators
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html
https://www.python-course.eu/python3_decorators.php
https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator  << Timing EG
used in scent.py

### Sniffer package
https://pypi.org/project/sniffer/

## L4-6
## Collections - improved alternatives
### to Python’s general purpose built-in containers, dict, list, set, and tuple
https://docs.python.org/3/library/collections.html#collections.deque

### Literal String Interpolation
https://www.python.org/dev/peps/pep-0498/

History and background
https://realpython.com/python-f-strings/

## L7-9
## Built in functions
https://docs.python.org/3/library/functions.html

## Built in types
https://docs.python.org/3/library/stdtypes.html

### String methods
https://www.w3schools.com/python/python_ref_string.asp

### timeit and EG Decorator
https://docs.python.org/3/library/timeit.html
https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator


```/python_koans/python3/koans/scratch_pad_0.py```
### Instance, Class, Static METHODS
https://realpython.com/instance-class-and-static-methods-demystified/

### Instance, Class, Static VARS
https://stackoverflow.com/questions/5690888/variable-scopes-in-python-classes


#### Aside - validating JSON
https://jsonlint.com/
#### Aside - JSON syntax
http://www.json.org/

### Documenting the cose with docstrings
https://www.geeksforgeeks.org/python-docstrings/

## L10-13
## Sets
https://www.programiz.com/python-programming/set

## Solution to no switch - using dict
### intersting syntax, neat solutions including default using .get(key, def_val)
https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python

## L14-L17
### Data Model  - a lot here!
https://docs.python.org/3/reference/datamodel.html

### Class Hierarchy, mro
https://stackoverflow.com/questions/2010692/what-does-mro-do
https://makina-corpus.com/blog/metier/2014/python-tutorial-understanding-python-mro-class-search-path

### Exceptions
https://docs.python.org/3/library/exceptions.html

### Error & Exceptions
https://docs.python.org/3/tutorial/errors.html

## Filter & Map

### difference
filter(by_this_function, data_to_filter)                # returns iterator   to get array list( filter(bla) )
map(apply_this_function, data_to_process)     # returns iterator   same for map

## Files
### great reference:
https://realpython.com/working-with-files-in-python/

### List comprehensions
https://www.programiz.com/python-programming/list-comprehension

## L18-21
### Generators - spec
http://www.python.org/dev/peps/pep-0342/    read spec summary quick overview! (and examples)

### Generators & Lazy evaluation  - when to use - back ground - better
## & Iterator pattern
https://www.freecodecamp.org/news/how-and-why-you-should-use-python-generators-f6fb56650888/

