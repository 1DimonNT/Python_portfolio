from dataclasses import dataclass 
from enum import Enum 
 
class Gender(Enum): 
    MALE = 'Male' 
    FEMALE = 'Female' 
    OTHER = 'Other' 
 
@dataclass 
class User: 
    first_name: str 
    last_name: str 
    email: str 
    gender: Gender 
    mobile: str 
    address: str 
    state: str 
    city: str 
 
    @property 
    def full_name(self) -> str: 
        return f'{self.first_name} {self.last_name}' 
 
test_user = User( 
    first_name='Alex', 
    last_name='Egorov', 
    email='alex@egorov.com', 
    gender=Gender.MALE, 
    mobile='1234567890', 
    address='Some street 1', 
    state='NCR', 
    city='Delhi' 
) 
