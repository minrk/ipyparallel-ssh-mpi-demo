from jupyter_server.auth import passwd

c = get_config()  # noqa

# this is wildly insecure, but convenient for demo purposes
c.ServerApp.password = passwd("whocares")

# stable cookie secret to preserve creds across restart
c.ServerApp.cookie_secret = b'3efc80c05677633ed019fc99fbb9d'
