"""Upload endpoints for VCF files."""

from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post("/vcf")
async def upload_vcf(file: UploadFile = File(...)) -> dict:
	"""Accept a VCF file and return a mock processing job id."""
	if not file.filename:
		raise HTTPException(status_code=400, detail="No file name provided")

	if not file.filename.lower().endswith(".vcf"):
		raise HTTPException(status_code=400, detail="Only .vcf files are accepted")

	return {
		"message": "VCF uploaded successfully",
		"filename": file.filename,
		"job_id": str(uuid4()),
		"status": "queued",
	}