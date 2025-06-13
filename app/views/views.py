from app import app
from flask import render_template
from flask import url_for, request

@app.route('/') #decorator
def homePage():
    usuario = 'Gustavo'
    return  render_template('index.html', usuario=usuario)


@app.route('/nova')
def nova():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
        print(f'Pesquisa: {pesquisa}')
        # Aqui você pode adicionar lógica para salvar os dados no banco de dados
        
    
    return render_template('contato.html')