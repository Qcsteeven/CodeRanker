#!/bin/bash

echo "Building Docker images..."

docker-compose build

echo "GO TO http://localhost:8000/scraper/"

echo "Starting Docker containers..."

docker-compose up