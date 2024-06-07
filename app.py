from flask import Flask, render_template, request

app = Flask(__name__)

def inferencia_diabetes(obesidad, historial_familiar, sedentarismo):
    tratamiento = ""
    if obesidad and historial_familiar:
        factor_riesgo = "Alto riesgo de diabetes tipo 2"
        tratamiento = "Se recomienda una dieta balanceada y ejercicio regular. Consulte a un médico para evaluación y seguimiento."
    elif obesidad and sedentarismo:
        factor_riesgo = "Riesgo alto de diabetes tipo 2"
        tratamiento = "Se recomienda una dieta saludable y ejercicio regular para reducir el riesgo de desarrollar diabetes tipo 2."
    elif obesidad:
        factor_riesgo = "Riesgo moderado de diabetes tipo 2"
        tratamiento = "Adoptar hábitos alimenticios más saludables y realizar actividad física regular pueden reducir el riesgo de diabetes tipo 2."
    elif historial_familiar and sedentarismo:
        factor_riesgo = "Riesgo moderado de diabetes tipo 2"
        tratamiento = "Es importante mantener un estilo de vida activo y controlar la dieta para reducir el riesgo de desarrollar diabetes tipo 2."
    elif historial_familiar:
        factor_riesgo = "Riesgo bajo de diabetes tipo 2"
        tratamiento = "Mantener un estilo de vida saludable y realizar chequeos médicos regulares puede ayudar a prevenir la diabetes tipo 2."
    elif sedentarismo:
        factor_riesgo = "Riesgo bajo de diabetes tipo 2"
        tratamiento = "Para reducir el riesgo de diabetes tipo 2, se recomienda realizar actividad física regular y mantener una dieta equilibrada."
    else:
        factor_riesgo = "Riesgo desconocido"
        tratamiento = "Se recomienda consultar a un médico para una evaluación adecuada del riesgo de diabetes tipo 2."

    return factor_riesgo, tratamiento

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inferencia', methods=['POST'])
def inferir_diabetes():
    # Mapear los nombres de los campos del formulario a versiones más legibles
    nombres_campos = {
        'obesidad': 'Obesidad',
        'historial_familiar': 'Historial Familiar de Diabetes Tipo 2',
        'sedentarismo': 'Estilo de Vida Sedentario'
    }
    
    # Obtener los datos del formulario enviado por el usuario y transformar los nombres de los campos
    valores_usuario = ", ".join([nombres_campos[key] for key in request.form if request.form.get(key) == '1'])

    # Obtener los valores seleccionados por el usuario
    obesidad = bool(request.form.get('obesidad', False))
    historial_familiar = bool(request.form.get('historial_familiar', False))
    sedentarismo = bool(request.form.get('sedentarismo', False))

    # Realizar la inferencia
    resultado_inferencia, tratamiento = inferencia_diabetes(obesidad, historial_familiar, sedentarismo)

    # Renderizar la plantilla HTML con el resultado de la inferencia
    return render_template('index.html', resultado=resultado_inferencia, tratamiento=tratamiento, valores_usuario=valores_usuario)

if __name__ == '__main__':
    app.run(debug=True)
