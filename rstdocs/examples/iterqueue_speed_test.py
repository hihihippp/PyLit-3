# iterqueue_speed_test.py
# =======================
# Profiling the iterqueue extended iterator classes
# -------------------------------------------------
#
# ::

import sys, os, itertools
from timeit import Timer
import iterqueue
from iterqueue_test import wrappers, peekables, pushables, \
     state_reporters, iqueues


def print_iterator_lists():
    print( "Wrappers" )
    print( " ","\n  ".join(wrapper.__name__ for wrapper in wrappers) )
    print( "Peekables" )
    print( " ","\n  ".join(peekable.__name__ for peekable in peekables) )
    print( "Pushables" )
    print( " ","\n  ".join(pushable.__name__ for pushable in pushables) )
    print( "State Reporters" )
    print( " ","\n  ".join(state_reporter.__name__
                     for state_reporter in state_reporters) )
    print( "Iterator Queues" )
    print( " ","\n  ".join(iqueue.__name__ for iqueue in iqueues) )


#print_iterator_lists()

# use cases (benchmarks)
# ~~~~~~~~~~~~~~~~~~~~~~
#
# ::

def loop(iterator):
    """baseline: empty `for` loop"""
    for _ in iterator:
        pass

def peek_in_loop(iterator):
    """peek in every loop"""
    for _ in iterator:
        try:
            iterator.peek()
        except StopIteration:
            pass

def peek_before_loop(iterator):
    """peek at first value once, then loop"""
    try:
        iterator.peek()
    except StopIteration:
        pass
    for _ in iterator:
        pass

def bool_in_loop(iterator):
    """test for values in every loop"""
    for _ in iterator:
        bool(iterator)

def bool_before_loop(iterator):
    """test for values once, then loop"""
    bool(iterator)
    for _ in iterator:
        pass


def time_benchmark(fun, wrappers, iterator):
    """profile benchmark `fun` with `iterator` wrapped in `wrappers`"""

    print( fun.__doc__, "({0:s})".format(iterator) )
    setup = "import iterqueue_speed_test\nimport iterqueue"
    benchmark = "iterqueue_speed_test.{0!s}(iterqueue.{1!s}(iter({2!r})))"
    stmts = [benchmark.format(fun.__name__, wrapper.__name__, iterator)
             for wrapper in wrappers]
    timers = [Timer(stmt=stmt, setup=setup) for stmt in stmts]

    t_i = [min(timer.repeat(number=1, repeat=3)) for timer in timers]

    results = ["%.5f s   %s"%(t, wrapper.__name__)
               for t, wrapper in zip(t_i, wrappers)]
    results.sort()
    print( "\n".join(results) )

# Typical use case: ``time_benchmark(loop, [iterqueue.XIter], xrange(1000))``
#
# ::

time_benchmark(loop, wrappers, range(1000))
print()
time_benchmark(peek_before_loop, peekables, range(1000))
print()
time_benchmark(peek_in_loop, peekables, range(1000))
print()
time_benchmark(bool_before_loop, state_reporters, range(1000))
print()
time_benchmark(bool_in_loop, state_reporters, range(1000))

