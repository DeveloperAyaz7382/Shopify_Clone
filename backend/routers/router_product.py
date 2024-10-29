# routers/router_product.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud_product  # Correct path to crud file
from schemas import schema_product  # Correct path to schema file
from config.database import get_db

router = APIRouter()

@router.post("/", response_model=schema_product.Product)
def create_product(product: schema_product.ProductCreate, db: Session = Depends(get_db)):
    return crud_product.create_product(db=db, product=product)

@router.get("/{product_id}", response_model=schema_product.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud_product.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/", response_model=list[schema_product.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_product.get_products(db, skip=skip, limit=limit)

@router.put("/{product_id}", response_model=schema_product.Product)
def update_product(product_id: int, product: schema_product.ProductCreate, db: Session = Depends(get_db)):
    return crud_product.update_product(db, product_id=product_id, product=product)

@router.delete("/{product_id}", response_model=schema_product.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud_product.delete_product(db, product_id=product_id)
