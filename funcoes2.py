def loginUsuario(perfil):
    if str.lower(perfil) == "admin" :
        print("Bem-vindo, Administrador")
    else :
        print("Bem-vindo, Usuário")

loginUsuario("usuario")