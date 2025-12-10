from http import HTTPStatus

from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from fastzero.schema import UserDB, UserList, UserPublic, UserSchema

app = FastAPI()
DATABASE = []


# Pega a lista de usuários
@app.get('/users/', response_model=UserList, status_code=HTTPStatus.OK)
def read_users():
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from fastzero.settings import Settings
    from fastzero.models import User
    from sqlalchemy import select
    
    engine = create_engine(Settings().DATABASE_URL)
    session = Session(engine)

    users = session.scalars(
        select(User)
    )
    
    return {'users': users.all()}


# Cria um novo Usuário
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from fastzero.settings import Settings
    from fastzero.models import User
    from sqlalchemy import select
    
    print(Settings().DATABASE_URL)
    engine = create_engine(Settings().DATABASE_URL)
    session = Session(engine)
    
    db_user: User | None = session.scalar(
        select(User).where(
            (User.email == user.email) | (User.username == user.username)
        )
    )
    
    if db_user: # Caminho Triste
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Username already exists!",
            )
        
        if db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Email already exists!"
            )
    
    #Caminho feliz
    db_user = User(
        **user.model_dump()
    )
    
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    
    return db_user



# Atualizar Usuário
@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from fastzero.settings import Settings
    from fastzero.models import User
    from sqlalchemy import select
    
    engine = create_engine(Settings().DATABASE_URL)
    session = Session(engine)
    
    user_db = session.scalar(select(User).where(User.id == user_id))
    print(user_db)
    if not user_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
        
    user_db.username = user.username  
    user_db.email = user.email  
    user_db.password = user.password  
    session.commit()
    session.refresh(user_db)
    
    print("\033[32mDEU CERTO\033[m")
    return user_db


# Deletar usuário
@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from fastzero.settings import Settings
    from fastzero.models import User
    from sqlalchemy import select
    
    engine = create_engine(Settings().DATABASE_URL)
    session = Session(engine)
    
    
    if not session.scalar(select(User).where(User.id == user_id)):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    
    
    db_user: User | None = session.scalar(
        select(User).where(
            User.id == user_id
        )
    )
    
    session.delete(db_user)
    session.commit()
    
    return db_user
