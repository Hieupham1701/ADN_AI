"""FastAPI entrypoint for Genomic Risk Pipeline."""

from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.report import router as report_router
from app.api.routes.upload import router as upload_router

app = FastAPI(
	title="Genomic Risk Pipeline API",
	version="0.1.0",
	description=(
		"API for uploading VCF files, running genomic risk workflows, "
		"and retrieving reports"
	),
)

app.include_router(health_router, prefix="/api/v1")
app.include_router(upload_router, prefix="/api/v1")
app.include_router(report_router, prefix="/api/v1")


@app.get("/", tags=["root"])
async def root() -> dict:
	"""Root endpoint with quick API navigation info."""
	return {
		"message": "Genomic Risk Pipeline API",
		"docs": "/docs",
		"health": "/api/v1/health",
	}
