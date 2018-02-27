''' Dev Server '''
import cointracker
from flask_cors import CORS

my_app = cointracker.app
CORS(my_app)

if __name__ == "__main__":
    my_app.run(host='0.0.0.0')
