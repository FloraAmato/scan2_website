#!/bin/bash
# Script to change WordPress user password after deployment
# Usage: ./scripts/change-wp-password.sh [username] [new_password]

set -e

# Load environment variables if .env exists
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

USERNAME="${1:-bondo2488_zeoxh4x1}"
PASSWORD="${2:-$WP_USER_PASSWORD}"

if [ -z "$PASSWORD" ]; then
    echo "Error: No password provided."
    echo "Usage: $0 [username] [password]"
    echo "Or set WP_USER_PASSWORD in your .env file"
    exit 1
fi

echo "Changing password for WordPress user: $USERNAME"

docker-compose run --rm wpcli wp user update "$USERNAME" --user_pass="$PASSWORD"

echo "Password updated successfully for user: $USERNAME"
