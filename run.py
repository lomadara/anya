import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.app import app as application
application.run(debug=False)