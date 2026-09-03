# AeroTrack

**Track the world. Flight by flight.**

AeroTrack is a portfolio-grade full-stack flight tracker for exploring live aircraft, technical telemetry, recorded trajectories, and global aviation activity in 2D and 3D. The browser talks only to the FastAPI service; provider credentials and normalization stay server-side.

## Features

- Responsive landing experience and fixed navigation
- Live MapLibre map with bounding-box requests, heading-aware markers, polling, search, airborne filter, and aircraft detail sheet
- Normalized OpenSky provider behind a replaceable `FlightDataProvider` contract
- Explicit demo mode, short-lived request cache, 429 backoff, and clear loading/error states
- Flight and airport search endpoints
- PostgreSQL flight history and ordered position model with Alembic migration
- History table, observed trajectory map, and replay controls (play/pause, scrub, 1x/2x/5x/10x)
- Interactive Three.js globe with performance sampling and mobile limits
- Docker, Render, Vercel, and Neon-ready configuration

> OpenSky supplies surveillance state vectors. Commercial origin, destination, registration, aircraft type, airline, and schedule data are shown as `--` when unavailable; AeroTrack never fabricates them. Demo responses are labeled **DEMO DATA**.

## Architecture

```text
Browser / Vercel (React + TypeScript)
              │ HTTPS
              ▼
Render (FastAPI ─ provider abstraction ─ cache)
         │                         │
         ▼                         ▼
Neon PostgreSQL               OpenSky Network
```

## Stack

React 19, TypeScript strict, Vite, Tailwind CSS, Lucide, TanStack Query, React Router, MapLibre GL JS, react-globe.gl / Three.js; FastAPI, Pydantic, SQLAlchemy 2, Alembic, httpx, PostgreSQL, pytest and Vitest.

## Project structure

```text
frontend/src/{components,hooks,pages,services,test,types,utils}
backend/app/{api,core,database,models,providers,repositories,schemas,services}
backend/alembic/versions
docker-compose.yml  render.yaml
```

## Local development

Prerequisites: Node 22+, Python 3.12+, and PostgreSQL 16 (or a Neon URL).

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`; API docs are at `http://localhost:8000/docs`. For a zero-credential first run, keep `DEMO_MODE=true`. Alternatively run `docker compose up --build`.

## Environment variables

Backend: `DATABASE_URL`, optional `OPENSKY_CLIENT_ID`, `OPENSKY_CLIENT_SECRET`, `DEMO_MODE`, `FRONTEND_URL`, and `CACHE_TTL_SECONDS`. Frontend: `VITE_API_URL`, `VITE_FLIGHT_REFRESH_INTERVAL`, `VITE_MAX_GLOBE_AIRCRAFT`, and `VITE_MAX_GLOBE_ROUTES`. Never expose provider or database credentials in `VITE_*` variables.

## OpenSky

Create an account/OAuth client through the OpenSky Network portal, copy its client ID and secret into backend-only environment variables, and set `DEMO_MODE=false`. Anonymous access may work with stricter limits. The provider handles state arrays, unit consistency, timeouts, rate limits, and conversion to typed objects before data reaches the UI.

## API

`GET /api/health`, `/api/aircraft`, `/api/aircraft/live`, `/api/aircraft/{icao24}`, `/api/flights/search?q=`, `/api/flights/{id}`, `/api/history`, `/api/history/{id}`, `/api/history/{id}/positions`, and `/api/airports/search?q=`. `/api/aircraft` accepts `lamin`, `lomin`, `lamax`, and `lomax` together.

## Database and migrations

Set a PostgreSQL SQLAlchemy URL such as `postgresql+psycopg://...`, then run `alembic upgrade head` from `backend`. Schema changes must be introduced with a new Alembic revision. The normalized schema includes `airports`, `aircraft`, `flight_history`, `flight_positions`, and `tracked_flights`; indexes cover identifiers, route endpoints, and timestamps.

## Tests

```bash
cd backend && pytest
cd frontend && npm test && npm run build
```

## Production deployment

### 1. Neon

Create a Neon PostgreSQL project, copy its pooled connection string, change the driver prefix to `postgresql+psycopg://` if necessary, and store it as `DATABASE_URL` in Render. Do not commit it.

### 2. Render backend

Connect the repository using `render.yaml` or choose root `backend`. Build: `pip install -r requirements.txt && alembic upgrade head`. Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`. Configure Neon, OpenSky, `DEMO_MODE=false`, and temporarily set `FRONTEND_URL` to the expected Vercel origin. Confirm `/api/health`.

### 3. Vercel frontend

Import with root `frontend`, build `npm run build`, output `dist`, and set `VITE_API_URL=https://YOUR-BACKEND.onrender.com`. Deploy, copy the exact Vercel HTTPS origin, update `FRONTEND_URL` in Render, and redeploy the backend. Verify Vercel → Render, Render → OpenSky, Render → Neon, CORS, and history endpoints.

## Current limitations

- OpenSky does not generally include commercial route metadata.
- History storage models, reads, and replay are implemented; automated background capture is the next operational service.
- Globe aircraft are sampled; live route arcs require a future provider offering trustworthy origins/destinations.
- The public dark basemap and globe texture need network access and should be self-hosted for stricter production control.

## Roadmap

1. Live Aircraft
2. Flight Search
3. Routes
4. History
5. Flight Replay
6. 3D Globe
7. Accounts
8. Favorite Flights
9. Flight Alerts
10. Aviation Analytics

## Contributing

Use focused branches, add tests for provider/service changes, run both test suites and the production build, and never commit `.env` files or secrets. Open an issue before introducing a new external provider so its normalization contract remains stable.
