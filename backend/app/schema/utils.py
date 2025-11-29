from pydantic import BaseModel, Field

class HealthCheckResponse(BaseModel):
    status: int = Field(..., example=200)