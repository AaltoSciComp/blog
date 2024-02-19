:blogpost: true
:date: 2024-02-13
:author: Richard Darst
:category: software


DuckDB: an intro
================

A colleague recently pointed me to `DuckDB <https://duckdb.org/>`__ as
an improvement on SQLite for my work.  After many months, I have
checked more and what I found was really useful.  This blog posts is
what I wish I had long ago.

DuckDB doesn't replace SQLite.  I look at it as a natural companion
that works together for another type of workload.



The basics
----------

DuckDB is "sqlite but optimized for analytics instead of
transactions".  It has all the best things of SQLite, and SQLite is
the right mental model for understanding it:

- Serverless, in-process library
- Database = single file
- Normal SQL
- Lightweight code, C++, so has very many different language bindings
  and easy to link to if you need.
- Seems to value stability and portability, but it doesn't promise an
  unchanging database format yet.

The extra advantages of DuckDB are:

- `Column oriented <https://en.wikipedia.org/wiki/Column-oriented_DBMS>`__, which makes it much faster for analytics
- `Extra built-in math and statistics functions <https://duckdb.org/docs/sql/functions/overview>`__
- Many, many more tools for `data import/export <https://duckdb.org/docs/data/overview>`__

  - from csv, parquet, json, and SQLite (can open SQLite databases
    directly as a first step)

The extra disadvantages are:

- Columns must be of consistent data types (or null).
- `INSERTing data is basically too slow to be usable - use other
  methods for batch importing
  data. <https://github.com/duckdb/duckdb/discussions/3433>`__



How to get started
------------------

Basically, however you would use SQLite, drop in DuckDB.  The same
concepts of files for databases, opening things, etc. all are the
same.  Most of your querying SQL will still work (assuming you don't
do anything too advanced, though you might be able to make it better
by using more DuckDB functions).

The big difference is making the database.  It's not practical to
iterate data and INSERT it into the database (even with
`.executemany()`).  Instead, you'll prepare the data in some other
format (csv, parquet, even SQLite) and then import it into a DuckDB
file.  This actually makes more sense, for my typical analytical uses,
than inserting directly.

One can even leave your workflow the same: accumulate your data
dynamically into SQLite (if you are slowly accumulating into files).
Then, in the end, you analyze with DuckDB (either in-place or by
making a copy).  The differences are really not that much.



How to prepare your workflow
----------------------------

One consideration how you can better prepare your workflow for
"Initial data collection → Intermediate bulk storage → Import to
DuckDB → pre-processing with SQL".  This really isn't that different
from some of my existing workflows, with the exception that I used raw
SQLite for the intermediate storage directly.  (Using SQLite for
intermediate storage was nice in some ways, like not needing to
re-convert and incremental updates, but also had some downsides like
risk of database corruption and needing to re-make everything)

Second, SQLite is still a fine intermediate storage format, if you
want.  In that case, you can make it easier to read it by DuckDB by
ensuring type consistency:

- Define type affinities for columns in your SQLite database (`DuckDB docs
  <https://duckdb.org/docs/extensions/sqlite#data-types>`__), for
  example ``INT``, ``REAL``, ``VARCHAR``. DuckDB will use these to
  automatically infer the types when opening the database, otherwise
  everything is ``VARCHAR``.  DuckDB needs the types to vectorize
  efficiently.

- Ensure everything inserted to the SQLite database is of the right
  type corresponding to the column.  SQLite doesn't enforce this, but
  DuckDB will at read time.  (SQLite `3.37, 2021-11-27, actually can
  optionally <https://sqlite.org/stricttables.html>`__)

Or, it might be even better to store your data straight in
JSON/CSV/parquet files which can be imported efficiently.  For CSV,
basically make things as well-formed as possible.  For JSON, each line
as an `{"key":value, ...}` works well (but it can import other
formats).  For anything, makes sure data types of each column are
consistent.




Examples
--------

DuckDB is good for anything where you do vectorized operations over
columns (this is basically the purpose of a column-oriented data
store).

Here are some examples.

Open a SQLite database with DuckDB:

.. code-block::

  $ duckdb database.sqlite3

Converting to DuckDB via command line:

.. code-block:: console

    $ duckdb new.duckdb "CREATE TABLE slurm AS (SELECT * FROM sqlite_scan('original.sqlite3', 'slurm'))"


Copy SQLite to an in-memory copy:

.. code-block::

   $ duckdb database.sqlite3

::

   D ATTACH ':memory:' AS tmp;
   D CREATE TABLE tmp.tablename AS (SELECT * FROM tablename);
   D USE tmp;      -- optional but makes tmp the default

Similar, but copy to a DuckDB file::

  D ATTACH 'newfile.db';
  D CREATE TABLE newfile.tablename AS (SELECT * FROM tablename);

Access from Python, to a ``pandas.DataFrame`` (``pandas.read_sql``
also seems to work):

.. code-block:: python

    conn = duckdb.connect("database.sqlite3")
    conn.execute("select avg(cputime) from slurm").df()

`Importing from CSV files
<https://duckdb.org/docs/data/csv/overview>`__



Summary
-------

If you like the philosophy SQLite, you'll probably also like DuckDB.
There really isn't that much to do to change.  But, they serve
different roles and one isn't better than the other: they are just
different.  Both will have continued uses in the future.  They can
even work together.

Don't take everything here as the final story - we are still learning,
too!



End notes
---------

This is written after just a small amount of DuckDB usage.  It may be
updated later on.
