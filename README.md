# PolarOS

Integrated Polar Science Outreach, Knowledge Repository & Media Dissemination Portal by Team JATABELS.

## Stack
React + TypeScript + Vite + Three.js/React Three Fiber + Python FastAPI + PostgreSQL/PostGIS + Java ingestion service + Docker + GitHub Actions.

## Run
Frontend: `cd frontend && npm install && npm run dev`
API: `cd backend && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && uvicorn app.main:app --reload --port 8787`
Java: `cd java-service && mkdir -p out && javac -d out src/main/java/com/polaros/IngestionServer.java && java -cp out com.polaros.IngestionServer`

Large .glb/.zip assets should use Git LFS.

## Modules
Mission Control · Polar Explorer · 3D Field Lab · Satellite Lab · Immersive Learn · Knowledge Repository · Data Core.
