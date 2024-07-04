import sys
from typing import Type
import pandas as pd

from login import Login

from interfaces.Interface_User import User
from interfaces.Interface_User_Admin import Admin_User
from interfaces.Interface_Employee import Employee
from interfaces.Interface_Company import Company
        

class Terminal_App():
    def __init__(self) -> None:
        self.nome_app = "Sistema Monitoramento de Armadilhas para Manejo de Fauna"
        self.path_dados = r'.\terminal_app\data'
        self.__usuario = None
        self.__employee = None
        self.__company = None
        self.__admin = None
        
    def inicializa_App(self) -> tuple[bool,bool]:
        """
        @brief Função que inicializa a aplicação e através do login do usuário, carrega os dados do usuário verificando se é admin ou não.
        @return Retorna uma tupla com dois valores booleanos. O primeiro valor indica se a inicialização foi bem sucedida e o segundo valor indica se o usuário é admin.
        """
        login_App = Login()
        print(f"Bem-vindo ao {self.nome_app}!\n")
        # Fazer login
        print("Faça login para acessar o sistema!\n")
        usuario = login_App.fazer_Login()
        if usuario == None:
            return False, None
        else:
            self.usuario = usuario
            print(f"Olá {self.usuario.name}! Seja bem-vindo(a)!\n")

            if self.carrega_Dados(usuario) == False:
                print("Erro ao carregar os dados do usuário!")
                return False, None
            else:
                print("Dados do usuário carregados com sucesso!")
                if self.usuario.type == "admin":
                    print("Usuário é admin")
                    print()
                    return True, True
                else:
                    print(f"Empresa: {self.company.name}")
                    print(f"Cargo: {self.employee.position}")
                    print()
                    return True, False
                
    def opcoes_Usuario_Admin(self) -> str:
        """
        @brief Função que exibe as opções para o usuário admin.
        @return Retorna a opção escolhida pelo usuário.
        """
        print("Qual operação você deseja fazer?")
        print("1 - Listar todas as empresas.")
        print("2 - Listar todos os funcionários de uma empresa.")
        print("3 - Listar todos os dispositivos de monitoramento de uma empresa.")
        print("4 - Cadastrar uma nova empresa.")
        print("5 - Cadastrar um novo funcionário.")
        print("6 - Cadastrar um novo dispositivo de monitoramento.")
        print("7 - Sair do programa!")

        print()
        flag_option_invalida = True
        option = input("Digite o número da operação que você que fazer: ")
        possiveis_options = ["1","2","3","4","5","6","7"]
        while(flag_option_invalida):        
            if option in possiveis_options:
                flag_option_invalida = False
                print()
                return option
            else:
                option = input("Opção inválida! Digite o número da operação de acordo com a lista acima: ")
    
    def handle_Opcoes_Admin(self, option: str) -> bool:
        """
        @brief Função que trata as opções do usuário admin.
        @param option Opção escolhida pelo usuário.
        @return Retorna True se a operação foi realizada com sucesso, caso contrário retorna False.
        """
        if option == "1":
            print("Listando todas as empresas!")
            self.admin.listar_Empresas()

        elif option == "2":
            print("Listando todos os funcionários de uma empresa!")
            company_id = self.admin.escolher_Empresa()
            print()
            if company_id != None:
                self.admin.listar_Funcionarios(company_id)           

        elif option == "3":
            print("Listando todos os dispositivos de monitoramento de uma empresa!")
            company_id = self.admin.escolher_Empresa()
            print()
            if company_id != None:
                self.admin.listar_Dispositivos(company_id)

        elif option == "4":
            print("Cadastrando uma nova empresa!")
            if self.admin.cadastrar_Nova_Empresa() == False:
                print("Erro ao cadastrar a nova empresa!")

        elif option == "5":
            print("Cadastrando um novo funcionário!")
            company_id = self.admin.escolher_Empresa()
            print()
            if company_id != None:
                if self.admin.cadastrar_Novo_Funcionario(company_id) == False:
                    print("Erro ao cadastrar o novo funcionário!")

        elif option == "6":
            print("Cadastrando um novo dispositivo de monitoramento!")
            company_id = self.admin.escolher_Empresa()
            print()
            if company_id != None:
                if self.admin.cadastrar_Novo_Dispositivo(company_id) == False:
                    print("Erro ao cadastrar o novo dispositivo de monitoramento!")

        elif option == "7":
            print(f"Obrigado por usar o {self.nome_app}!")
            sys.exit(0)
        else:
            print("Opção inválida! Digite novamente!")
        return True

    def opcoes_Usuario_Normal(self) -> str:
        """
        @brief Função que exibe as opções para um usuário Normal (que não é admin).
        @return Retorna a opção escolhida pelo usuário.
        """
        print("Qual operação você deseja fazer?")
        print("1 - Exibir resumo dos dados.")
        print("2 - Exibir informações do usuário.")
        print("3 - Exibir informações da empresa.")
        print("4 - Exibir áreas monitoradas.")
        print("5 - Adicionar uma nova área monitorada.")
        print("6 - Sair do programa!")
        print()
        flag_option_invalida = True
        option = input("Digite o número da operação que você que fazer: ")
        possiveis_options = ["1","2","3","4","5"]
        while(flag_option_invalida):        
            if option in possiveis_options:
                flag_option_invalida = False
                print()
                return option
            else:
                option = input("Opção inválida! Digite o número da operação de acordo com a lista acima: ")
    
    def handle_Opcoes_Normal(self, option: str) -> bool:
        """
        @brief Função que trata as opções do usuário Normal.
        @param option Opção escolhida pelo usuário.
        @return Retorna True se a operação foi realizada com sucesso, caso contrário retorna False.
        """
        if option == "1":
            print("Exibindo resumo dos dados!")
            self.company.exibir_Resumo()

        elif option == "2":
            print("Exibindo informações do usuário!")
            self.usuario.listar_info_usuario()
            self.employee.listar_info_funcionario()
            print()

        elif option == "3":
            self.company.listar_info_empresa()
            print()

        elif option == "4":
            print("Exibindo áreas monitoradas!")
            area_id = self.company.escolher_Area()
            print()
            if area_id != None:
                self.company.exibir_Area(area_id)
            else:
                print("Nenhuma área escolhida!")

        elif option == "5":
            print(f"Obrigado por usar o {self.nome_app}!")
            sys.exit(0)
        else:
            print("Opção inválida! Digite novamente!")        
        return True

    def nova_Interacao(self) -> bool:
        flag_operation = True
        print()
        while(flag_operation):
            continuar_script = input("Deseja fazer uma nova operação? Digite 'S' para Sim ou 'N' para Não: ")
            if continuar_script == "S":
                flag_operation = False
                print()
                return True                
            elif continuar_script == "N":
                print(f"Obrigado por usar o {self.nome_app}!")
                sys.exit(0)
            else:
                print("A opção digitada é inválida! Digite novamente!")

    def carrega_Dados(self,usuario: Type[User]) -> bool:
        """
        @brief Função que carrega os dados do usuário.
        @param usuario Objeto do tipo User.
        @return Retorna True se os dados foram carregados com sucesso, caso contrário retorna False.
        """
        if usuario.type == "admin":
            self.admin = Admin_User(usuario.user_id, usuario.name, usuario.password, usuario.email, usuario.type)
            if self.admin.carrega_Dados_Admin() == False:
                return False
            return True
        
        employee = usuario.get_employee_by_user()
        if employee == None:
            return True
        else:
            self.employee = employee
            company = employee.get_company_by_employee()
            self.company = company

            return True

    @property
    def usuario(self) -> User:
        return self.__usuario
    @usuario.setter
    def usuario(self, usuario: User) -> None:
        self.__usuario = usuario

    @property
    def employee(self) -> Employee:
        return self.__employee
    @employee.setter
    def employee(self, employee: Employee) -> None:
        self.__employee = employee
    
    @property
    def company(self) -> Company:
        return self.__company
    @company.setter
    def company(self, company: Company) -> None:
        self.__company = company

    @property
    def admin(self) -> Admin_User:
        return self.__admin
    @admin.setter
    def admin(self, admin: Admin_User) -> None:
        self.__admin = admin
