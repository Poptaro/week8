from django.core.exceptions import ValidationError
import re

def validate_student_name(name):
  pattern = r"^[A-Z][a-z]+ ([A-Z]\.)? [A-Z][a-z]+$"
  validatedName = re.match(pattern, name)
  if not validatedName:
    raise ValidationError("Your name does not meet the name format")
  else:
    return name
  
def validate_student_email(email):
  pattern = r"^[a-zA-Z0-9._%+-]+@school\.com$"
  if not re.match(pattern, email):
    raise ValidationError("Student Email is not in the correct format")
  else:
    return email
