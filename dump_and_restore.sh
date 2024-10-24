rm manuscripta.sql
pg_dump -d manuscripta -h 127.0.0.1 -p 5432 -U postgres -c -f manuscripta.sql
# psql -U postgres -d manuscripta < manuscripta.sql
