from sqlalchemy.orm import Session
from . import models, schemas

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_reviews(db: Session, product_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Review).filter(models.Review.product_id == product_id).offset(skip).limit(limit).all()
