from zeep import Client

'''informa o endereço do WSDL do serviço SOAP'''
wsdl_url = 'https://web.comercialmariano.com.br:31301/g5-senior-services/sapiens_Synccom_senior_g5_co_mcm_ven_pedidos?wsdl'
client = Client(wsdl=wsdl_url)

# Chama o serviço SOAP com os parâmetros formatados corretamente
def exportar_pedidos(parameters):
    '''Implementa a correta formatação dos valores de response para o serviço SOAP ExportarPedidos'''
    response = client.service.ExportarPedidos(
        user=parameters['user'],
        password=parameters['password'],
        encryption=parameters['encryption'],
        parameters={
            'exportacaoPadraoVarejo': {
                'codEmp': parameters['codEmp'],
                'codFil': parameters['codFil'],
                'consulta': {
                    'numPed': parameters['numPed']
                },
                'tipoIntegracao': parameters['tipoIntegracao'],
                'quantidadeRegistros': parameters['quantidadeRegistros'],
            },
            'sigInt': parameters['sigInt']
        }
    )
    return response
