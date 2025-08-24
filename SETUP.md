# Setup Instructions

## Quick Start
1. Clone the repository
2. Set your OpenAI API key: `$env:OPENAI_API_KEY = "your-key"`
3. Run: `docker-compose up -d`
4. Visit: http://localhost:8000

## API Endpoints
- GET `/` - Welcome message
- POST `/translate` - Translation service
- GET `/health` - Health check

## Development
- Built with FastAPI and Docker
- Inspired by Eidolon AI framework
- Ready for expansion with more AI agents