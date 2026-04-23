from fastapi import Depends

from core.database import session
from user.model import User

from .utils import verify_token
from .routes import oauth2_schema


def get_current_user(db:session, token: str = Depends(oauth2_schema)):
    payload = verify_token(token)

    if payload is None or type(payload) != dict:
        # raise HTTPException(status_code=401, detail="Invalid token")
        return None
    # breakpoint()
    user_id = payload.get("sub")

    if user_id is None:
        # raise HTTPException(status_code=401, detail="Invalid credentials")
        return None

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        # raise HTTPException(status_code=404, detail="User not found")
        return None

    return user