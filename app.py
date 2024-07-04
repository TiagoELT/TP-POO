from terminal import Terminal_App
import sys

"""
    Função principal que inicializa a aplicação.
"""
def main():
    app = Terminal_App()
    flag_inicializacao, flag_admin = app.inicializa_App()
    if flag_inicializacao == False:
        print("O programa será encerrado.")
        sys.exit(0)

    flag_interacao = True
    while(flag_interacao):
        if flag_admin:
            option = app.opcoes_Usuario_Admin()
            if not app.handle_Opcoes_Admin(option):
                print("O programa será encerrado.")
                sys.exit(0)
        else:
            option = app.opcoes_Usuario_Normal()
            if not app.handle_Opcoes_Normal(option):
                print("O programa será encerrado.")
                sys.exit(0)
        flag_interacao = app.nova_Interacao()

if __name__ == "__main__":
    main()