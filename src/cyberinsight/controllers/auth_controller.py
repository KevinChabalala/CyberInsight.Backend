from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status

from cyberinsight.core.database import get_db
from cyberinsight.core.dependencies import get_current_user
from cyberinsight.repositories.user_repository import UserRepository
from cyberinsight.schemas.auth_schema import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from cyberinsight.services.auth_service import AuthService
from cyberinsight.models.user import User


router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    repository = UserRepository(db)
    service = AuthService(repository)

    try:
        return service.register(request)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):

    repository = UserRepository(db)
    service = AuthService(repository)

    try:
        token = service.login(request)

        return {
            "access_token": token,
            "token_type": "bearer",
        }

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )


@router.get(
    "/me",
    response_model=UserResponse,
)
def me(
    current_user: User = Depends(get_current_user),
):
    return current_user