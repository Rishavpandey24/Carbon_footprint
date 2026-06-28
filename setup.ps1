# EcoVision Setup Script for Windows
Write-Host "Checking Python..." -ForegroundColor Yellow
python --version
Write-Host "Checking Node.js..." -ForegroundColor Yellow  
node --version
Write-Host "Setting up Backend..." -ForegroundColor Cyan
cd backend
if (!(Test-Path "venv")) {
    python -m venv venv
}
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd ..
Write-Host "Setting up Frontend..." -ForegroundColor Cyan
cd frontend
npm install
cd ..
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "Next steps:"
Write-Host "  Terminal 1: cd backend && .\venv\Scripts\Activate.ps1 && python main.py"
Write-Host "  Terminal 2: cd frontend && npm start"
