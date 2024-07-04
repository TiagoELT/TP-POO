from typing import Type
import pandas as pd
from abc import ABC, abstractmethod

from interfaces.Interface_Employee import Employee

class User(ABC):
    def __init__(self, user_id: int, name: str, password: str, email: str, type: str) -> None:
        self.user_id = user_id
        self.name = name
        self.password = password
        self.email = email
        self.type = type
        self.path_dados = r'.\terminal_app\data'


    def get_employee_by_user(self) -> Type[Employee]:
        try:    
            employees_df = pd.read_csv(f'{self.path_dados}\\employees.csv')
            employee = employees_df[employees_df['user_id'] == self.user_id].iloc[0]
            return Employee(employee['employee_id'], employee['user_id'], employee['company_id'], employee['position'], employee['phone'])
        
        except Exception as e:
            print(f"Erro ao carregar funcionário do usuário! {e}")
            return None
    
    def listar_info_usuario(self) -> None:
        """
        @brief Função que lista as informações do usuário.
        """
        print(f"Nome: {self.name}")
        print(f"Email: {self.email}")
        print(f"Tipo: {self.type}")