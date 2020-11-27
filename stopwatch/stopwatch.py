import os
from datetime import datetime
from time import time, sleep


class Stopwatch:
    """
    Args:
        desc (str, optional) : Task description
        form (str, optional) : elapsed time format. Default is '%.3f'
        logpath (str, optional) :
            If it is set, stopwatch writes and print message
        logmode (str, optional) :
            If `logmode` is `reset`, it erases `logpath`
        now (bool, optional) :
            If True, it attachs current time at print message as '%Y-%m-%d %H:%M:%S' format
        silent (bool, optional) :
            If True, it only writes messages with elapsed time

    Examples:
        `log` function print message attached elapsed time and write it to `logpath`

            >>> with Stopwatch('Task description', logpath='log.txt') as t:
            >>>     sleep(1)
            >>>     # do some tasks
            >>>     t.log('write result with record time to `logpath`')
            $ [Task description] 1.002 sec. write result with record time to `logpath`


        `log` function in silent mode Stopwatch just write message attached elapsed time to `logpath`

            >>> with Stopwatch('Task description', logpath='log_silent.txt', silent=True) as t:
            >>>     # do some tasks
            >>>     sleep(1)
            >>>     t.log('write result with record time to `logpath`, but not print')

        `record` function only print `message` and elapsed time

            >>> with Stopwatch('Task description') as t:
            >>>     # do some tasks
            >>>     sleep(1)
            >>>     t.record('print messages with record time')
            $ [Task description] 1.001 sec. print messages with record time

        With current time

            >>> with Stopwatch('Task description', now=True) as t:
            >>>     # do some tasks
            >>>     sleep(1)
            >>>     t.record('print messages with record time')
            $ [Task description] [2020-11-28 08:05:20] 1.001 sec. print messages with record time

        Without `description`

            >>> with Stopwatch(now=True) as t:
            >>>     # do some tasks
            >>>     sleep(1)
            >>>     t.record('print messages with record time')
            $ [2020-11-28 08:05:24] 1.001 sec. print messages with record time

        Use as Python package

            >>> stopwatch = Stopwatch('Task description', now=True)
            >>> for n_iter in range(5):
            >>>     sleep(1)
            >>>     stopwatch.record(f'{n_iter} th iteration')
            $ [Task description] [2020-11-28 08:08:18] 1.001 sec. 0 th iteration
            $ [Task description] [2020-11-28 08:08:19] 2.002 sec. 1 th iteration
            $ [Task description] [2020-11-28 08:08:20] 3.004 sec. 2 th iteration
            $ [Task description] [2020-11-28 08:08:21] 4.005 sec. 3 th iteration
            $ [Task description] [2020-11-28 08:08:22] 5.006 sec. 4 th iteration
    """
    def __init__(self, desc=None, form='%.3f', logpath=None, logmode='reset', now=False, silent=False):
        desc = '' if desc is None else f'[{desc}]'
        self.desc = desc
        self.form = form
        self.logpath = logpath
        self.logmode = logmode
        self.now = now
        self.silent = silent
        self._begin_event = time()
        self._init_logpath(logpath, logmode)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        elapsed_time = time() - self._begin_event
        return elapsed_time

    def _init_logpath(self, logpath, logmode):
        if logpath is None:
            return
        dirname = os.path.dirname(os.path.abspath(logpath))
        os.makedirs(dirname, exist_ok=True)
        if logmode == 'reset':
            with open(logpath, 'w', encoding='utf-8') as f:
                f.write('')

    def _prepare(self, t, message):
        if message is None:
            message = ''
        t_str = self.form % (t)
        if self.now:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            now = f' [{now}]'
        else:
            now = ''
        return f'{self.desc}{now} {t_str} sec. {message}'.strip()

    def log(self, message=None):
        """
        Print and write message with elapsed time [and now]

        Args:
            message (str, optional)
        """
        t = time() - self._begin_event
        line = self._prepare(t, message)
        if not self.silent:
            print(line)
        if self.logpath is not None:
            with open(self.logpath, 'a', encoding='utf-8') as f:
                f.write(f'{line}\n')

    def record(self, message=None):
        """
        Print message with elapsed time [and now]

        Args:
            message (str, optional)
        """
        t = time() - self._begin_event
        print(self._prepare(t, message))

    def reset(self):
        """
        Reset base time
        """
        self._begin_event = time()
