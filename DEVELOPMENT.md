# EcoVision Development Guidelines

## Code Structure

### Backend (FastAPI)
- **Models** (`app/models/`): Database schemas and relationships
- **Routes** (`app/routes/`): API endpoint definitions
- **Services** (`app/services/`): Business logic and calculations
- **Database** (`database.py`): Connection and session management
- **Config** (`config.py`): Central configuration

### Frontend (React)
- **Pages** (`src/pages/`): Full-page components
- **Components** (`src/components/`): Reusable UI components
- **Styles** (`src/styles/`): CSS styling
- **App.js**: Main app component with routing

## Adding New Features

### 1. Add a New API Endpoint

**Backend (backend/app/routes/new_feature.py):**
```python
from fastapi import APIRouter
router = APIRouter()

@router.get("/endpoint")
def my_endpoint():
    return {"status": "success"}
```

**Then add to main.py:**
```python
from app.routes import new_feature
app.include_router(new_feature.router, prefix="/api/feature", tags=["Feature"])
```

### 2. Add a New Page

**Frontend (src/pages/NewPage.js):**
```javascript
import React from 'react';

function NewPage() {
  return <div>New Feature</div>;
}

export default NewPage;
```

**Add to App.js routing:**
```javascript
<Route path="/new-page" element={<NewPage />} />
```

### 3. Add a New Calculation Service

Create `backend/app/services/new_service.py` with calculation logic.

## Database Modifications

To add a new table:

1. Create model in `app/models/new_model.py`
2. Import in `app/models/__init__.py`
3. Restart backend (recreates tables)

## Styling Guidelines

- Use CSS variables from `:root` in `App.css`
- Follow responsive design with media queries
- Use the existing color palette (green, blue, orange)
- Maintain consistent spacing using `--spacing-*` variables

## Testing

### Backend
```bash
# Install testing dependencies
pip install pytest pytest-httpx

# Run tests
pytest
```

### Frontend
```bash
# Run tests
npm test
```

## Performance Tips

1. **Backend**: Use database indexes for frequently queried fields
2. **Frontend**: Lazy load routes with React.lazy()
3. **API**: Cache predictions and suggestions when possible
4. **Database**: Archive old footprint records periodically

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| CORS Error | Check ALLOWED_ORIGINS in config.py |
| Port conflict | Change port in config.py or main.py |
| DB locked | Close other connections or delete .db file |
| npm packages missing | Run `npm install` again |
| Python modules missing | Activate venv and run `pip install -r requirements.txt` |

## Future Enhancement Ideas

1. **Authentication**: Add user login/signup
2. **Email Notifications**: Send challenge reminders
3. **Social Features**: Share achievements, friend connections
4. **Mobile App**: React Native version
5. **Advanced Analytics**: More detailed charts and insights
6. **ML Integration**: Better prediction models
7. **API Integration**: Connect with fitness trackers, smart home devices
8. **Blockchain**: Carbon credit system

## Contributing Standards

- Write clean, commented code
- Follow existing code style
- Test changes before committing
- Update documentation
- Keep dependencies up to date

---

Last Updated: 2026-06-03
