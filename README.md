pgqd (PgQ Ticker Daemon) on Docker
==================================

This image runs [pgqd](http://skytools.projects.pgfoundry.org/skytools-3.0/doc/pgqd.html), the PgQ ticker daemon.

The entrypoint for this image generates a pgqd configuration file from the environment variables provided to the container.

Environment Variables
---------------------

- `PGDQ_BASE_CONNSTR`: `libpq` connection string, without dbname=
- `PGQD_LOGFILE`: where to log
- `PGQD_PIDFILE`: where to write pidfile
- `PGQD_INITIAL_DATABASE`: startupd database to query for other databases
- `PGQD_DATABASE_LIST`: limit ticker to specific databases
- `PGQD_SYSLOG`: log to syslog
- `PGQD_SYSLOG_IDENT`
- `PGQD_CHECK_PERIOD`: how often to check for new databases
- `PGQD_RETRY_PERIOD`: how often to flush retry queue
- `PGQD_MAINT_PERIOD`: how often to do maintenance
- `PGQD_TICKER_PERIOD`: how often to run ticker
