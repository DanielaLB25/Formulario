from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal con el menú
@app.route('/')
def index():
    return render_template('index.html')

# Inscripción en curso
@app.route('/inscripcion_curso', methods=['GET', 'POST'])
def inscripcion_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        return render_template('resultado.html', titulo="Inscripción en Curso", datos={
            'Nombre': nombre,
            'Apellido': apellido,
            'Curso': curso
        })
    return render_template('inscripcion_curso.html')

# Registro de usuario
@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        return render_template('resultado.html', titulo="Registro de Usuario", datos={
            'Nombre': nombre,
            'Apellido': apellido,
            'Correo Electrónico': correo
        })
    return render_template('registro_usuario.html')

# Registro de productos
@app.route('/registro_producto', methods=['GET', 'POST'])
def registro_producto():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return render_template('resultado.html', titulo="Registro de Producto", datos={
            'Producto': producto,
            'Categoría': categoria,
            'Existencia': existencia,
            'Precio': precio
        })
    return render_template('registro_producto.html')

# Registro de libros
@app.route('/registro_libro', methods=['GET', 'POST'])
def registro_libro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        return render_template('resultado.html', titulo="Registro de Libro", datos={
            'Título': titulo,
            'Autor': autor,
            'Resumen': resumen,
            'Medio': medio
        })
    return render_template('registro_libro.html')

if __name__ == '__main__':
    app.run(debug=True)
