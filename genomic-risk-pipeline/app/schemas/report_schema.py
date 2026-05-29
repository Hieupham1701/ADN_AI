from pydantic import BaseModel
from variant_schema import Variant
class Report(BaseModel):
	filename: str
	client_id: str
	risk_levels: str
	variants: list[Variant]