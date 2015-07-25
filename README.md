pgqd (PgQ Ticker Daemon) on Docker
==================================

This image runs [pgqd](http://skytools.projects.pgfoundry.org/skytools-3.0/doc/pgqd.html), the PgQ ticker daemon.

The entrypoint for this image generates a pgqd configuration file from the environment variables provided to the container.

Environment Variables
---------------------

All environment variables are optional, although `PGQD_BASE_CONNSTR` will need to be set for typical usage unless you'd prefer to configure the daemon with [libpq environment variables](http://www.postgresql.org/docs/9.4/static/libpq-envars.html). More thorough documentation on valid configuration values can be found in the [pgqd documentation](http://skytools.projects.pgfoundry.org/skytools-3.0/doc/pgqd.html).

- `PGQD_BASE_CONNSTR`: `libpq` connection string, without dbname=
- `PGQD_LOGFILE`: where to log
- `PGQD_PIDFILE`: where to write pidfile
- `PGQD_INITIAL_DATABASE`: startup database to query for other databases
- `PGQD_DATABASE_LIST`: limit ticker to specific databases
- `PGQD_SYSLOG`: log to syslog
- `PGQD_SYSLOG_IDENT`
- `PGQD_CHECK_PERIOD`: how often to check for new databases
- `PGQD_RETRY_PERIOD`: how often to flush retry queue
- `PGQD_MAINT_PERIOD`: how often to do maintenance
- `PGQD_TICKER_PERIOD`: how often to run ticker
