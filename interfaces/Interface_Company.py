import pandas as pd

from interfaces.Interface_Area import Area

class Company ():
    def __init__(self, company_id: int, name: str, address: str, phone: str, cnpj: str) -> None:
        self.company_id = company_id
        self.name = name
        self.address = address
        self.phone = phone
        self.cnpj = cnpj
        self.path_dados = r'.\terminal_app\data'

    def get_all_employees(self) -> pd.DataFrame:
        """
        @brief Função que retorna todos os funcionários da empresa.
        @return Retorna um dataframe com todos os funcionários da empresa.
        """
        try:
            all_employees = pd.read_csv(f'{self.path_dados}\\employees.csv')
            return all_employees[all_employees['company_id'] == self.company_id]
        except Exception as e:
            print(f"Erro ao carregar funcionários da empresa! {e}")
            return None
        
    
    def get_all_devices(self) -> pd.DataFrame:
        """
        @brief Função que retorna todos os dispositivos da empresa.
        @return Retorna um dataframe com todos os dispositivos da empresa.
        """
        try:
            all_devices = pd.read_csv(f'{self.path_dados}\\devices.csv')
            return all_devices[all_devices['company_id'] == self.company_id]
        except Exception as e:
            print(f"Erro ao carregar dispositivos da empresa! {e}")
            return None
        
    
    def get_all_areas(self) -> pd.DataFrame:
        """
        @brief Função que retorna todas as áreas da empresa.
        @return Retorna um dataframe com todas as áreas da empresa.
        """
        try:
            all_areas = pd.read_csv(f'{self.path_dados}\\areas.csv')
            return all_areas[all_areas['company_id'] == self.company_id]
        except Exception as e:
            print(f"Erro ao carregar áreas da empresa! {e}")
            return None
        
    def listar_info_empresa(self) -> None:
        """
        @brief Função que lista as informações da empresa.
        """
        print(f"ID: {self.company_id}")
        print(f"Nome: {self.name}")
        print(f"Endereço: {self.address}")
        print(f"Telefone: {self.phone}")
        print(f"CNPJ: {self.cnpj}")
        print()
    
    def listar_dispositivos(self) -> bool:
        """
        @brief Função que lista os dispositivos da empresa.
        """
        devices = self.get_all_devices()
        if not devices.empty:
            print("Dispositivos:")
            devices.apply(lambda x: print(f"ID: {x['device_id']} - Nome: {x['name']} - Tipo: {x['type']} - Status: {x['status']} - Bateria: {x['battery']} - Localização: {x['location']} - MAC: {x['mac']}"), axis=1)
            return True
        else:
            print("Nenhum dispositivo cadastrado!")
            return False
    
    def exibir_Resumo(self) -> None:
        funcionarios = self.get_all_employees()
        dispositivos = self.get_all_devices()
        areas = self.get_all_areas()

        if funcionarios is None or dispositivos is None or areas is None:
            print("Erro ao carregar os dados da empresa!")
            return
        
        qtd_funcionarios = len(funcionarios)
        print(f"Quantidade de funcionários: {qtd_funcionarios}")
        print()

        qtd_total_dispositivos = len(dispositivos)
        print(f"Quantidade total de dispositivos cadastrados: {qtd_total_dispositivos}")
        if qtd_total_dispositivos == 0:
            print()
        else:
            qtd_dispositivos_instalados = len(dispositivos[dispositivos['status'] == 'Instalado'])
            qtd_dispositivos_nao_instalados = len(dispositivos[dispositivos['status'] == 'Não Instalado'])
            print(f"Quantidade de dispositivos Instalados / Não Instalados: {qtd_dispositivos_instalados}/{qtd_dispositivos_nao_instalados}")
            qtd_gateways = len(dispositivos[dispositivos['type'] == 'Gateway'])
            qtd_cages = len(dispositivos[dispositivos['type'] == 'Cage'])
            print(f"Quantidade de Gateways / Cages: {qtd_gateways}/{qtd_cages}")
            print()        

        qtd_areas = len(areas)
        print(f"Quantidade de áreas cadastradas: {qtd_areas}")
        if qtd_areas > 0:
            qtd_areas_nao_monitoradas = len(areas[areas['status'] == 'Não Monitorada'])
            qtd_areas_em_monitoramento = len(areas[areas['status'] == 'Em Monitoramento'])
            print(f"Quantidade de áreas Não Monitoradas / Em Monitoramento: {qtd_areas_nao_monitoradas}/{qtd_areas_em_monitoramento}")
    
    def escolher_Area(self) -> int:
        """
        @brief Função que exibe as áreas da empresa e permite o usuário escolher uma.
        @return Retorna o ID da área escolhida.
        """
        areas = self.get_all_areas()
        if not areas.empty:
            print("Áreas:")
            areas.apply(lambda x: print(f"ID: {x['area_id']} - Nome: {x['name']} - Status: {x['status']}"), axis=1)
            print()
            flag_area_invalida = True
            while(flag_area_invalida):
                area_id = input("Digite o ID da área desejada: ")
                if area_id.isnumeric():
                    area_id = int(area_id)
                    if area_id in areas['area_id'].values:
                        flag_area_invalida = False
                        return area_id
                    else:
                        print("ID de área inválido! Digite novamente!")
                else:
                    print("ID de área inválido! Digite novamente!")
        else:
            print("Nenhuma área cadastrada!")
            return None
    
    def exibir_Area(self, area_id: int) -> None:
        """
        @brief Função que exibe as informações de uma área.
        @param area_id ID da área a ser exibida.
        """
        areas = self.get_all_areas()
        area = areas[areas['area_id'] == area_id]
        if not area.empty:
            # area_id,name,location,size,company_id,status
            area = area.iloc[0]
            area_obj = Area(area['area_id'], area['name'], area['location'], area['size'], area['company_id'])
            area_obj.exibir_Area()
        else:
            print("Área não encontrada!")
            
            


        
        
        