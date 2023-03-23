from sqlalchemy import MetaData, Table, Integer, String, Column, ForeignKey, TIMESTAMP
from datetime import datetime


metadata = MetaData()

card = Table(
    "card",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("number", String, nullable=False),
    Column("pincode", String, nullable=False),
    Column("account_id", Integer, ForeignKey("card_account.id")),
)

card_account = Table(
    "card_account",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("number", String, nullable=False),
    Column("currency", String, nullable=False),
    Column("balance", Integer),
)

transfer = Table(
    "transfer",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("account_id", Integer, ForeignKey("card_account.id")),
    Column("operation_type", String, nullable=False),
    Column("operation_name", String),
    Column("completed_at", TIMESTAMP, default=datetime.utcnow),
    Column("amount", Integer),
)