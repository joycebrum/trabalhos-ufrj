def print_default_message(msg):
    print('\n----------------------------------------------------------------')
    print(msg)
    print('----------------------------------------------------------------\n')

def start_application():
    msg = 'Para encerrar digite \'exit\'\n'
    msg += 'Bem vindo, digite o seu nome de usuário'
    print_default_message(msg)
          
def cannot_receive_msg():
    print_default_message('Este usuário não está mais disponível para receber mensagens')
    
def user_not_found():
    print_default_message('Não foi possível encontrar este usuário no sistema.')

def user_data(user):
    print_default_message(user[0] + ': ('+ str(user[1]) + ', ' + str(user[2]) + ')')

def users(users):
    msg = '                            Usuários                              \n'
    if users and len(users) > 0:
        for user in users:
            msg += (user[0] + ': ('+ str(user[1]) + ', ' + str(user[2]) + ')\n')
        
    else:
        msg += 'Não há usuários ativos\n'
    print_default_message(msg)

def message(user, msg):
    print(user +':', msg)

def invalid_username():
    print_default_message('Nome de usuário inválido. O nome de usuário deve conter apenas letras e números')

def welcome(username):
    print_default_message('Nome de usuário cadastrado com sucesso. Bem vindo(a) ' + username)

def username_in_use():
    print_default_message('Nome de usuário já em uso. Escolha outro.')
