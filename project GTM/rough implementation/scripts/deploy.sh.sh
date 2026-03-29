#!/bin/bash
# scripts/deploy.sh
# Deploying the Sourcegraph GTM infrastructure on a server

set -e

# Variables (can be overridden before running)
PROJECT_DIR="/opt/sourcegraph-gtm"
BRANCH="main"
ENV_FILE=".env.production"

echo "🚀 Starting deployment of Sourcegraph GTM..."

# Go to the project directory
cd "$PROJECT_DIR" || { echo "Project directory not found!"; exit 1; }

# 1. Updating code from the repository
echo "📦 Pulling latest code from git..."
git pull origin "$BRANCH"

# 2. Copying the production configuration (if any)
if [ -f "$ENV_FILE" ]; then
    cp "$ENV_FILE" .env
    echo "✅ Environment file copied."
else
    echo "⚠️  Warning: $ENV_FILE not found, using existing .env"
fi

# 3. Stopping old containers
echo "🛑 Stopping old containers..."
docker-compose down

# 4. Assembling images
echo "🔨 Building Docker images..."
docker-compose build --no-cache

# 5. Running database migrations (via a separate container)
echo "🔄 Running database migrations..."
docker-compose run --rm backend alembic upgrade head

# 6. Launch of new containers
echo "🚀 Starting new containers..."
docker-compose up -d

# 7. Cleaning up unused images (optional)
echo "🧹 Cleaning up old Docker images..."
docker image prune -f

echo "✅ Deployment completed successfully!"
echo "📊 Check logs: docker-compose logs -f"