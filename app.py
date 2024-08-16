from flask import Flask, request, redirect, url_for, render_template, flash
from models import db, Realizar
"""configuração da aplicação"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SECRET_KEY'] = 'mysecretkey'
db.init_app(app)

"""rota da aplicação"""
@app.route('/')
def index():
    items = Realizar.query.all()
    return render_template('index.html', items=items)


"""a seguir a direção de cada funcionalidade do CRUD onde apresenta a Criação do objeto, Visualzação, Edição e Deleção 
    com base nos objetos salvos no banco de dados"""
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form.get('description')
        if not name:
            flash('Name is required!')
            return redirect(url_for('create'))
        new_item = Realizar(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Realizar.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form.get('description')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', item=item)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    item = Realizar.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
