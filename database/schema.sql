CREATE EXTENSION IF NOT EXISTS postgis;
CREATE TABLE IF NOT EXISTS resources(id UUID PRIMARY KEY DEFAULT gen_random_uuid(),title TEXT NOT NULL,kind TEXT NOT NULL,description TEXT,source TEXT,region TEXT,latitude DOUBLE PRECISION,longitude DOUBLE PRECISION,geometry GEOGRAPHY(POINT,4326),metadata JSONB DEFAULT '{}'::jsonb,created_at TIMESTAMPTZ DEFAULT NOW());
CREATE INDEX IF NOT EXISTS resources_geometry_idx ON resources USING GIST(geometry);
CREATE TABLE IF NOT EXISTS model_assets(id UUID PRIMARY KEY DEFAULT gen_random_uuid(),slug TEXT UNIQUE NOT NULL,title TEXT NOT NULL,category TEXT,file_path TEXT NOT NULL,location TEXT);
