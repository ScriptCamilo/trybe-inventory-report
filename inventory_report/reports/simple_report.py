# evaluator
from datetime import datetime


class SimpleReport:
    def generate(products):
        current_date = datetime.now().strftime('%Y/%M/%D')
        manufacturing_date = [product['data_de_fabricacao']
                              for product in products]
        expiration_date = [product['data_de_validade'] for product in products
                           if product['data_de_validade'] > current_date]
        stock = [product['nome_da_empresa'] for product in products]
        return (
          f'Data de fabricação mais antiga: {min(manufacturing_date)}\n'
          f'Data de validade mais próxima: {min(expiration_date)}\n'
          f'Empresa com maior quantidade de produtos estocados: {max(stock)}\n'
        )
