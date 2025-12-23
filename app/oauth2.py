# JWT & Auth related imports
from jose import JWTError, jwt
from datetime import datetime, timedelta

from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app import schemas   # TokenData schema

# This is the OAuth2 scheme used by FastAPI (API working)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ---------------- JWT SETTINGS ----------------
SECRET_KEY = "secret"              # this is secret key
ALGORITHM = "HS256"                # hashing algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 1  # token expiry time
# ----------------------------------------------


# This function creates JWT access token (API working)
def create_access_token(data: dict):
    to_encode = data.copy()

    # token expiry time
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # generate JWT token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# This function verifies JWT token (API working)
def verify_access_token(token: str, credentials_exception):
    try:
        # decode token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # get user id from token
        user_id: str = payload.get("user_id")

        if user_id is None:
            raise credentials_exception

        # return token data
        token_data = schemas.TokenData(id=user_id)
        return token_data

    except JWTError:
        raise credentials_exception


# This dependency gets current logged-in user (API working)
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # verify token and return user
    return verify_access_token(token, credentials_exception)
