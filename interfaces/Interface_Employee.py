from typing import Type
import pandas as pd

from interfaces.Interface_Company import Company

class Employee:
    def __init__(self, employee_id: int, user_id: int, company_id: int, position: str, phone: str) -> None:
        self.employee_id = employee_id
        self.user_id = user_id
        self.company_id = company_id
        self.position = position
        self.phone = phone
        self.path_dados = r'.\terminal_app\data'

    def get_company_by_employee(self) -> Type[Company]:
        try:
            companies_df = pd.read_csv(f'{self.path_dados}\\companies.csv')
            company = companies_df[companies_df['company_id'] == self.company_id].iloc[0]
            return Company(company['company_id'], company['name'], company['address'], company['phone'], company['cnpj'])
        except Exception as e:
            print(f"Erro ao carregar empresa do funcionário! {e}")
            return None
    
    def listar_info_funcionario(self) -> None:
        """
        @brief Função que lista as informações do funcionário.
        """
        print(f"Cargo: {self.position}")
        print(f"Telefone: {self.phone}")