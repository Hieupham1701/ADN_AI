from pydantic import BaseModel

class UploadVCFRequest(BaseModel):
	filename: str
	client_id: str