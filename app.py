from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = "clase_python_web_secreto"

USUARIOS_PERMITIDOS = {"Ana", "Luis", "María"}
BLOQUEADOS = {"Luis"}

@app.route("/", methods=["GET"])
def index():
    intentos = session.get("intentos", 0)
    ultimo = session.get("ultimo_nombre", "")
    return render_template("index.html", intentos=intentos, ultimo=ultimo)

@app.route("/procesar", methods=["POST"])
def procesar():
    nombre = request.form.get("nombre", "")
    nombre = nombre.strip()

    session["intentos"] = session.get("intentos", 0) + 1
    session["ultimo_nombre"] = nombre

    if nombre in USUARIOS_PERMITIDOS and nombre not in BLOQUEADOS and nombre !="":
        permitido= True
        mensaje="Acceso permitido"
    else:
        permitido= False
        mensaje="Acceso denegado"
    return render_template("resultado.html", nombre= nombre, permitido=permitido, mensaje=mensaje)

@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    session.clear()
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run(debug=True)
    

