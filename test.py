from datetime import datetime
import random

def UserID_generator():
    # Generate a unique UserID (e.g., using UUID or auto-increment in the database)
    UserID = datetime.now().strftime("%Y%m%d") + f"{random.randint(1, 9999):04d}" # Example format
    return UserID

timeCheck = datetime.now()
UserID = UserID_generator()
print (UserID)