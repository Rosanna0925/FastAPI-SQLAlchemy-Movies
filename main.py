from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing_extensions import Annotated
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker, Session

from database import engine, SessionLocal
from models import Movie

    
class AddMovieForm(BaseModel):
    name:str
    intro:str
    rating:int

app=FastAPI()

templates=Jinja2Templates(directory="templates")

@app.api_route("/", methods=["GET","POST"],response_class=HTMLResponse)
async def read_root(request: Request):
    with SessionLocal() as session:
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
     with SessionLocal() as session:
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
    with SessionLocal() as session:
        movie=session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        session.delete(movie)
        session.commit()
    return RedirectResponse(url="/")
    

@app.api_route("/edit/{movie_id}", methods=["GET","POST"])
def edit(request: Request,movie_id:int,rating: Annotated[int, Form()] = None):
    with SessionLocal() as session:
        movie=session.get(Movie, movie_id)
        if request.method=="POST":
            movie.rating=rating
            session.commit()
            return RedirectResponse(url="/")
        return templates.TemplateResponse("edit.html",{"request":request, "movie":movie})
    

    
