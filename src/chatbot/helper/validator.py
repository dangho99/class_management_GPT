from typing import Optional, Union, Literal
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from datetime import date


class Case(BaseModel):
    case_type: str
    table_name: str | Literal["user","assignment","course","class"]
    action: Optional[str] = None
    dateinfo: Optional[date] = None


output_parser = PydanticOutputParser(pydantic_object=Case)
