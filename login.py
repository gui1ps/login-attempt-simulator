dados={}

while True:
    login=int(input('Deseja realizar login (0) ou criar uma conta(1)?: '))
    if login==0:
        usr=input('Nome do usuário: ')
        password=input('Senha: ')
        for user,data in dados.items():
            if usr==user and password==data[0]:
                print('login válido')
            elif usr==user and password!=data[0]:
                print('Senha incorreta!')
        break
    else:
        if login==1:
            usr=input('Nome do usuário: ')
            password=input('Senha: ')
            email=input('Email: ')
            if usr not in dados:
                dados.update({usr:(password,email)})
            else:
                print('Usuário já existente')
            continue
        else:
            print('Comando inválido!')
            continue
