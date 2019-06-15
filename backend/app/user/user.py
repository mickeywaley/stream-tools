from mongo_thingy import connect, Thingy


from main import app

connect()


class User(Thingy):
    pass;


User.add_view(name="everything", defaults=False, include="username")

User.add_view(name="public", defaults=True, exclude="password")
