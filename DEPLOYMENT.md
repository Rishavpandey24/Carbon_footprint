# EcoVision - Deployment Guide

## 🌐 Hosting Options

### Option 1: Heroku (Easiest for Beginners)

#### Deploy Backend to Heroku
```bash
# Install Heroku CLI
# Windows: choco install heroku-cli
# macOS: brew tap heroku/brew && brew install heroku

# Login to Heroku
heroku login

# Create Heroku app
heroku create ecovision-api

# Create Procfile in backend/
echo "web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app" > backend/Procfile

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev --app ecovision-api

# Deploy
git push heroku main
```

#### Deploy Frontend to Vercel
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd frontend
vercel --prod
```

---

### Option 2: Railway (Modern & Easy)

#### Deploy Both Services
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Link to Railway project
railway link

# Deploy
railway up
```

---

### Option 3: AWS (Enterprise Grade)

#### Backend on EC2
```bash
# Launch EC2 instance (Ubuntu 20.04)
# SSH into instance
ssh -i key.pem ubuntu@instance-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3-pip python3-venv nginx -y

# Clone repository
git clone <repo-url>
cd Carbon_footprint/backend

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start with Gunicorn
pip install gunicorn
gunicorn -w 4 main:app --bind 0.0.0.0:8000
```

#### Frontend on S3 + CloudFront
```bash
cd frontend
npm run build

# Upload to S3
aws s3 sync build/ s3://your-bucket-name

# Set CloudFront distribution
# (Use AWS Console for easy setup)
```

---

## 📦 Production Checklist

- [ ] Update `.env` with production values
- [ ] Switch to PostgreSQL database
- [ ] Enable HTTPS/SSL
- [ ] Configure environment variables
- [ ] Set up error logging (Sentry)
- [ ] Configure email service
- [ ] Set up monitoring (DataDog)
- [ ] Enable CORS for production domain
- [ ] Add rate limiting
- [ ] Set up database backups
- [ ] Configure CDN for assets
- [ ] Test all endpoints
- [ ] Load testing
- [ ] Security audit

---

## 🔐 Production Configuration

### Backend Environment Variables
```env
DATABASE_URL=postgresql://user:password@host:5432/ecovision
API_HOST=0.0.0.0
API_PORT=8000
ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-secret-key-here
```

### Frontend Environment Variables
```env
REACT_APP_API_URL=https://api.yourdomain.com
REACT_APP_ENVIRONMENT=production
```

---

## 🚀 CI/CD Pipeline (GitHub Actions)

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy EcoVision

on:
  push:
    branches: [main]

jobs:
  test-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Set up Node
        uses: actions/setup-node@v2
        with:
          node-version: 16

      - name: Install backend dependencies
        run: |
          cd backend
          pip install -r requirements.txt

      - name: Install frontend dependencies
        run: |
          cd frontend
          npm install

      - name: Run tests
        run: |
          cd backend
          pytest

      - name: Build frontend
        run: |
          cd frontend
          npm run build

      - name: Deploy to Heroku
        uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key: ${{secrets.HEROKU_API_KEY}}
          heroku_app_name: "ecovision-api"
          heroku_email: ${{secrets.HEROKU_EMAIL}}
```

---

## 📊 Monitoring & Analytics

### Recommended Tools

1. **Error Tracking**: Sentry
2. **Performance**: DataDog or New Relic
3. **Analytics**: Google Analytics
4. **Uptime**: UptimeRobot
5. **Logging**: LogRocket (Frontend) + ELK (Backend)

---

## 💾 Database Migration

### From SQLite to PostgreSQL

```python
# backup.py - Backup SQLite to JSON
import sqlite3
import json

conn = sqlite3.connect('ecovision.db')
cursor = conn.cursor()

# Backup users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

with open('users_backup.json', 'w') as f:
    json.dump(users, f)

# Similar for other tables
```

---

## 🔧 Scaling Considerations

### When to Scale

1. **Database**: 
   - Users > 1,000 → Consider caching
   - Users > 10,000 → Migrate to PostgreSQL
   - Users > 100,000 → Add read replicas

2. **Backend**:
   - Requests > 100/sec → Add load balancer
   - Requests > 1,000/sec → Horizontal scaling
   - Requests > 10,000/sec → Microservices

3. **Frontend**:
   - CDN recommended from start
   - Add caching headers
   - Use lazy loading for routes

---

## 📈 Performance Benchmarks

### Expected Performance
- Page Load: < 2 seconds
- API Response: < 500ms
- Calculation: < 100ms
- Database Query: < 50ms

### Load Testing
```bash
# Using Apache Bench
ab -n 1000 -c 100 http://localhost:8000/api/footprint/current

# Using wrk
wrk -t12 -c400 -d30s http://localhost:8000/api/footprint/current
```

---

## 🆘 Troubleshooting Deployment

| Issue | Solution |
|-------|----------|
| Database connection error | Check DATABASE_URL and credentials |
| CORS error on production | Verify ALLOWED_ORIGINS is set correctly |
| Static files not loading | Configure CloudFront or CDN |
| High latency | Check server location, add caching |
| Memory issues | Increase server size or optimize queries |

---

## 📚 Additional Resources

- [Heroku Deployment](https://devcenter.heroku.com/articles/getting-started-with-python)
- [AWS Deployment](https://docs.aws.amazon.com/elasticbeanstalk/)
- [Railway Docs](https://docs.railway.app/)
- [Vercel Docs](https://vercel.com/docs)

---

## ✅ Pre-Launch Checklist

- [ ] All tests passing
- [ ] Error handling implemented
- [ ] Logging configured
- [ ] Database backed up
- [ ] Environment variables set
- [ ] HTTPS enabled
- [ ] Performance optimized
- [ ] Security reviewed
- [ ] Documentation updated
- [ ] Team notified
- [ ] Rollback plan ready

---

## 🎉 Launch!

Once everything is ready:

```bash
# Do a final test
curl https://api.yourdomain.com/health
# Should return: {"status": "healthy", "service": "EcoVision Backend"}

# Monitor for first 24 hours
# Check error logs and performance metrics
# Be ready to rollback if needed
```

---

**Happy deploying!** 🚀🌍
