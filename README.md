#Back End Bandejão
- `https://test3-kndm.onrender.com`
## Banco de Dados da Aplicação

![Banco de Dados da Aplicação](bd/Banco_de_dados.png)

Este site está sendo desenvolvido para otimizar as filas do Refeitório do IFNMG Campus Salinas - MG. Este espaço irá organizar as filas de forma online, visando proporcionar uma melhor qualidade de vida aos estudantes e servidores, resultando em um melhor aproveitamento do tempo de intervalo.

## Lista de usuarios

- **Método:** GET
- **Permissões:** Permite a qualquer usuário acessar.
- **Descrição:** Retorna uma lista de todos os usuários no banco de dados.
- **Endpoint:** `https://test3-kndm.onrender.com/usuarios`

## Criação de usuario

- **Método:** POST
- **Permissões:** Permite a qualquer usuário acessar.
- **Descrição:** Adiciona um novo usuário ao banco de dados com base nos dados fornecidos.
- **Endpoint:** `https://test3-kndm.onrender.com/usuario/`
- **Body:** {
   "Vinculo_Escolar": "vinculo",
   "Tipo_Usuario" : "Seu tipo: Servidor, Aluno do tecnico, Aluno do medio, Visitante"
   "ID": "id",
   "Email": "email",
   "Senha": "senha",
   "Nome": "nome"
}

## Alterações de dados do usuário, consulta de usuário por id e exclusão de usuário

- **Métodos:** GET, PUT, DELETE
- **Permissões:** Permite a qualquer usuário acessar.
- **Descrição:**
- **GET:** Retorna detalhes de um usuário específico com base no ID fornecido.
- **PUT:** Atualiza os dados de um usuário específico com base no ID fornecido.
- **DELETE:** Exclui um usuário específico com base no ID fornecido.
- **Endpoint:** `https://test3-kndm.onrender.com/usuario/<int:user_id>/`
- **Body apenas para as requisições do tipo PUT:**{
   "Vinculo_Escolar": "vinculo",
    "Tipo_Usuario" : "Seu tipo: Servidor, Aluno do tecnico, Aluno do medio, Visitante",
   "Email": "email",
   "Senha": "senha",
   "Nome": "nome"
}

## Lista de usuarios adiminisrativos

- **Método:** GET
- **Permissões:** Permite a qualquer usuário acessar.
- **Descrição:** Retorna uma lista de todos os usuarios adiminisrativos no banco de dados.
- **Endpoint:** `https://test3-kndm.onrender.com/admins`

## Criação de usuario adiminisrativo

- **Método:** POST
- **Permissões:** Permite a qualquer usuário acessar.
- **Descrição:** Adiciona um novo usuario adiminisrativo ao banco de dados com base nos dados fornecidos.
- **Endpoint:** `https://test3-kndm.onrender.com/admin/`
- **Body:** {
   "Vinculo_Escolar": "vinculo",
   "ID": "id",
   "Email": "email",
   "Senha": "senha",
   "Nome": "nome"
}

## Alterações de dados do usuario adiminisrativo, consulta de usuario adiminisrativo por id e exclusão de usuario adiminisrativo

- **Métodos:** GET, PUT, DELETE
- **Permissões:** Permite a qualquer usuário acessar.
- **Descrição:**
- **GET:** Retorna detalhes de um usuario adiminisrativo específico com base no ID fornecido.
- **PUT:** Atualiza os dados de um usuario adiminisrativo específico com base no ID fornecido.
- **DELETE:** Exclui um usuario adiminisrativo específico com base no ID fornecido.
- **Endpoint:** `https://test3-kndm.onrender.com/admin/<int:admin_id>/`
- **Body apenas para as requisições do tipo PUT:**{
   "Vinculo_Escolar": "vinculo",
   "Email": "email",
   "Senha": "senha",
   "Nome": "nome"
}
