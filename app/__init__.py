import os

from flask import Flask

import portfolio


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get("SENDGRID_API_KEY"),
    )

    app.register_blueprint(portfolio.bp)

    app.run(host="0.0.0.0", port=4000, debug=True)


if __name__ == "__main__":
    create_app()
