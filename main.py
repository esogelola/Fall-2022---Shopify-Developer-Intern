from inventory import create_app

if __name__ == '__main__':  # Makes sure this is the main process

    app = create_app()
    app.run(host='0.0.0.0', port=80)  # Starts the site
