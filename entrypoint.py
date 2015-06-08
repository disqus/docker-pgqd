#!/usr/bin/env python
import os
import tempfile


# Configuration keys are translated into their corresponding environment
# variables by uppercasing and prefixing with `PGQD_`, e.g. `PGQD_LOGFILE`.
keys = {
    'logfile',
    'pidfile',
    'base_connstr',
    'initial_database',
    'database_list',
    'syslog',
    'syslog_ident',
    'check_period',
    'retry_period',
    'maint_period',
    'ticker_period',
}

configuration = {}
for key in keys:
    value = os.environ.get('PGQD_%s' % (key.upper(),))
    if value is not None:
        configuration[key] = value


destination = tempfile.NamedTemporaryFile(prefix='pgqd-', suffix='.ini', delete=False)
destination.write('[pgqd]\n\n')
for key, value in configuration.items():
    destination.write('%s = %s\n' % (key, value,))

destination.flush()
destination.close()


os.execvp('pgqd', ('pgqd', destination.name))
