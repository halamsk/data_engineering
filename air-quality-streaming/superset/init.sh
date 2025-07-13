#!/bin/bash
set -e

# Wait for DB to be ready
echo "Waiting for Superset DB..."
sleep 5

superset db upgrade

# Create admin user only if not exists
superset fab create-admin \
    --username "${ADMIN_USERNAME:-admin}" \
    --firstname "${ADMIN_FIRST_NAME:-Superset}" \
    --lastname "${ADMIN_LAST_NAME:-Admin}" \
    --email "${ADMIN_EMAIL:-admin@superset.com}" \
    --password "${ADMIN_PASSWORD:-admin}" || true

superset init

# Run the server
superset run -h 0.0.0.0 -p 8088 --with-threads --reload --debugger
