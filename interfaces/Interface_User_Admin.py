import pandas as pd

from interfaces.Interface_User import User
from interfaces.Interface_Company import Company

class Admin_User(User):
    def __init__(self, user_id: int, name: str, password: str, email: str, type: str) -> None:
        super().__init__(user_id, name, password, email, type)
        self.__companies = None
        self.__usuarios = None
        self.__funcionarios = None
        self.__devices = None
        self.__gateways = None
        self.__cages = None

    def carrega_Usuarios(self) -> bool:
        """
        @brief Função que carrega os usuários a partir do arquivo users.csv.
        @return Retorna True se os usuários foram carregados com sucesso, caso contrário retorna False.
        """
        try:
            self.usuarios = pd.read_csv(f'{self.path_dados}\\users.csv')
            return True
        except Exception as e:
            print(f"Erro ao carregar usuários! {e}")
            return False
    
    def carrega_Funcionarios(self) -> bool:
        """
        @brief Função que carrega os funcionários a partir do arquivo employees.csv.
        @return Retorna True se os funcionários foram carregados com sucesso, caso contrário retorna False.
        """
        try:
            self.funcionarios = pd.read_csv(f'{self.path_dados}\\employees.csv')
            return True
        except Exception as e:
            print(f"Erro ao carregar funcionários! {e}")
            return False

    def carrega_Empresas(self) -> bool:
        """
        @brief Função que carrega as empresas a partir do aquivo companies.csv.
        @return Retorna True se as empresas foram carregadas com sucesso, caso contrário retorna False.
        """
        try:
            self.companies = pd.read_csv(f'{self.path_dados}\\companies.csv')
            return True
        except Exception as e:
            print(f"Erro ao carregar empresas! {e}")
            return False
    
    def carrega_Dispositivos(self) -> bool:
        """
        @brief Função que carrega os dispositivos a partir dos arquivos csv.
        @return Retorna True se os dispositivos foram carregados com sucesso, caso contrário retorna False.
        """
        try:
            self.devices = pd.read_csv(f'{self.path_dados}\\devices.csv')
            self.gateways = pd.read_csv(f'{self.path_dados}\\gateways.csv')
            self.cages = pd.read_csv(f'{self.path_dados}\\cages.csv')
            return True
        except Exception as e:
            print(f"Erro ao carregar dispositivos! {e}")
            return False

    def carrega_Dados_Admin(self) -> bool:
        """
        @brief Função que carrega os dados do usuário administrador.
        @return Retorna True se os dados foram carregados com sucesso, caso contrário retorna False.
        """
        if self.carrega_Empresas() == False:
            return False
        if self.carrega_Usuarios() == False:
            return False
        if self.carrega_Funcionarios() == False:
            return False
        if self.carrega_Dispositivos() == False:
            return False
        return True
    
    def listar_Empresas(self) -> bool:
        """
        @brief Função que lista as empresas carregadas nos dados do usuário administrador.
        @return Retorna True se as empresas foram listadas com sucesso, caso contrário retorna False.
        """
        try:
            if self.companies is None:
                print("Nenhuma empresa carregada!")
                print("É necessário carregar as empresas antes de listar!")
                return False
            else:
                print("Empresas cadastradas:")
                self.companies.apply(lambda x: print(f"ID: {x['company_id']} - Nome: {x['name']}"), axis=1)
                return True
        
        except Exception as e:
            print(f"Erro ao listar empresas! {e}")
            return False
    
    def escolher_Empresa(self) -> int:
        """
        @brief Função que permite ao usuário administrador escolher uma empresa.
        @return Retorna o ID da empresa escolhida.
        """
        if self.companies is None:
            print("Nenhuma empresa carregada!")
            print("É necessário carregar as empresas antes de listar!")
        else:
            if self.listar_Empresas():
                print()   
                flag_empresa_invalida = True
                while(flag_empresa_invalida):
                    company_id = input("Digite o ID da empresa que deseja listar: ")
                    if company_id.isnumeric():
                        company_id = int(company_id)
                        if company_id in self.companies['company_id'].values:
                            return company_id
                        else:
                            print("ID da empresa inválido! Digite novamente!")
                    else:
                        print("ID da empresa inválido! Digite novamente!")
            else:
                print("Erro ao listar empresas!")
        return None
        
    def listar_Funcionarios(self, company_id: int) -> bool:
        """
        @brief Função que lista os funcionários de uma empresa.
        @param company_id ID da empresa.
        @return Retorna True se os funcionários foram listados com sucesso, caso contrário retorna False.
        """
        try:
            comapany = self.companies[self.companies['company_id'] == company_id]
            if comapany.empty:
                print("Empresa não encontrada!")
                return False
            class_company = Company(comapany['company_id'].values[0], comapany['name'].values[0], comapany['address'].values[0], comapany['phone'].values[0], comapany['cnpj'].values[0])
            employees = class_company.get_all_employees()

            if not employees.empty:
                print("Funcionários:")
                employees.apply(lambda x: self.print_funcionario_info(x), axis=1)
                return True
            else:
                print("Nenhum funcionário cadastrado!")
                return False
        except Exception as e:
            print(f"Erro ao listar funcionários! {e}")
            return False
    
    def listar_Dispositivos(self, company_id: int) -> bool:
        """
        @brief Função que lista os dispositivos de monitoramento de uma empresa.
        @param company_id ID da empresa.
        @return Retorna True se os dispositivos foram listados com sucesso, caso contrário retorna False.
        """
        try:
            comapany = self.companies[self.companies['company_id'] == company_id]
            if comapany.empty:
                print("Empresa não encontrada!")
                return False
            class_company = Company(comapany['company_id'].values[0], comapany['name'].values[0], comapany['address'].values[0], comapany['phone'].values[0], comapany['cnpj'].values[0])
            class_company.listar_dispositivos()
            return True
        except Exception as e:
            print(f"Erro ao listar dispositivos! {e}")
            return False
    
    def print_funcionario_info(self, x: pd.Series) -> None:
        """
        @brief Função que imprime as informações de um funcionário.
        @param x Funcionário.
        """
        user = self.usuarios[self.usuarios['user_id'] == x['user_id']].iloc[0]
        print(f"ID: {x['employee_id']} - Nome: {user['name']} - Cargo: {x['position']} - Telefone: {x['phone']}")
    
    def cadastrar_Nova_Empresa(self) -> bool:
        """
        @brief Função que cadastra uma nova empresa.
        @return Retorna True se a empresa foi cadastrada com sucesso, caso contrário retorna False.
        """
        try:
            if self.companies is None:
                print("Nenhuma empresa carregada!")
                print("É necessário carregar as empresas antes de cadastrar!")
                return False
            else:
                company_id = self.companies['company_id'].max() + 1
                name = input("Digite o nome da empresa: ")
                name = name.replace(',', ' ')
                address = input("Digite o endereço da empresa: ")
                address = address.replace(',', ' ')
                phone = input("Digite o telefone da empresa: ")
                cnpj = input("Digite o CNPJ da empresa: ")
                new_company = pd.DataFrame([[company_id, name, address, phone, cnpj]], columns=['company_id', 'name', 'address', 'phone', 'cnpj'])
                self.companies = pd.concat([self.companies, new_company], ignore_index=True)
                self.companies.to_csv(f'{self.path_dados}\\companies.csv', index=False)
                print("Empresa cadastrada com sucesso!")
                return True
        except Exception as e:
            print(f"Erro ao cadastrar empresa! {e}")
            return False
    
    def cadastrar_Novo_Funcionario(self, company_id: int) -> bool:
        """
        @brief Função que cadastra um novo funcionário.
        @param company_id ID da empresa.
        @return Retorna True se o funcionário foi cadastrado com sucesso, caso contrário retorna False.
        """
        try:
            company = self.companies[self.companies['company_id'] == company_id]
            if company.empty:
                print("Empresa não encontrada!")
                return False
            else:
                print("Cadastrando novo funcionário!")
                employee_id = self.funcionarios['employee_id'].max() + 1
                user_id = self.usuarios['user_id'].max() + 1
                name = input("Digite o nome do funcionário: ")
                name = name.replace(',', ' ')
                position = input("Digite o cargo do funcionário: ")
                position = position.replace(',', ' ')
                phone = input("Digite o telefone do funcionário: ")
                email = input("Digite o email do funcionário: ")
                flag_email_invalido = True
                while(flag_email_invalido):
                    if email in self.usuarios['email'].values:
                        print("Email já cadastrado! Digite outro email!")
                        email = input("Digite o email do funcionário: ")
                    else:
                        flag_email_invalido = False
                flag_senha_invalida = True
                while(flag_senha_invalida):
                    password = input("Digite a senha do funcionário. Ela não pode conter vírgula: ")
                    if ',' in password:
                        print("Senha inválida! A senha não pode conter vírgula!")
                    else:
                        flag_senha_invalida = False
                flag_senha_novamente = True
                while(flag_senha_novamente):
                    password2 = input("Digite a senha novamente: ")
                    if password != password2:
                        print("Senhas não conferem! Digite novamente!")
                    else:
                        flag_senha_novamente = False
                new_user = pd.DataFrame([[user_id, name, password, email, 'normal']], columns=['user_id', 'name', 'password', 'email', 'type'])
                self.usuarios = pd.concat([self.usuarios, new_user], ignore_index=True)
                new_funcionario = pd.DataFrame([[employee_id, user_id, company_id, position, phone]], columns=['employee_id', 'user_id', 'company_id', 'position', 'phone'])
                self.funcionarios = pd.concat([self.funcionarios, new_funcionario], ignore_index=True)
                self.usuarios.to_csv(f'{self.path_dados}\\users.csv', index=False)
                self.funcionarios.to_csv(f'{self.path_dados}\\employees.csv', index=False)
                print("Funcionário cadastrado com sucesso!")                
                return True
        except Exception as e:
            print(f"Erro ao cadastrar funcionário! {e}")
            return False
        
    def cadastrar_Novo_Dispositivo(self, company_id: int) -> bool:
        """
        @brief Função que cadastra um novo dispositivo de monitoramento.
        @param company_id ID da empresa.
        @return Retorna True se o dispositivo foi cadastrado com sucesso, caso contrário retorna False.
        """
        try:
            company = self.companies[self.companies['company_id'] == company_id]
            if company.empty:
                print("Empresa não encontrada!")
                return False
            else:
                print("Cadastrando novo dispositivo de monitoramento!")
                device_id = self.devices['device_id'].max() + 1
                name = input("Digite o nome do dispositivo: ")
                name = name.replace(',', ' ')
                device_type = input("Digite o modelo do dispositivo (Gateway ou Cage): ")
                flag_type_invalido = True
                while(flag_type_invalido):
                    if device_type.lower() == 'gateway' or device_type.lower() == 'cage':
                        flag_type_invalido = False
                    else:
                        device_type = input("Modelo inválido! Digite novamente (Gateway ou Cage): ")
                status = "Não Instalado"
                battery = 100
                location = None
                mac = input("Digite o MAC do dispositivo: ")
                flag_mac_invalido = True
                while(flag_mac_invalido):
                    if mac in self.devices['mac'].values:
                        print("MAC já cadastrado! Digite outro MAC!")
                        mac = input("Digite o MAC do dispositivo: ")
                    else:
                        flag_mac_invalido = False
                new_device = pd.DataFrame([[device_id, name, device_type, status, battery, location, mac, company_id]], columns=['device_id', 'name', 'type', 'status', 'battery', 'location', 'mac', 'company_id'])
                self.devices = pd.concat([self.devices, new_device], ignore_index=True)
                self.devices.to_csv(f'{self.path_dados}\\devices.csv', index=False)

                if device_type.lower() == 'gateway':
                    gateway_id = self.gateways['gateway_id'].max() + 1
                    sim_card_iccid = input("Digite o ICCID do SIM Card: ")
                    imei = input("Digite o IMEI do dispositivo: ")
                    new_gateway = pd.DataFrame([[gateway_id, device_id, sim_card_iccid, imei]], columns=['gateway_id', 'device_id', 'sim_card_iccid', 'imei'])
                    self.gateways = pd.concat([self.gateways, new_gateway], ignore_index=True)
                    self.gateways.to_csv(f'{self.path_dados}\\gateways.csv', index=False)
                else:
                    cage_id = self.cages['cage_id'].max() + 1
                    new_cage = pd.DataFrame([[cage_id, device_id]], columns=['cage_id', 'device_id'])
                    self.cages = pd.concat([self.cages, new_cage], ignore_index=True)
                    self.cages.to_csv(f'{self.path_dados}\\cages.csv', index=False)

                print("Dispositivo cadastrado com sucesso!")
                return True
        except Exception as e:
            print(f"Erro ao cadastrar dispositivo! {e}")
            return False

    @property
    def companies(self) -> pd.DataFrame:
        return self.__companies
    @companies.setter
    def companies(self, companies: pd.DataFrame) -> None:
        self.__companies = companies

    @property
    def usuarios(self) -> pd.DataFrame:
        return self.__usuarios
    @usuarios.setter
    def usuarios(self, usuarios: pd.DataFrame) -> None:
        self.__usuarios = usuarios

    @property
    def funcionarios(self) -> pd.DataFrame:
        return self.__funcionarios
    @funcionarios.setter
    def funcionarios(self, funcionarios: pd.DataFrame) -> None:
        self.__funcionarios = funcionarios

    @property
    def devices(self) -> pd.DataFrame:
        return self.__devices
    @devices.setter
    def devices(self, devices: pd.DataFrame) -> None:
        self.__devices = devices

    @property
    def gateways(self) -> pd.DataFrame:
        return self.__gateways
    @gateways.setter
    def gateways(self, gateways: pd.DataFrame) -> None:
        self.__gateways = gateways

    @property
    def cages(self) -> pd.DataFrame:
        return self.__cages
    @cages.setter
    def cages(self, cages: pd.DataFrame) -> None:
        self.__cages = cages

