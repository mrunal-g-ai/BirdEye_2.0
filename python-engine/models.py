from pydantic import BaseModel, Field
from typing import List, Optional

class CivicIssue(BaseModel):
    record_id: str
    record_type: str = "civic_issue"
    description: str
    category: str

class SecurityEvent(BaseModel):
    record_id: str
    record_type: str = "security_alert"
    description: str
    category: str
    
class LangChainRoutingDecision(BaseModel):
    record_id: str
    record_type: str
    assigned_department: str
    routing_confidence: float
    priority_assigned: str
    rationale: str
    action_plan: List[str]
    human_review_required: Optional[bool] = False
