from typing import Optional
from pydantic import BaseModel

class Mail(BaseModel):
    recipient: str
    subject: str
    text: str
    as_html: Optional[bool] = None