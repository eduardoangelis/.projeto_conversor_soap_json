from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from .soap_client import exportar_pedidos

'''Instanciando a classe APIRouter para criar as rotas da aplicação'''
router = APIRouter()


'''Criando a classe para receber os parametros da requisição validada pelo pydantic'''
class PedidosExportarPedidosIn(BaseModel):
    '''Criando os atributos de request com os tipos'''
    user: str
    password: str
    encryption: int
    codEmp: int
    codFil: int
    numPed: int
    tipoIntegracao: str
    quantidadeRegistros: int
    sigInt: str


'''Criando a rotas para consultar pedidos'''
@router.post("/") 
async def consultar_pedidos_endpoint(parameters: PedidosExportarPedidosIn):
    try:
        '''Cria um dicionario com os parametros passados na requisição'''
        params = parameters.dict()
        '''Verifique se todas as chaves necessárias estão presentes em params'''
        required_keys = ['user', 'password', 'encryption', 'codEmp', 'codFil', 'numPed', 'tipoIntegracao', 'quantidadeRegistros', 'sigInt']
        '''Se todos os parametros necessários estiverem presentes, chama a função exportar_pedidos com os parametros passados na requisição'''
        if not all(key in params for key in required_keys):
            '''Se algum parametro estiver faltando, retorna um erro 400 com a mensagem "Missing required parameters'''
            raise HTTPException(status_code=400, detail="Missing required parameters")
        response = exportar_pedidos(params)
        return response
    except Exception as e:
        '''Se ocorrer algum erro, retorna um erro 500 com a mensagem do erro'''
        raise HTTPException(status_code=500, detail=str(e))