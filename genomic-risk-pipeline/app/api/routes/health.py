"""Health check endpoints."""

from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", summary="Service health check")
async def health_check() -> dict:
	"""Simple liveness endpoint."""
	return {
		"status": "ok",
		"service": "genomic-risk-pipeline",
		"timestamp": datetime.now(timezone.utc).isoformat(),
	}