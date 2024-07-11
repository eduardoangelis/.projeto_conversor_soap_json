from zeep import Client, xsd
import logging.config

'''
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
        },
    }
})
'''

wsdl_url = 'https://web.comercialmariano.com.br:31301/g5-senior-services/sapiens_Synccom_senior_g5_co_mcm_ven_pedidos?wsdl'
client = Client(wsdl=wsdl_url)

def exportar_pedidos(parameters):
    # Chama o serviço SOAP com os parâmetros formatados corretamente
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
