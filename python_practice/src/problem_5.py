import logging

def setup_logging():
    logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="""%(asctime)s [%(levelname)s] %(name)s 
    (%(filename)s:%(funcName)s:%(lineno)d): %(message)s""",
    force=True,
)
    
logger = logging.getLogger(__name__)
"""
 Problem 5: Data Quality Check
 Validate a dataset and return all validation errors.
  
 Rules: 
 - id must not be null 
 - email must contain '@' 
 - age must be >= 0 

 rows = [ 
 {"id": 1, "email": "a@example.com", "age": 30}, 
 {"id": None, "email": "b@example.com", "age": -5} 
 ] 
 """


def validating_data(lst: list[dict[str,any]])-> list[dict[str,any]] | str:
    if not isinstance(lst, list):
        return "you did not input a list"
    if len(lst)==0:
        return "no element in the provided list"

    errors = []
    for i,row in enumerate(lst):
        if row.get("id") is None:
            errors.append({"row": i, "field": "id", "error": "must not be null"})

        if "@" not in row.get("email", ""):
            errors.append({"row": i, "field": "email", "error": "must contain @"})

        if row.get("age", 0) < 0:
            errors.append({"row": i, "field": "age", "error": "must be >= 0"})



    return errors


