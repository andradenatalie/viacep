from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.services.endereco_service import (
    adicionar_endereco, obter_endereco, atualizar_endereco, deletar_endereco
)

endereco_bp = Blueprint("endereco", __name__)

"""Camada de aplicação (App Layer) expõe as APIs REST."""

@endereco_bp.route("/endereco", methods=["POST"])
@swag_from({
    "tags": ["Endereços"],
    "summary": "Adicionar um endereço",
    "description": "Recebe um CEP, consulta o ViaCEP e armazena no banco",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "cep": {"type": "string", "example": "01001-000"}
                },
                "required": ["cep"]
            }
        }
    ],
    "responses": {
        "201": {"description": "Endereço salvo com sucesso"},
        "400": {"description": "Erro na requisição"},
        "404": {"description": "CEP inválido"}
    }
})
def criar_endereco():
    """Cria o registro do CEP no banco de dados"""
    data = request.json
    response, status = adicionar_endereco(data.get("cep"))
    return jsonify(response), status

@endereco_bp.route("/endereco/<cep>", methods=["GET"])
@swag_from({
    "tags": ["Endereços"],
    "summary": "Buscar um endereço",
    "description": "Consulta um endereço salvo no banco de dados pelo CEP",
    "parameters": [
        {
            "name": "cep",
            "in": "path",
            "type": "string",
            "required": True,
            "exemplo": "01001-000"
        }
    ],
    "responses": {
        "200": {"description": "Quando endereço encontrado"},
        "404": {"description": "Quando CEP não encontrado"}
    }
})
def buscar_endereco(cep):
    """Busca o registro do CEP no banco de dados"""
    response = obter_endereco(cep)
    status = 200 if "erro" not in response else 404
    return jsonify(response), status

@endereco_bp.route("/endereco/<cep>", methods=["PUT"])
@swag_from({
    "tags": ["Endereços"],
    "summary": "Atualizar um endereço",
    "description": "Marca o endereço como 'alterado'",
    "parameters": [
        {
            "name": "cep",
            "in": "path",
            "type": "string",
            "required": True,
            "exemplo": "01001-000"
        }
    ],
    "responses": {
        "200": {"description": "Endereço atualizado"},
        "404": {"description": "CEP não encontrado"}
    }
})
def editar_endereco(cep):
    """Edita o registro do CEP no banco de dados"""
    response = atualizar_endereco(cep)
    status = 200 if "erro" not in response else 404
    return jsonify(response), status

@endereco_bp.route("/endereco/<cep>", methods=["DELETE"])
@swag_from({
    "tags": ["Endereços"],
    "summary": "Remover um endereço",
    "description": "Deleta um endereço salvo no banco de dados pelo CEP",
    "parameters": [
        {
            "name": "cep",
            "in": "path",
            "type": "string",
            "required": True,
            "examplo": "01001-000"
        }
    ],
    "responses": {
        "200": {"description": "Endereço removido"},
        "404": {"description": "CEP não encontrado"}
    }
})
def remover_endereco(cep):
    """Deleta o registro do CEP no banco de dados"""
    response = deletar_endereco(cep)
    status = 200 if "erro" not in response else 404
    return jsonify(response), status
