from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.product import Product
from app.extensions import db
from datetime import datetime

bp = Blueprint('products', __name__, url_prefix='/productos')

@bp.route('/')
def Listar():
    productos = Product.query.order_by(Product.fecha_creacion.desc()).all()
    return render_template('products/listar.html', productos=productos)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        try:
            producto=Product(
                nombre=request.form['nombre'],
                descripcion=request.form['descripcion'],
                precio=float(request.form['precio']),
                stock=int(request.form['stock']),
                categoria=request.form['categoria']
            )
            db.session.add(producto)
            db.session.commit()
            flash('Producto creado exitosamente.', 'success')
            return redirect(url_for('products.listar'))
        except ValueError:
            db.session.rollback()
            flash(f'error al crear el producto: {str(e)}', 'danger')
    return render_template('products.crear.html')

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    producto = Product.query.get_or_404(id)

    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        descripcion = request.form['descripcion'].strip()
        precio = request.form['precio'].strip()
        stock = request.form['stock'].strip()
        categoria = request.form['categoria'].strip()

        if not nombre or not precio or not stock:
            flash('Nombre, precio y stock son obligatorios.', 'error')
            return redirect(url_for('productos.editar_producto', id=id))

        try:
            producto.precio = float(precio)
            producto.stock = int(stock)
        except ValueError:
            flash('Precio debe ser numérico y stock debe ser un número entero.', 'error')
            return redirect(url_for('productos.editar_producto', id=id))

        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.categoria = categoria

        db.session.commit()
        flash('Producto actualizado exitosamente.', 'success')
        return redirect(url_for('productos.listar_productos'))

    return render_template('form_producto.html', accion='Editar', producto=producto)

@bp.route('/eliminar/<int:id>')
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado exitosamente.', 'success')
    return redirect(url_for('productos.listar_productos'))
