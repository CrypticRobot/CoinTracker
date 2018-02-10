''' Dev Server '''
import cointracker

my_app = cointracker.app

if __name__ == "__main__":
    my_app.run(host='0.0.0.0')
