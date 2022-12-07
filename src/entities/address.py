from pydantic import BaseModel, validator


class Address(BaseModel):
    street: str
    number: int
    zip: str
    city: str

    class Config:
        """
        Ideally, the value objects class should have private attributes.
        But there aren't public or private attributes in python!
        """
        frozen = True

    @validator("street", "zip", "city")
    def validate_street(cls, v):
        if not len(v):
            raise ValueError("Input can't be empty")

        return v
