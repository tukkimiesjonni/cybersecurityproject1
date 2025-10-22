from flask import Flask, request, session
from os import getenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from logging_config import setup_logging

ENABLE_LOGGING = True


app = Flask(__name__)
logger = setup_logging(enable_logging=ENABLE_LOGGING)

@app.before_request
def log_request_info():
    if ENABLE_LOGGING:
        logger.info(f"Request: {request.method} {request.path} | IP: {request.remote_addr}")

@app.after_request
def log_response_info(response):
    if ENABLE_LOGGING:
        logger.info(f"Response: {response.status_code} {response.status}")
    return response

# Initialize rate limiter for the app to prevent brute-force attacks
limiter = Limiter(
    key_func=get_remote_address,
)
limiter.init_app(app)


# app.secret_key = getenv("SECRET_KEY")
app.secret_key = "test"

import routes
