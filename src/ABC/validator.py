from typing import Optional, Literal
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser

class Validator(BaseModel):
    # Model Type
    llm_type: str | Literal["chatgpt","mistral","llama"]
    
    # Class
    class_name: Optional[str] = None
    teacher_name: Optional[str] = None
    

output_parser = PydanticOutputParser(pydantic_object=Validator)
    
    
    
    
    
