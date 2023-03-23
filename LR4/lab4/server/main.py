from fastapi import FastAPI

import logging
from logging.config import dictConfig
from lab4.server.config import logger_config

from lab4.server.controllers import cards_router, accounts_router, transfers_router

dictConfig(logger_config)
logger = logging.getLogger("app")


app = FastAPI(
    title="Bank Server",
    debug=True,
)

app.include_router(cards_router)
app.include_router(accounts_router)
app.include_router(transfers_router)