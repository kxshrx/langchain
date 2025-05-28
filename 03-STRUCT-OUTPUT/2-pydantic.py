from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    id : int  #basic
    name: str ='aamir'   #default
    age : Optional[int] = None    #optional
    email : EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description="the cumulative grade in decimal value")


new_Student={
    'id':24043,
    'email' : 'john@yahoo.com',
    'cgpa' : 8.45
}

student1 = Student(**new_Student)


student_dict = dict(student1)
print(student1)

student_json = student1.model_dump_json()

print(student_json)

# student2: Student = {'name': 'pranav'}

# print(student1)
# print(type(student1))
# print(student2)
# print(type(student2))
