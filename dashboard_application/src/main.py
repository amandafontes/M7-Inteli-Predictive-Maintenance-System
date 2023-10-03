from fastapi import FastAPI, Request, Response, Depends, HTTPException
from security import hash_password, verify_password
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from models import User

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Middleware para evitar logs indesejados
@app.middleware("http")
async def remove_favicon(request: Request, call_next):
    if request.url.path == "/favicon.ico":
        return Response(content="", media_type="image/x-icon")
    response = await call_next(request)
    return response

# Rota principal
@app.get("/")
def root():
    return {"message": "Hello World"}

# Rota de registro de usuários
@app.post("/register/")
def register_user(username: str, password: str, db: Session = Depends(get_db)):
    hashed_password = hash_password(password)
    db_user = User(username=username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Rota de login de usuários
@app.post("/login/")
def login_user(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user is None or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    return {"message": "Login bem-sucedido"}