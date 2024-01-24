from fastapi import FastAPI, Depends, HTTPException
from model import SessionLocal, Restaurant, Base
from sqlalchemy.orm import Session
from api import RestaurantResponseItem, RestaurantResponseAll, RestaurantCreate

 
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API endpoint to read all items
@app.get("/restaurants/", response_model=list[RestaurantResponseItem])
async def read_restaurants(db: Session = Depends(get_db)):
    db_item = db.query(Restaurant)#.filter(Restaurant.id == restaurant_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# API endpoint to read an item by ID
@app.get("/restaurants/{restaurant_id}", response_model=RestaurantResponseItem)
async def read_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# API endpoint to create an item
@app.post("/restaurants/create", response_model=RestaurantResponseItem)
async def create_restaurant(item: RestaurantCreate, db: Session = Depends(get_db)):
    db_item = Restaurant(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
 

if __name__ == "__main__":
    import uvicorn
 
    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)