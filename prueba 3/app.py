from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario_notas', methods=['GET', 'POST'])
def formulario_notas():
    estado = None
    promedio = None
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3
        estado = 'APROBADO' if promedio >= 40 and asistencia >= 75 else 'REPROBADO'
    return render_template('formulario_notas.html', estado=estado, promedio=promedio)

@app.route('/formulario_nombres', methods=['GET', 'POST'])
def formulario_nombres():
    nombre_largo = None
    longitud = None
    if request.method == 'POST':
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]
        nombre_largo = max(nombres, key=len)
        longitud = len(nombre_largo)
    return render_template('formulario_nombres.html', nombre_largo=nombre_largo, longitud=longitud)

if __name__ == '__main__':
    app.run(debug=True)
