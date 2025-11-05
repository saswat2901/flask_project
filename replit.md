# Flask Project

## Overview
This is a basic Flask web application running on Replit. The project was imported from GitHub as an empty Flask template and has been configured to run in the Replit environment.

**Purpose:** Basic Flask web application starter template  
**Current State:** Fully configured and running  
**Last Updated:** November 5, 2025

## Project Structure
```
.
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .replit                # Replit configuration
└── replit.md              # Project documentation
```

## Recent Changes
- **2025-11-05:** Initial setup
  - Installed Python 3.11
  - Created basic Flask application with a simple home page
  - Configured Flask to run on 0.0.0.0:5000
  - Set up workflow to run the Flask development server
  - Configured deployment with Gunicorn for production
  - Added Flask, Werkzeug, and Gunicorn dependencies

## Project Architecture

### Backend
- **Framework:** Flask 3.0.0
- **WSGI Server (Production):** Gunicorn 21.2.0
- **Development Server:** Flask built-in development server
- **Port:** 5000 (bound to 0.0.0.0)

### Dependencies
- Flask==3.0.0
- Werkzeug==3.0.1
- gunicorn==21.2.0

### Configuration
- **Development:** Flask runs in debug mode on 0.0.0.0:5000
- **Production:** Gunicorn serves the app with autoscale deployment
- **Workflow:** Configured to automatically run `python app.py` for development

## Running the Application

### Development
The application runs automatically via the configured workflow. To restart manually:
```bash
python app.py
```

### Production
The deployment is configured to use Gunicorn:
```bash
gunicorn --bind=0.0.0.0:5000 --reuse-port app:app
```

## Next Steps
This is a minimal Flask starter. You can extend it by:
- Adding more routes and views
- Creating HTML templates in a `templates/` directory
- Adding static files (CSS, JS) in a `static/` directory
- Integrating a database
- Adding authentication
- Building out API endpoints

## User Preferences
No specific user preferences have been documented yet.
