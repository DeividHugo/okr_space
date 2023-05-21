#!/bin/bash
set -e

echo "Creating ork_space database"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE okr_space;
    ALTER DATABASE okr_space OWNER TO postgres;
    GRANT ALL PRIVILEGES ON DATABASE okr_space TO postgres;
EOSQL
