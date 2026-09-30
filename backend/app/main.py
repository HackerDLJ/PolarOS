from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app=FastAPI(title="PolarOS API",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

class Resource(BaseModel):
    id:str
    title:str
    kind:str
    region:str
    description:str
    source:str

RESOURCES=[
Resource(id="icesat2",title="ICESat-2 / ATLAS",kind="mission",region="Antarctica / Greenland",description="Laser altimetry mission for surface elevation.",source="NASA"),
Resource(id="erebus",title="Mount Erebus",kind="model",region="Ross Island, Antarctica",description="Volcanic terrain experience.",source="PolarOS source archive"),
Resource(id="everest",title="Everest & Himalayas",kind="model",region="Tibet / Nepal",description="High-altitude cryosphere terrain.",source="Uploaded GLB"),
Resource(id="landsat8",title="Landsat 8",kind="mission",region="Polar orbit",description="Multispectral remote sensing mission.",source="USGS / NASA")
]

@app.get("/api/health")
def health():
    return {"status":"online","service":"polaros-api","version":"1.0.0"}

@app.get("/api/resources",response_model=list[Resource])
def resources(q:str|None=Query(default=None),region:str|None=None):
    rows=RESOURCES
    if q:
        n=q.lower()
        rows=[r for r in rows if n in f"{r.title} {r.description} {r.region}".lower()]
    if region:
        rows=[r for r in rows if region.lower() in r.region.lower()]
    return rows

@app.get("/api/missions")
def missions():
    return [{"id":"ice-altimetry","title":"Read the Ice","duration_min":8},{"id":"ross-island","title":"Inside Ross Island","duration_min":12},{"id":"orbit","title":"Build an Orbit","duration_min":10}]
