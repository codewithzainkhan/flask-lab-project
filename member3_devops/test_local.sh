#!/bin/bash

echo "🔧 Testing Flask Application Locally"

# Test Python app
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🧪 Running tests..."
python -m pytest tests/ -v

echo "🐳 Building Docker image..."
docker build -t flask-lab-app .

echo "🚀 Testing Docker container..."
docker run -d -p 5000:5000 --name test-app flask-lab-app
sleep 10

echo "📡 Testing endpoints..."
curl -f http://localhost:5000/health || echo "Health check failed!"
curl -f http://localhost:5000/ || echo "Home route failed!"

echo "✅ Testing Docker container health..."
docker exec test-app curl -f http://localhost:5000/health || echo "Container health check failed"

echo "🛑 Cleaning up..."
docker stop test-app
docker rm test-app

echo "✅ Local testing completed!"