from unicodedata import name

import sendgrid
from flask import (Blueprint, current_app, redirect, render_template, request,
                   url_for)
from sendgrid.helpers.mail import *

from __init__ import create_app

bp = Blueprint("portfolio", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    return render_template("portfolio/index.html")


@bp.route("/mail", methods=["POST", "GET"])
def mail():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if request.method == "POST":
        send_email(name, email, message)
        return render_template("portfolio/send_mail.html")
    return redirect(url_for("portfolio.index"))


def send_email(name, email, message):
    mi_email = "mhernanez95@gmail.com"
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config["SENDGRID_KEY"])

    from_email = Email(mi_email)
    to_email = To(
        mi_email,
        substitutions={
            "-name-": name,
            "-email-": email,
            "-message-": message,
        },
    )

    html_content = """


    <p>Hola Mike, tienes un nuevo contacto desde la web:</p>
    <p>Nombre: -name- </p>
    <p>Correo: -email- </p>
    <p>Message: -message- </p>
    
    """
    mail = Mail(
        mi_email, to_email, "Nuevo contacto desde la web", html_content=html_content
    )
    response = sg.client.mail.send.post(request_body=mail.get())

