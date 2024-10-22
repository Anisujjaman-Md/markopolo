import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.database import DATABASE_URL
from app.models import Base
