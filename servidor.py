from flask import Flask, render_template_string, request, redirect, jsonify
import json
import utils

servidor = Flask(__name__)

config = servidor.config
test_client = servidor.test_client

@servidor.route('/')
def pagina_imoveis():
    return render_template_string('''
        <p>Servidor rodando...</p>
        <p>Acesse /imoveis para acessar a API.</p>
    ''')

@servidor.route('/imoveis', methods=["GET"])
def get_imoveis():
    cidade = request.args.get("cidade")
    tipo = request.args.get("tipo")

    imoveis = utils.get_imoveis(cidade, tipo)

    return json.dumps(imoveis), 200

@servidor.route('/imoveis/<int:imovel_id>', methods=["GET"])
def get_imovel(imovel_id):
    imovel = utils.get_imovel(imovel_id)
    
    if not imovel:
        return "Imóvel não encontrado", 404
    
    return json.dumps(imovel), 200

@servidor.route('/imoveis', methods=["POST"])
def create_imovel():
    data = request.get_json()
    
    if isinstance(data, str):
        data = json.loads(data)
        
    campos_obrigatorios = [
        "logradouro",
        "tipo_logradouro",
        "bairro",
        "cidade",
        "cep",
        "tipo",
        "valor",
        "data_aquisicao"
    ]
    
    if not all(campo in data for campo in campos_obrigatorios):
        return "Dados insuficientes para adicionar o imóvel", 400
    
    try:
        float(data["valor"])
    except:
        return "Dados inválidos para adicionar o imóvel", 400
    
    novo_id = utils.create_imovel(data)
    
    return jsonify({"id": novo_id, "mensagem": "Imóvel adicionado com sucesso"}), 201

@servidor.route("/imoveis/<int:imovel_id>", methods=["PUT"])
def update_imovel(imovel_id):
    data = request.get_json()
    
    atualizar = utils.update_imovel(imovel_id, data)
    
    if not atualizar:
        return "Imóvel não encontrado", 404
    
    return jsonify({"message": "Imóvel atualizado com sucesso"}), 200

@servidor.route("/imoveis/<int:imovel_id>", methods=["DELETE"])
def delete_imovel(imovel_id):    
    deletar = utils.delete_imovel(imovel_id)
    
    if not deletar:
        return "Imóvel não encontrado", 404
    
    return jsonify({"message": "Imóvel removido com sucesso"}), 200
    
if __name__ == '__main__':
    servidor.run(debug=True)