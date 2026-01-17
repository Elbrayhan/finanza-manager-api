from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str
    debts: List["Debt"] = Relationship(back_populates="owner")

class Debt(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    remaining_balance: float
    description: str
    due_date: datetime
    user_id: int = Field(foreign_key="user.id")
    owner: User = Relationship(back_populates="debts")
