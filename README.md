# Full Stack Application

This project is a full-stack application built with Django, React, MongoDB, and sentiment analysis capabilities.

## Features

- Django backend with REST API
- React frontend with modern UI
- MongoDB docker container for data storage
- Sentiment analysis functionality

## Technologies Used

- **Django**: Backend framework
- **React**: Frontend library
- **MongoDB**: Database
- **Sentiment Analysis**: Text processing

## Architecture

```
┌───────────────────────┐
│      Django API       │
└─────────┬─────────────┘
          │
┌─────────▼─────────────┐
│    React Frontend     │
└─────────┬─────────────┘
          │
┌─────────▼─────────────┐
│   MongoDB Database    │
└─────────┬─────────────┘
          │
┌─────────▼─────────────┐
│ Sentiment Analysis    │
└─────────┬─────────────┘
```

## Getting Started

1. Clone the repository
2. Install dependencies
3. Run the application

## Project Structure

- `server/` - Django backend
- `frontend/` - React frontend
- `database/` - MongoDB data files
- `.github/workflows/` - CI/CD workflows

## Deployment

This project is deployed on the following platforms:
- GitHub Actions for CI/CD
- IBM Cloud Code Engine
- MongoDB docker container with node mongoose.