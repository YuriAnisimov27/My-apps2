# 1. перебор паролей
# 2. перебор логинов
# 3. запрос (обращение к серверу)
# 4. логика перебора

import logic
import generators
import queries

logic.one_login_logic(
    login_genetator=generators.simple_logins,
    password_generator=generators.popular_passwords,
    query=queries.request_local
)
