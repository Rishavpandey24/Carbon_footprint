# Performance Optimization Guide for EcoVision

## Backend Optimization

### 1. Database Optimization
```python
# Add indexes for frequently queried fields
from sqlalchemy import Index

# In models/user.py
__table_args__ = (
    Index('idx_badge_level', 'badge_level'),
    Index('idx_green_score', 'green_score'),
)
```

### 2. API Response Caching
```python
# Add caching headers
from fastapi import Header
from datetime import timedelta

@router.get("/leaderboard/top-users")
def get_top_users(
    cache_control: str = Header(None),
    limit: int = 10
):
    # Results cached for 5 minutes on client
    return {"Cache-Control": "public, max-age=300"}
```

### 3. Database Connection Pooling
```python
# In database.py
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10
)
```

## Frontend Optimization

### 1. Code Splitting
```javascript
// Use React.lazy for route-based splitting
const Dashboard = React.lazy(() => import('./pages/Dashboard'));
const Calculator = React.lazy(() => import('./pages/Calculator'));

// In Routes:
<Suspense fallback={<Loading />}>
  <Routes>
    <Route path="/" element={<Dashboard />} />
  </Routes>
</Suspense>
```

### 2. Memoization
```javascript
import { memo } from 'react';

// Prevent unnecessary re-renders
const ChallengeCard = memo(({ challenge }) => (
  <div>{challenge.title}</div>
));
```

### 3. API Call Optimization
```javascript
// Use React Query or SWR for caching
import useSWR from 'swr';

function Dashboard() {
  const { data, isLoading } = useSWR('/api/footprint/current', fetcher);
  // Data is automatically cached and reused
}
```

## Deployment Optimization

### Frontend Production Build
```bash
npm run build
# Creates optimized production build in build/

# Serve with gzip compression
npx serve -s build -c ./serve.json
```

### Backend Production Configuration
```python
# Use Gunicorn for production
pip install gunicorn

# Run with multiple workers
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
```

## Monitoring & Profiling

### Backend Performance Monitoring
```python
# Add to main.py for monitoring
import time

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

### Frontend Performance
```javascript
// Use Chrome DevTools Performance tab
// Lighthouse for audits
// React DevTools Profiler for component performance
```

---

For detailed optimization techniques, see DEVELOPMENT.md
