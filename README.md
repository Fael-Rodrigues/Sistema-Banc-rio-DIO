# Sistema-Bancario-DIO
Criar um sistema bancário com as transações : sacar, depositar e visualizar extrato.

Desafio da trilha Python DIO
Objetivo
Criar um sistema bancário com as transações:
•	sacar, depositar e visualizar extrato;
•	criar usuário e criar conta atual.
Desafio
Fomos contratados por um grande banco para desenvolver seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.
Para segunda versão precisamos deixar o código modularizado com funções e introduzir novas funcionalidades: criar usuário do banco e criar conta corrente, que vincula com o usuário.
Operação de depósito
Deve ser possível depositar valores positivos para minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos serão armazenados em uma variável e formas na operação de extrato.
Operação de saque
O sistema deve permitir a realização de 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deverá exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques deverão ser armazenados em uma variável e variações na operação de extrato.
Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser calculado o saldo atual da conta. Se o extrato estiver em branco, exiba a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500,45 = R$ 1500,45
