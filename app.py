from flask import Flask, render_template, request

app = Flask(__name__)

def inferencia_diabetes(obesidad, historial_familiar, sedentarismo):
    if obesidad and historial_familiar:
        return "Alto riesgo de diabetes tipo 2"
    elif obesidad and sedentarismo:
        return "Riesgo moderado de diabetes tipo 2"
    elif historial_familiar:
        return "Riesgo bajo de diabetes tipo 2"
    else:
        return "Riesgo desconocido"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inferencia', methods=['POST'])
def inferir_diabetes():
    # Obtener los datos del formulario enviado por el usuario
    obesidad = bool(request.form.get('obesidad'))
    historial_familiar = bool(request.form.get('historial_familiar'))
    sedentarismo = bool(request.form.get('sedentarismo'))

    # Realizar la inferencia
    resultado_inferencia = inferencia_diabetes(obesidad, historial_familiar, sedentarismo)

    # Renderizar la plantilla HTML con el resultado de la inferencia
    return render_template('resultado.html', resultado=resultado_inferencia)

if __name__ == '__main__':
    app.run(debug=True)
