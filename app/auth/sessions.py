from uuid import uuid4

sessions = {}

def create_session(user_id: int) -> str:
    session_id = str(uuid4())
    sessions[session_id] = user_id
    return session_id

def get_user_from_session(session_id: str | None):
    if session_id is None:
        return None
    return(sessions.get(session_id))