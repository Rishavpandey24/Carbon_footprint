# EcoVision - Complete Setup Guide

## 🌍 Project Overview

**EcoVision** is an AI-powered carbon footprint tracker and sustainability platform designed to help users understand their environmental impact, calculate their carbon footprint, get personalized AI suggestions, and participate in eco-challenges while competing on a leaderboard.

### Key Features:
1. ✅ **Carbon Footprint Calculator** - Track travel, electricity, and food emissions
2. 🤖 **AI-Powered Suggestions** - Personalized recommendations to reduce carbon
3. 📈 **Future Emission Predictions** - Forecast your impact for the next 12 months
4. 🎯 **Sustainability Challenges** - Weekly/monthly eco-challenges with rewards
5. 🏆 **Leaderboard & Badges** - Compete with others and unlock achievements
6. 📊 **Interactive Dashboard** - Real-time tracking and visualizations

---

## 🛠️ Tech Stack

### Frontend:
- **React 18** - UI framework
- **React Router** - Navigation
- **Axios** - HTTP client
- **Recharts** - Data visualization charts
- **CSS3** - Styling with responsive design

### Backend:
- **Python 3.8+** - Backend language
- **FastAPI** - Web framework
- **SQLAlchemy** - ORM
- **SQLite** - Database
- **Uvicorn** - ASGI server

---

## 📋 Prerequisites

### System Requirements:
- **Node.js 14+** and **npm** (for frontend)
- **Python 3.8+** (for backend)
- **Git** (optional, for version control)
- **Windows/macOS/Linux**

### Installation Verification:
```bash
# Check Node.js and npm
node --version
npm --version

# Check Python
python --version
```

---

## 🚀 Installation & Setup

### Step 1: Backend Setup

#### 1.1 Navigate to Backend Directory
```bash
cd d:\Carbon_footprint\backend
```

#### 1.2 Create Python Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 1.3 Install Dependencies
```bash
pip install -r requirements.txt
```

#### 1.4 Verify Installation
```bash
pip list
```

You should see packages like: fastapi, uvicorn, sqlalchemy, pydantic

---

### Step 2: Frontend Setup

#### 2.1 Navigate to Frontend Directory
```bash
cd d:\Carbon_footprint\frontend
```

#### 2.2 Install Dependencies
```bash
npm install
```

This will install all packages from `package.json`:
- react
- react-dom
- react-scripts
- react-router-dom
- axios
- recharts

#### 2.3 Verify Installation
```bash
npm list
```

---

## ▶️ Running the Application

### Option 1: Terminal Windows (Recommended for Development)

#### Terminal 1 - Backend API
```bash
# Navigate to backend directory
cd d:\Carbon_footprint\backend

# Activate virtual environment (if not already active)
venv\Scripts\activate  # Windows
# or source venv/bin/activate  # macOS/Linux

# Run FastAPI server
python main.py
```

Expected output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

#### Terminal 2 - Frontend Dev Server
```bash
# Navigate to frontend directory
cd d:\Carbon_footprint\frontend

# Start React development server
npm start
```

Expected output:
```
webpack compiled
Compiled successfully!
On Your Network: http://192.168.x.x:3000
Local:            http://localhost:3000
```

### Option 2: Running Both with a Single Command

Create a `run.bat` file in the root directory:

```batch
@echo off
start "EcoVision Backend" python d:\Carbon_footprint\backend\main.py
timeout /t 3
start "EcoVision Frontend" cmd /k "cd d:\Carbon_footprint\frontend && npm start"
```

Then run: `run.bat`

---

## 🌐 Accessing the Application

Once both servers are running:

1. **Frontend**: Open http://localhost:3000 in your browser
2. **Backend API**: http://localhost:8000
3. **API Documentation**: http://localhost:8000/docs (Swagger UI)
4. **Alternative API Docs**: http://localhost:8000/redoc (ReDoc)

---

## 📁 Project Structure

```
d:\Carbon_footprint\
├── backend/                          # Python FastAPI Backend
│   ├── main.py                      # Entry point
│   ├── config.py                    # Configuration
│   ├── database.py                  # Database setup
│   ├── requirements.txt             # Python dependencies
│   └── app/
│       ├── models/                  # Database models
│       │   ├── user.py
│       │   ├── footprint.py
│       │   └── challenge.py
│       ├── routes/                  # API endpoints
│       │   ├── footprint_routes.py
│       │   ├── challenge_routes.py
│       │   └── leaderboard_routes.py
│       └── services/                # Business logic
│           ├── carbon_calculator.py
│           ├── ai_suggestions.py
│           └── prediction.py
│
├── frontend/                         # React Frontend
│   ├── package.json                 # Dependencies
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.js                   # Main component
│       ├── index.js                 # Entry point
│       ├── components/              # Reusable components
│       │   ├── shared.js
│       │   ├── Charts.js
│       │   └── Cards.js
│       ├── pages/                   # Page components
│       │   ├── Dashboard.js
│       │   ├── Calculator.js
│       │   ├── Suggestions.js
│       │   ├── Challenges.js
│       │   └── Leaderboard.js
│       └── styles/
│           └── App.css              # Global styles
│
└── README.md                         # This file
```

---

## 🔌 API Endpoints

### Base URL: `http://localhost:8000/api`

### Footprint Routes
- **POST** `/footprint/calculate` - Calculate carbon footprint
- **GET** `/footprint/current` - Get current footprint data
- **GET** `/footprint/suggestions` - Get AI suggestions
- **GET** `/footprint/prediction` - Get emission predictions

### Challenge Routes
- **GET** `/challenges/available` - Get available challenges
- **GET** `/challenges/active` - Get user's active challenges
- **POST** `/challenges/join/{challenge_id}` - Join a challenge
- **POST** `/challenges/update-progress/{user_challenge_id}` - Update progress

### Leaderboard Routes
- **GET** `/leaderboard/top-users` - Get top users
- **GET** `/leaderboard/badges` - Get badge statistics
- **GET** `/leaderboard/stats` - Get global statistics

---

## 💾 Database

### SQLite Setup
The database (`ecovision.db`) is automatically created when you first run the backend.

### Database Tables:
1. **users** - User profiles and stats
2. **footprints** - User carbon footprint data
3. **challenges** - Available challenges
4. **user_challenges** - User challenge participation

### Accessing Database (Optional):
```bash
# Install SQLite browser
# Windows: Download from https://sqlitebrowser.org/
# macOS: brew install sqlitebrowser
# Linux: sudo apt-get install sqlitebrowser

# Open database file
# d:\Carbon_footprint\backend\ecovision.db
```

---

## 🎮 Using the Application

### 1. Calculate Your Footprint
- Navigate to "Calculator" tab
- Enter your travel, electricity, and food data
- Click "Calculate My Footprint"
- View your breakdown by category

### 2. Get AI Suggestions
- Go to "AI Suggestions" tab
- Review personalized recommendations
- Filter by difficulty level (Easy, Medium, Hard)
- Check estimated carbon and money savings

### 3. Join Challenges
- Visit "Challenges" tab
- Browse available eco-challenges
- Click "Join Challenge"
- Use the progress slider to track completion
- Earn rewards when completed

### 4. Check Leaderboard
- Go to "Leaderboard" tab
- See top performers by green score
- View carbon saved rankings
- Check global statistics
- Aim to unlock achievement badges

### 5. Monitor Dashboard
- Home page shows all key metrics
- View emission breakdown chart
- See 12-month predictions
- Check your emission goals

---

## 🔧 Configuration

### Backend Configuration (backend/config.py)
```python
# CORS settings
ALLOWED_ORIGINS = ["http://localhost:3000"]

# Database URL
DATABASE_URL = "sqlite:///./ecovision.db"

# Carbon emission factors (customizable)
EMISSION_FACTORS = {
    "car": 0.21,              # kg CO₂ per km
    "public_transport": 0.05,
    "electricity": 0.92,      # kg CO₂ per kWh
    # ... more factors
}
```

### Frontend API URL (frontend/src/pages/*)
```javascript
const API_BASE_URL = 'http://localhost:8000/api';
```

---

## 🐛 Troubleshooting

### Issue: "Port 8000 already in use"
```bash
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (Windows)
taskkill /PID <PID> /F

# Or use a different port in main.py
# Change: uvicorn.run(app, host=API_HOST, port=9000)
```

### Issue: "CORS error" in frontend
- Ensure backend is running on http://localhost:8000
- Check ALLOWED_ORIGINS in backend/config.py
- Verify API_BASE_URL in frontend pages

### Issue: "Module not found" in backend
```bash
# Verify virtual environment is activated
# Then reinstall dependencies
pip install -r requirements.txt
```

### Issue: "npm packages not found"
```bash
# Clear cache and reinstall
npm cache clean --force
npm install
```

### Issue: Database errors
```bash
# Delete old database and let it recreate
rm d:\Carbon_footprint\backend\ecovision.db

# Restart backend
python main.py
```

---

## 🚀 Deployment

### Build for Production

#### Frontend Build
```bash
cd d:\Carbon_footprint\frontend
npm run build
```
Creates optimized build in `frontend/build/` directory.

#### Backend Deployment
```bash
# Install production ASGI server
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 main:app
```

### Recommended Hosting:
- **Frontend**: Vercel, Netlify, or GitHub Pages
- **Backend**: Heroku, Railway, or AWS Lambda
- **Database**: PostgreSQL (instead of SQLite)

---

## 📊 Sample Data

The application comes with default challenges:
1. **Save 50 kWh Electricity** - Medium difficulty, 100 points
2. **Car-Free Week** - Hard difficulty, 150 points
3. **Plastic-Free Shopping** - Easy difficulty, 80 points
4. **Vegetarian Week** - Medium difficulty, 120 points
5. **Water Conservation** - Easy difficulty, 90 points

Users can calculate their footprint and get suggestions based on their input.

---

## 🌟 Features Explained

### Carbon Footprint Calculation
Based on real-world emission factors:
- **Travel**: Car (0.21 kg CO₂/km), Public transport (0.05), Flights (0.255)
- **Electricity**: 0.92 kg CO₂/kWh (average grid)
- **Food**: Beef (27), Chicken (6.9), Vegetarian (2), Vegan (0.5) kg CO₂ per meal

### AI Suggestion Engine
Rule-based system analyzing user data:
- If car usage > 500 km/month → suggest public transport
- If electricity > 200 kWh/month → suggest LED bulbs, AC optimization
- If high beef consumption → suggest vegetarian alternatives
- Calculates estimated CO₂ and money savings

### Emission Prediction
Projects future emissions based on:
- Current lifestyle patterns
- Trend analysis (stable/increasing/decreasing)
- 6-month and 12-month forecasts
- Comparison to global average (333 kg CO₂/person/month)

### Challenges & Gamification
- Users earn green points for challenges
- 100+ points: "Eco Beginner"
- 10+ challenges: "Carbon Saver"
- 20+ challenges: "Climate Champion"
- Leaderboard tracks top performers

---

## 📚 Additional Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com
- **React Documentation**: https://react.dev
- **SQLAlchemy ORM**: https://www.sqlalchemy.org
- **Recharts**: https://recharts.org

---

## 🤝 Contributing

Want to add features? Here are ideas for extensions:

1. **User Authentication** - Add login/registration
2. **Mobile App** - React Native version
3. **Social Features** - Friend connections, team challenges
4. **Location-based Features** - Map integration for local impact
5. **Advanced ML** - Machine learning for better predictions
6. **Export Reports** - PDF/Excel carbon reports
7. **Integration APIs** - Connect with fitness trackers, smart home devices
8. **Blockchain** - Carbon credit tracking

---

## 📄 License

This project is open-source and available for educational and hackathon purposes.

---

## ❓ FAQ

**Q: Can I modify the emission factors?**
A: Yes! Edit `backend/config.py` EMISSION_FACTORS dictionary.

**Q: How do I reset user data?**
A: Delete `backend/ecovision.db` and restart the backend.

**Q: Can I deploy this?**
A: Yes! See Deployment section. Need to switch to PostgreSQL for production.

**Q: How accurate are the calculations?**
A: Based on scientific carbon accounting standards. Real impacts vary by region/context.

**Q: Can I add more challenges?**
A: Yes! Add them via the API or directly insert into database.

---

## 🎉 You're All Set!

Your EcoVision application is ready to track, analyze, and reduce carbon footprint! Start with the Calculator, get suggestions, join challenges, and help the planet.

**Let's make sustainability fun and achievable together! 🌍💚**

---

For questions or support, refer to the project structure documentation above.
