from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Annotated, Optional
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL="sqlite:///./test.db"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
Sesssional=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

class Movie(Base):
    __tablename__="movies"

    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)
    intro=Column(String, index=True)
    rating=Column(Integer, index=True)
    
class AddMovieForm(BaseModel):
    name:str
    intro:str
    rating:int

Base.metadata.create_all(bind=engine)


with Session(engine) as session:
    # session.add(movie_1)
    session.commit()
    # session.refresh(movie_1)

app=FastAPI()

templates=Jinja2Templates(directory="templates")

@app.api_route("/", methods=["GET","POST"],response_class=HTMLResponse)
async def read_root(request: Request):
    movies=session.query(Movie).all()
    return templates.TemplateResponse(
        request=request, name="index.html", context={"movies":movies})
    


@app.api_route("/add", methods=["GET","POST"])
async def add(request: Request, 
              name:Annotated[str, Form()]=None,
              intro:Annotated[str, Form()]=None,
              rating:Annotated[int, Form()]=None):
    if request.method =="GET":
        return templates.TemplateResponse("add.html",{"request":request})
    
    if request.method =="POST":
        new_movie=Movie(
            name=name,
            intro=intro,
            rating=rating
        )
        session.add(new_movie)
        session.commit()
        return RedirectResponse(url="/")
    
@app.get("/delete/{movie_id}")
def delete(movie_id:int):
    with Session(engine) as session:
        movie=session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        session.delete(movie)
        session.commit()
        return RedirectResponse(url="/")
    

@app.api_route("/edit/{movie_id}", methods=["GET","POST"])
def edit(request: Request,movie_id:int,rating: Annotated[int, Form()] = None):
    with Session(engine) as session:
        movie=session.get(Movie, movie_id)
        if request.method=="POST":
            movie.rating=rating
            session.commit()
            return RedirectResponse(url="/")
        return templates.TemplateResponse("edit.html",{"request":request, "movie":movie})
    
