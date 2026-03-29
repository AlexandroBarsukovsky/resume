#!/bin/bash
# scripts/backup.sh
# Backing up a PostgreSQL database for Sourcegraph GTM

set -e

# Configuration (can be moved to .env or environment variables)
BACKUP_DIR="/backups"
DB_NAME="sg_gtm_db"
DB_USER="sg_user"
DB_HOST="localhost"
DB_PORT="5432"
# The password is taken from the environment variable (for security)
PGPASSWORD="${DB_PASSWORD}"

# Create a directory for backups if there is none
mkdir -p "$BACKUP_DIR"

# Forming a file name with the date
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql"

echo "Starting backup of database $DB_NAME to $BACKUP_FILE"

# Performing a dump
pg_dump -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -F c -f "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "Backup completed successfully: $BACKUP_FILE"
    # We delete backups older than 30 days
    find "$BACKUP_DIR" -name "${DB_NAME}_*.sql" -mtime +30 -delete
    echo "Old backups removed."
else
    echo "Backup failed!"
    exit 1
fi

# Optional: upload to cloud storage (S3, Yandex Cloud)
# Example for AWS S3 (requires awscli):
# aws s3 cp "$BACKUP_FILE" s3://your-bucket/backups/

echo "Backup finished."