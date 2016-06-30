### repeated tests

look at test_repeated.py.

study it. 

understand it, inside and out. 

now, never, ever, do that.

## parametrize

instead, do this:

    import pytest


    @pytest.mark.parametrize(['x', 'y', 'ans'],
                             [(1, 1, 2),
                              (1, 2, 3),
                              (1, 3, 4),
                              (1, 4, 5)])
    def test_addition(x, y, ans):
        assert x + y == ans

boom! now you've parametrized a test. check the output: it'll look a little different, and will automagically generate IDs for you. note that you can also make up your own ids, see `test_addition_ids` in test_params.py for this

## one more thing

you can still apply xfail and skip markers! test_addition_ids shows this off too.