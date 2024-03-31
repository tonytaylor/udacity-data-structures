
## Working with cProfile for Performance Analysis

```python
"""Generating a Profile"""
import cProfile
# import Task2
cProfile.run('Task2.run()', 'Task2.stats')

"""Loading/Printing a profile"""
import pstats
from pstats import SortKey
p = pstats.Stats("Task2.stats")
p.strip_dirs().sort_stats(-1).print_stats()
```