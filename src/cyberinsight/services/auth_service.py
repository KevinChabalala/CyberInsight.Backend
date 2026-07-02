from cyberinsight.models.user import User
from cyberinsight.repositories.user_repository import UserRepository
from cyberinsight.schemas.auth_schema import LoginRequest, RegisterRequest
from cyberinsight.utils.security import (
    create_access_token,
    hash_password,
    verify_password,
)


class AuthService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, request: RegisterRequest) -> User:

        existing_user = self.repository.get_by_email(request.email)

        if existing_user:
            raise ValueError("Email already registered.")

        user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password_hash=hash_password(request.password),
        )

        return self.repository.create(user)

    def login(self, request: LoginRequest) -> str:

        user = self.repository.get_by_email(request.email)

        if user is None:
            raise ValueError("Invalid email or password.")

        if not verify_password(request.password, user.password_hash):
            raise ValueError("Invalid email or password.")

        return create_access_token(str(user.id))