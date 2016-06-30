## the basics

the basics of py.test are pretty basic:

    def test_passing():
        """ example of a passing test """
        assert 1 == 1

open a file, name it test_basics.py, write a function named test_passing, and add a single assert statement. once you've done this, you can run py.test:

    $ py.test
    =========================== test session starts ===========================
    platform darwin -- Python 3.5.1, pytest-2.8.5, py-1.4.31, pluggy-0.3.1
    rootdir: /Users/fwph/code/pytest-examples/1_basics, inifile: 
    collected 1 items 

    test_basics.py .

    ========================= 1 passed in 0.01 seconds ========================

congratulations! you've written a test. this isn't my favorite output, personally, but py.test has some arguments:

    $ py.test -v test_basics.py
    =========================== test session starts ===========================
    platform darwin -- Python 3.5.1, pytest-2.8.5, py-1.4.31, pluggy-0.3.1 -- /Users/fwph/anaconda/bin/python
    cachedir: .cache
    rootdir: /Users/fwph/code/pytest-examples/1_basics, inifile: 
    collected 1 items 

    test_basics.py::test_passing PASSED

    ======================== 1 passed in 0.00 seconds =========================

the `-v` argument makes your output a bit more verbose, showing one per test. check out test_basics.py for a failing test to see what that output looks like

## markers

most useful feature of py.test after the test-runner: markers

    import pytest


    @pytest.mark.xfail(reason="xfail mark example")
    def test_xfailing():
        """ example of an xfail test """
        assert 2 == 3

markers are the first (and main) feature you need to actually use an import statement to get ahold of. they're implemented as decorators ([read more here](https://realpython.com/blog/python/primer-on-python-decorators/)), and can change the way your tests run and are reported. in this example, the xfail decorator prevents your entire test run from failing because of one stupid test that we know is currently failing.

now when we run py.test:

    $ py.test -v -ra test_markers.py 
    =========================== test session starts ===========================
    platform darwin -- Python 3.5.1, pytest-2.8.5, py-1.4.31, pluggy-0.3.1 -- /Users/fwph/anaconda/bin/python
    cachedir: .cache
    rootdir: /Users/fwph/code/pytest-examples/1_basics, inifile: 
    collected 1 items 

    test_markers.py::test_xfailing xfail
    ========================= short test summary info =========================
    XFAIL test_markers.py::test_xfailing
      xfail mark example

    ======================== 1 xfailed in 0.01 seconds ========================


we can see that something failed. 

note also in this test run the addition of the `-ra` option: this just gives a summary of information about tests that didn't just pass normally; it's a pretty handy flag.

note that when tests are xfailed this way, they actually do run, so when they start passing again, py.test will let you know. check test_markers.py for an example of an *xpass* test.

## one more thing!

py.test has a bunch of command line arguments, and chances are you'll pick a few you really like. pytest.ini is here to save you from having to rewrite them all the time. check out the pytest.ini in this directory and others to see the basics.

#### even one more

you can also mark tests as skip. there's an example of that too. note that the skip marker doesn't work on pytest less than 2.9, and also that there is a 'skipif' marker which i don't demonstrate.