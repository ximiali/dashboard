#!/bin/bash
set -e

# Check if the path to the SQL file was provided as an argument
if [ -z "$1" ]; then
  echo "Error: Missing argument."
  echo "Correct usage: $0 <path_to_sql_file.sql>"
  exit 1
fi

SQL_FILE_PATH="$1"

# Check if the SQL file actually exists before proceeding
if [ ! -f "$SQL_FILE_PATH" ]; then
    echo "Error: SQL file '$SQL_FILE_PATH' not found."
    exit 1
fi

export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/test"
export DJANGO_SECRET_KEY=$(openssl rand -base64 22)
export DB_DEFAULT_HOST=127.0.0.1
export DASH_DB_HOST=127.0.0.1
export DASH_DB_NAME=dashboard
export DASH_DB_USER=admin
export DASH_DB_PASSWORD=admin
export DB_DEFAULT="{
  \"ENGINE\": \"django.db.backends.postgresql\",
  \"NAME\": \"dashboard\",
  \"USER\": \"admin\",
  \"PASSWORD\": \"admin\",
  \"HOST\": \"127.0.0.1\",
  \"PORT\": \"5434\",
  \"CONN_MAX_AGE\": ${DB_DEFAULT_CONN_MAX_AGE:=null},
  \"OPTIONS\": {
    \"connect_timeout\": 2 
  }
}"
export DEBUG=True

echo "Starting the 'dashboard_db' container..."
if ! docker-compose up -d dashboard_db; then
  # If the command fails, display a specific error message and exit
  echo "ERROR: Failed to start the 'dashboard_db' container. Check Docker logs."
  docker-compose logs dashboard_db | sed -n '1,200p'
  exit 1
fi
echo "Container 'dashboard_db' started successfully."
sleep 1

mkdir -p volume_data
echo "Running App DB migration (migrate-app-db.sh)..."
if [ -f "migrate-app-db.sh" ]; then
    sh migrate-app-db.sh
else
    echo "Warning: Script 'migrate-app-db.sh' not found. Skipping."
fi

echo "App DB Migration successful."

psql -h 127.0.0.1 -p 5434 -W -U admin -d dashboard < $SQL_FILE_PATH

echo "Running Cache DB migration (migrate-cache-db.sh)..."
if [ -f "migrate-cache-db.sh" ]; then
    sh migrate-cache-db.sh
else
    echo "Warning: Script 'migrate-cache-db.sh' not found. Skipping."
fi

echo "Local database is ready to use. Running server!"

poetry run python3 manage.py runserver


