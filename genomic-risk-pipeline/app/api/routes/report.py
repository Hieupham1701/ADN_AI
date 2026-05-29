"""Report endpoints."""

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/report", tags=["report"])


@router.get("/{report_id}")
async def get_report(report_id: str) -> dict:
	"""Return a mock report payload by report id."""
	if not report_id.strip():
		raise HTTPException(status_code=400, detail="report_id is required")

	return {
		"report_id": report_id,
		"status": "completed",
		"summary": "Mock genomic risk report",
		"risk_score": 0.42,
		"risk_level": "moderate",
		"recommendations": [
			"Discuss results with a qualified clinician",
			"Confirm findings with validated clinical workflow",
		],
	}