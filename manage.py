from flask.ext.script import Manager, Server
from features_app.app import current_app

@manager.command
def worker():
    app = create_app()
    from musiclistr.queue_runner import queue_daemon
    queue_daemon(app)


# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

if __name__ == "__main__":
    manager.run()

