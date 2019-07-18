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
### Unit test Framework - Python3
https://docs.python.org/3/library/unittest.html#

### Unit test methods
https://docs.python.org/3/library/unittest.html#assert-methods

### Decorators
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html
used in scent.py

### Sniffer packaeg
https://pypi.org/project/sniffer/



# Notes


