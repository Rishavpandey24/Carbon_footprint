#!/bin/bash
# Quick Start Script for EcoVision (macOS/Linux)

echo "╔════════════════════════════════════╗"
echo "║      EcoVision Quick Start         ║"
echo "╚════════════════════════════════════╝"
echo ""

# Check if Python is installed
echo "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✓ Python found: $PYTHON_VERSION"
else
    echo "✗ Python not found. Please install Python 3.8+"
    exit 1
fi

# Check if Node.js is installed
echo "Checking Node.js installation..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo "✓ Node.js found: $NODE_VERSION"
else
    echo "✗ Node.js not found. Please install Node.js 14+"
    exit 1
fi

echo ""
echo "Setting up Backend..."

# Navigate to backend
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

echo "✓ Backend setup complete!"
echo ""

# Go back to root
cd ..

echo "Setting up Frontend..."
cd frontend

# Install npm dependencies
if [ ! -d "node_modules" ]; then
    echo "Installing npm packages..."
    npm install -q
else
    echo "npm packages already installed"
fi

echo "✓ Frontend setup complete!"
echo ""

cd ..

echo "╔════════════════════════════════════╗"
echo "║   Setup Complete! Ready to Run     ║"
echo "╚════════════════════════════════════╝"
echo ""

echo "To start EcoVision:"
echo ""
echo "Terminal 1 (Backend API):"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  python main.py"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd frontend"
echo "  npm start"
echo ""
echo "Then open: http://localhost:3000"
echo ""
