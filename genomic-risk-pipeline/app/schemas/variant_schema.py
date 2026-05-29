from pydantic import BaseModel

class Variant(BaseModel):
	chromosome: str
	position: int
	reference: str
	alternate: str
	gene: str
	significance: str