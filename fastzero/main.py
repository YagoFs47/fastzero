from http import HTTPStatus

from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from fastzero.schema import UserDB, UserList, UserPublic, UserSchema

app = FastAPI()
DATABASE = []


# Pega a lista de usuários
@app.get('/users/', response_model=UserList, status_code=HTTPStatus.OK)
def read_users():

    return {'users': DATABASE}


# Cria um novo Usuário
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(DATABASE) + 1)
    DATABASE.append(user_with_id)
    return user_with_id


# Atualizar Usuário
@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(DATABASE):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    DATABASE[user_id - 1] = UserDB(
        id=user_id, **user.model_dump()
    ).model_dump()
    return DATABASE[user_id - 1]


# Deletar usuário
@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(DATABASE):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_deleted = DATABASE.pop(user_id - 1)
    return user_deleted
