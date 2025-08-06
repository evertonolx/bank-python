def show_logo():
    print(r"""
  ____              _    _ 
  |  _ \            | |  | |
  | |_) | __ _ _ __ | | _| |
  |  _ < / _` | '_ \| |/ / |
  | |_) | (_| | | | |   <|_|
  |____/ \__,_|_| |_|_|\_(_)
            """)

CLIENT_FEATURES = {
    "1": lambda: print("Funcionalidade: Consultar Saldo - Em desenvolvimento"),
    "2": lambda: print("Funcionalidade: Fazer Depósito - Em desenvolvimento"),
    "3": lambda: print("Funcionalidade: Fazer Saque - Em desenvolvimento"),
    "4": lambda: print("Funcionalidade: Transferir - Em desenvolvimento"),
    "5": lambda: print("Funcionalidade: Extrato - Em desenvolvimento"),
    "6": lambda: print("Funcionalidade: Relatório da Conta - Em desenvolvimento"),
    "7": lambda: print("Funcionalidade: Consultar Rendimentos - Em desenvolvimento")
}

ADMIN_FEATURES = {
    "1": lambda: print("Funcionalidade: Cadastrar Nova Conta - Em desenvolvimento"),
    "2": lambda: print("Funcionalidade: Bloquear Conta - Em desenvolvimento"),
    "3": lambda: print("Funcionalidade: Desbloquear Conta - Em desenvolvimento"),
    "4": lambda: print("Funcionalidade: Excluir Conta - Em desenvolvimento"),
    "5": lambda: print("Funcionalidade: Editar Conta - Em desenvolvimento"),
}

MENUS = {
    "CLIENT": {
        "title": "MENU CLIENTE",
        "options": [
            "1. Consultar Saldo",
            "2. Fazer Depósito",
            "3. Fazer Saque",
            "4. Transferir",
            "5. Extrato",
            "6. Relatório da Conta",
            "7. Consultar Rendimentos",
            "0. Sair"
        ],
        "features": CLIENT_FEATURES
    },
    "ADMIN": {
        "title": "MENU ADMINISTRADOR",
        "options": [
            "1. Cadastrar Nova Conta",
            "2. Bloquear Conta",
            "3. Desbloquear Conta",
            "4. Excluir Conta",
            "5. Editar Conta",
            "6. Alterar Taxa de Rendimento",
            "0. Sair"
        ],
        "features": ADMIN_FEATURES
    }
}

def authenticate_user():
    # Obter credenciais do arquivo CSV!
    CREDENTIALS = {
        "123": "CLIENT",
        "321": "ADMIN"
    }
    
    print("\n" + "="*35)
    print("         SISTEMA DE ACESSO")
    print("="*35)
    
    password = input("Digite sua senha: ")
    
    profile = CREDENTIALS.get(password)
    
    if profile:
        return profile
    else:
        print("Senha incorreta! Acesso negado.")
        return None

def show_menu(profile):
    menu_config = MENUS[profile]
    
    print("\n" + "="*35)
    print(f"         {menu_config['title']}")
    print("="*35)
    
    for option in menu_config['options']:
        print(option)
    
    print("="*35)

def execute_option(profile, option):
    menu_config = MENUS[profile]
    feature = menu_config['features'].get(option)
    
    if feature:
        feature()
    else:
        print("Opção inválida!")

def main():
    show_logo()
    
    profile = authenticate_user()
    
    if profile is None:
        return
    
    print(f"\nBem-vindo! Você está logado como: {profile}")
    
    while True:
        show_menu(profile)
        option = input("\nEscolha uma opção: ")
        
        if option == "0":
            print("Obrigado por usar o sistema! Até logo!")
            break
        
        execute_option(profile, option)
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()