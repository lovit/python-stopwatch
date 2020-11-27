# Python-Stopwatch

## Install

- from source
```
git clone https://github.com/lovit/python-stopwatch
cd python-stopwatch
python setup.py install
```

## Usage

- `log` function print message attached elapsed time and write it to `logpath`
```python
from stopwatch import Stopwatch

with Stopwatch('Task description', logpath='log.txt') as t:
    sleep(1)
    # do some tasks
    t.log('write result with record time to `logpath`')
```
```
[Task description] 1.002 sec. write result with record time to `logpath`
```

- `log` function in silent mode Stopwatch just write message attached elapsed time to `logpath`
```python
with Stopwatch('Task description', logpath='log_silent.txt', silent=True) as t:
    # do some tasks
    sleep(1)
    t.log('write result with record time to `logpath`, but not print')
```

- `record` function only print `message` and elapsed time
```python
with Stopwatch('Task description') as t:
    # do some tasks
    sleep(1)
    t.record('print messages with record time')
```
```
[Task description] 1.001 sec. print messages with record time
```

- With current time
```python
with Stopwatch('Task description', now=True) as t:
    # do some tasks
    sleep(1)
    t.record('print messages with record time')
```
```
[Task description] [2020-11-28 08:05:20] 1.001 sec. print messages with record time
```

- Without `description`
```python
with Stopwatch(now=True) as t:
    # do some tasks
    sleep(1)
    t.record('print messages with record time')
```
```
[2020-11-28 08:05:24] 1.001 sec. print messages with record time
```

- Use as Python package
```python
stopwatch = Stopwatch('Task description', now=True)
for n_iter in range(5):
    sleep(1)
    stopwatch.record(f'{n_iter} th iteration')
```
```
[Task description] [2020-11-28 08:08:18] 1.001 sec. 0 th iteration
[Task description] [2020-11-28 08:08:19] 2.002 sec. 1 th iteration
[Task description] [2020-11-28 08:08:20] 3.004 sec. 2 th iteration
[Task description] [2020-11-28 08:08:21] 4.005 sec. 3 th iteration
[Task description] [2020-11-28 08:08:22] 5.006 sec. 4 th iteration
```