IMOVEIS = [
    {
        "id": 1,
        "logradouro": "Nicole Common",
        "tipo_logradouro": "Travessa",
        "bairro": "Lake Danielle",
        "cidade": "Judymouth",
        "cep": "85184",
        "tipo": "casa em condominio",
        "valor": 488423.52,
        "data_aquisicao": "2017-07-29"
    },
    {
        "id": 2,
        "logradouro": "Price Prairie",
        "tipo_logradouro": "Travessa",
        "bairro": "Colonton",
        "cidade": "North Garyville",
        "cep": "93354",
        "tipo": "casa em condominio",
        "valor": 260069.89,
        "data_aquisicao": "2021-11-30"
    },
    {
        "id": 3,
        "logradouro": "Taylor Ranch",
        "tipo_logradouro": "Avenida",
        "bairro": "West Jennashire",
        "cidade": "Katherinefurt",
        "cep": "51116",
        "tipo": "apartamento",
        "valor": 815969.92,
        "data_aquisicao": "2020-04-24"
    }
]

def get_imoveis(cidade=None, tipo=None):
    resultado = IMOVEIS
    
    if cidade:
        resultado = [i for i in resultado if i["cidade"] == cidade]
        
    if tipo:
        resultado = [i for i in resultado if i["tipo"] == tipo]
        
    return resultado

def get_imovel(imovel_id):
    for imovel in IMOVEIS:
        if imovel["id"] == imovel_id:
            return imovel
    return None

def create_imovel(data):
    novo_id = max(i["id"] for i in IMOVEIS) + 1 if IMOVEIS else 1
    
    data["id"] = novo_id
    IMOVEIS.append(data)
    
    return novo_id

def update_imovel(imovel_id, data):
    for imovel in IMOVEIS:
        if imovel["id"] == imovel_id:
            imovel.update(data)
            return True
    return False

def delete_imovel(imovel_id):
    for imovel in IMOVEIS:
        if imovel["id"] == imovel_id:
            IMOVEIS.remove(imovel)
            return True
    return False