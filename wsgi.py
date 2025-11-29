from app import app

# Application entry point for WSGI servers
application = app  # Required name "application" for many servers

if __name__ == "__main__":
    app.run()
