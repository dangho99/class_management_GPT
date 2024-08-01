example = [
    {"questions": "Hello",
     "answer": """case_type: "greetings",
                  table_name: None
                  action: None
                  dateinfo: None"""},
    
    {"questions": "Hi",
     "answer": """case_type: "greetings",
                  table_name: None
                  action: None
                  dateinfo: None"""},
    
    {"questions": "Xin chao",
     "answer": """case_type: "greetings",
                  table_name: None
                  action: None
                  dateinfo: None"""},
    
    {"questions": "Start",
     "answer": """case_type: "greetings",
                  table_name: None
                  action: None
                  dateinfo: None"""}
]

# For Class Agent
example_class = [
    {"questions": "Tell me assign class",
     "answer": """case_type: "class",
                  table_name: Class
                  action: None
                  dateinfo: None"""},
]


# For Assignment Agent
example_assignmnet = [
     {"questions": "Assign XYZ to class ABC",
     "answer": """case_type: "assign",
                  table_name: Class
                  action: None
                  dateinfo: None"""},
]