```markdown
# EcoVision - Quick Start Guide

## 🚀 Get Running in 5 Minutes

### Prerequisites
- **Python 3.8+** installed
- **Node.js 14+** installed
- **2 Terminal windows** ready

---

## Step 1: Setup (One-time)

### Windows Users:
```powershell
cd d:\Carbon_footprint
.\setup.ps1
```

### macOS/Linux Users:
```bash
cd ~/Carbon_footprint
bash setup.sh
```

This automatically:
- ✓ Checks Python and Node.js
- ✓ Creates Python virtual environment
- ✓ Installs all Python packages
- ✓ Installs all npm packages

---

## Step 2: Start Backend (Terminal 1)

```bash
cd d:\Carbon_footprint\backend

# Activate virtual environment
.\venv\Scripts\Activate.ps1  # Windows
# or source venv/bin/activate  # macOS/Linux

# Start API server
python main.py
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
Press CTRL+C to quit
```

✅ **Backend is running!** API available at http://localhost:8000

---

## Step 3: Start Frontend (Terminal 2)

```bash
cd d:\Carbon_footprint\frontend

# Start development server
npm start
```

**Expected output:**
```
Compiled successfully!
On Your Network: http://192.168.x.x:3000
Local:            http://localhost:3000
```

✅ **Frontend is running!** App opens at http://localhost:3000

---

## 🎯 Using the App

1. **Dashboard** - See your current carbon footprint
2. **Calculator** - Enter your lifestyle data
3. **AI Suggestions** - Get personalized eco-tips
4. **Challenges** - Join and track eco-challenges
5. **Leaderboard** - See top performers

---

## 📚 API Documentation

Visit: **http://localhost:8000/docs**

Interactive API documentation with all endpoints!

---

## ❌ Troubleshooting

| Problem | Solution |
|---------|----------|
| Backend won't start | Make sure Python venv is activated |
| Frontend won't start | Delete `node_modules/` and run `npm install` |
| "Port already in use" | Another app is using port 8000 or 3000 |
| "Module not found" | Make sure you activated the venv and ran pip install |

---

## 📁 Project Layout

```
Carbon_footprint/
├── backend/          ← Python API (port 8000)
├── frontend/         ← React App (port 3000)
├── README.md         ← Full documentation
└── DEVELOPMENT.md    ← Developer guide
```

---

## 🎓 What's Inside

### Backend (FastAPI)
- 🧮 Carbon calculation engine
- 🤖 AI suggestion system
- 📈 Emission prediction
- 💾 SQLite database
- 🔌 REST API

### Frontend (React)
- 📊 Interactive charts
- 📱 Responsive design
- 🎮 Challenge tracking
- 🏆 Leaderboard
- 🎨 Modern UI

---

## 💡 Next Steps

1. Calculate your carbon footprint
2. Explore AI suggestions
3. Join your first challenge
4. Check the leaderboard
5. Read [README.md](README.md) for detailed docs

---

## 🆘 Help

- **Full Setup Guide**: See [README.md](README.md)
- **Developer Info**: See [DEVELOPMENT.md](DEVELOPMENT.md)
- **API Docs**: Visit http://localhost:8000/docs when running

---

## ✨ Have fun tracking your environmental impact! 🌍💚
```

---

Save this as a quick reference card or print it out!
