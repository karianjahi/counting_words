# counting_words
This module is supposed to count words in a string without exception. By exception, we mean every string irrespective of how it looks like.

### `count_words.py`
This is the main module that counts words

### `test_count_words.py`
This is the file that tests the `count_words.py`

Since we want to conform to PEP8 convection, we are going to use a linter to render our code.

In this case we are going to use `pylint`

We created a virtual env for this module using: `virtualenv -p python3.8 word_counting_env`

This ensures that there is no pre-installed python modules. It is just empty.

To activate this environment:
`source word_counting_env/bin/activate`

### NOTE:
Always start with a failing test to make sure that your tests are being read!

### Code coverage
It is important to measure coverage of your code to detect lines which have not been touched by tests. The aim is to make sure that every line is touched by tests.

To test coverage we need a module known as `coverage`

**How to test coverage**

`pytest --cov`

Make sure you install the module `pytest-cov`

This displays the coverage in the terminal

`coverage html`

This creates a folder which has among other files, an `index.hmtl` that you can open in your favourite browser to assess the coverage of your tests.

To open the coverage hmtl page, use the command:

`firefox htmlcov/index.html`

Usually, you can wrap all the commands in a bash file. The bash file will have all the commands necessary to run the tests and coverage

We can create the bash file and call it `run_tests_and_coverage.sh`.

### Note
A bash file must always start with `#!/bin/bash` to tell the system that this is actually a bash file

Then put all the test commands into the bash file

Make it executable: `chmod u+x file.sh`

To run it:  `./file.sh`


### Continuous Integration
This is a smoke detector to our Application. It tells us when something goes wrong with our package

#### How does it work:
1. Create a virtual machine
2. clone the rep
3. install libraries
4. run tests and other automatic checks -- pylint!
5. The tests should pass and if they don't, notify the developer through email or a message.

### How do we implement Continuous Integration:
1. Create a workflow: This involvs creates a .github/workflows folder. In the workflows folder we need a yml file that instructs the virtual machine on what to do once we push the code.



