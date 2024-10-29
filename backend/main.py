# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from fastapi import Request
from routers.user import router as user_router  # Correct import for user router
from routers.router_product import router as product_router  # Correct import for product router

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:5173",  # Update with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Middleware for logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Response: {response.status_code}")
    return response

# Register routers
app.include_router(user_router, prefix="/users")  # Prefix for user routes
app.include_router(product_router, prefix="/products")  # Prefix for product routes
