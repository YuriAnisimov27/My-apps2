def one_login_logic(login_genetator, password_generator, query):
    login, next_login_state = login_genetator(None)
    password, next_password_state = password_generator(None)

    while next_password_state is not None:
        result = query(login, password)
        if result:
            print('SUCCESS', login, password)
            break
        password, next_password_state = password_generator(next_password_state)
