import pandas as pd
from interfaces import Interface_User
from typing import Type

class Login():
    def __init__(self) -> None:
        self.tentativas_login = 3
        self.__usuarios_df = None
        self.path_usuarios = r'.\terminal_app\data\users.csv'

    
    def fazer_Login(self) -> Type[Interface_User.User]:
        """
        @brief Função que realiza o login do usuário.
        @return Retorna True se o login foi realizado com sucesso, caso contrário retorna False.
        """
        flag_login_invalido = True
        if self.carrega_Usuarios() == False:
            print("Erro com a base de dados de usuários!")
            return None

        while(flag_login_invalido):
            email = input("Digite seu email: ")
            password = input("Digite sua senha: ")
            print()
            user_id = self.verifica_Login(email, password)
            if user_id != None:
                flag_login_invalido = False
                print("Login realizado com sucesso!")
                print()
                usuario = self.get_User_by_Id(user_id)
                return usuario
            else:
                self.tentativas_login -= 1
                if self.tentativas_login == 0:
                    print("Número de tentativas excedido! O programa será encerrado.")
                    return None
                else:
                    print(f"Login inválido! Digite novamente!\n")
        
    def verifica_Login(self, email: str, password: str) -> int:
        """
        @brief Função que verifica se o login é válido.
        @param email Email do usuário.
        @param password Senha do usuário.
        @return Retorna o id do usuário se o login for válido, caso contrário retorna None.
        """
        user = self.usuarios_df[(self.usuarios_df['email'] == email) & (self.usuarios_df['password'] == password)]
        if not user.empty:
            return user['user_id'].iloc[0]
        return None

    @property
    def usuarios_df(self) -> pd.DataFrame:
        return self.__usuarios_df
    @usuarios_df.setter
    def usuarios_df(self, usuarios_df: pd.DataFrame) -> None:
        self.__usuarios_df = usuarios_df
    def carrega_Usuarios(self) -> bool:
        """
        @brief Função que carrega os usuários do arquivo csv.
        @return Retorna True se os usuários foram carregados com sucesso, caso contrário retorna False.
        """
        dataframe_usuarios = pd.read_csv(self.path_usuarios)
        if dataframe_usuarios.empty:
            return False
        self.usuarios_df = dataframe_usuarios

    def get_User_by_Id(self, user_id: int) -> Type[Interface_User.User]:
        user = self.usuarios_df[self.usuarios_df['user_id'] == user_id]
        if not user.empty:
            user = user.iloc[0]
            return Interface_User.User(user['user_id'], user['name'], user['password'], user['email'], user['type'])
        return None
        

    