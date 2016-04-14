from flask.ext.script import Manager


from app import app


manager = Manager(app) #instantiate a manager


if __name__ == '__main__'
     manager.run()
