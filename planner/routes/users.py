from database.connection import Database
from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])
user_database = Database(User)


@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким email уже существует в MongoDB",
        )
    await user_database.save(user)
    return {
        "message": "Пользователь успешно зарегистрирован в MongoDB! (Марданов Рустем)"
    }


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь с таким email не найден.",
        )
    if user_exist.password == user.password:
        return {"message": "Вход выполнен успешно! (Марданов Рустем)"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверные учетные данные (пароль)",
    )