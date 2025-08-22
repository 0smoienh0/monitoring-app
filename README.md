# Monitoring App

## Description
A lightweight Python application for monitoring API health and performance. It provides real-time status checks, alerts, and reports. Can be easily run with Docker or Python for both development and production environments.

## Features
- Check the health of multiple APIs
- Real-time response time monitoring
- Simple JSON configuration for API endpoints
- Lightweight and easy to deploy with Docker
- Generates basic reports on API status

## Requirements
- Python 3.11+
- Docker (optional, for containerized deployment)
- Python packages in `requirements.txt`

## Installation

### Using Docker
```bash
docker build -t monitoring-app .
docker run -d --name monitoring-app -p 8000:8000 monitoring-app
