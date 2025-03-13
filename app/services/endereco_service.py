from app.adapters.database import db
from app.domain.models import Endereco
from app.adapters.via_cep import consultar_cep

"""Camada de serviço (Service Layer) contém a lógica de negócio"""

def adicionar_endereco(cep):
    if not cep:
        return {"erro": "CEP não informado"}, 400
    
    cep_info = consultar_cep(cep)
    if not cep_info:
        return {"erro": "CEP inválido"}, 404

    endereco = Endereco(
        cep=cep_info["cep"],
        logradouro=cep_info["logradouro"],
        complemento=cep_info["complemento"],
        bairro=cep_info["bairro"],
        localidade=cep_info["localidade"],
        uf=cep_info["uf"],
        ibge=cep_info.get("ibge"),
        gia=cep_info.get("gia"),
        ddd=cep_info.get("ddd"),
        siafi=cep_info.get("siafi"),
    )

    db.session.add(endereco)
    db.session.commit()

    return {"mensagem": "Endereço salvo com sucesso!", "dados": cep_info}, 201

def obter_endereco(cep):
    endereco = Endereco.query.filter_by(cep=cep).first()
    if not endereco:
        return {"erro": "CEP não encontrado no banco"}, 404

    return {
        "cep": endereco.cep,
        "logradouro": endereco.logradouro,
        "complemento": endereco.complemento,
        "bairro": endereco.bairro,
        "localidade": endereco.localidade,
        "uf": endereco.uf,
        "ibge": endereco.ibge,
        "gia": endereco.gia,
        "ddd": endereco.ddd,
        "siafi": endereco.siafi,
        "alterado": endereco.alterado,
    }

def atualizar_endereco(cep):
    endereco = Endereco.query.filter_by(cep=cep).first()
    if not endereco:
        return {"erro": "CEP não encontrado no banco"}, 404

    endereco.alterado = "ok"
    db.session.commit()
    return {"mensagem": "Endereço atualizado com sucesso!", "alterado": "ok"}

def deletar_endereco(cep):
    endereco = Endereco.query.filter_by(cep=cep).first()
    if not endereco:
        return {"erro": "CEP não encontrado no banco"}, 404

    db.session.delete(endereco)
    db.session.commit()
    return {"mensagem": "Endereço removido com sucesso!"}
