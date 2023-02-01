print('\33[1;32m•\33[m'*30)
print('\33[1;32mPROCEDIMENTOS SUPORTE PICPAY\33[m')
print('\33[1;32m•\33[m'*30)
print('''\33[1m[1] Bloqueio 26
[2] Bloqueio 27
[3] Bloqueio 42
[4] Bloqueio 21
[5] Fraude
[6] Re-validar CPF
[7] Manipulação\33[m''')
opção = int(input('Qual procedimento deseja verificar? Digite a opção: '))
if opção == 1:
    print('''O bloqueio 26 é um bloqueio de transição, ele indica que o cliente não completou todas as etapas no fluxo de criação de contas.
Quando há um BUG que impede o cliente de seguir com a criação da conta, o Relacionamento encaminha o ticket para análise do time de Suporte Operacional.
\33[1;36mA Prevenção só tem atuação em casos de cadastro criado por terceiros, nesses casos a conta precisa ser arquivada para que o titular do CPF consiga criá-la corretamente.\33[m''')
elif opção == 2:
    print('\33[1;30;46mBLOQUEIO 27\33[m')
    print('''\33[1m[1] Biometria negada
[2] Suspeita de fraude
[3] Validação negada
[4] Vinculo com responsável negado
[5] Documentoscopia negada
[6] Negado menor de idade\33[m''')
    motivo = int(input('Qual o motivo do bloqueio 27? Digite a opção: '))
    if motivo == 1 or motivo == 2:
        print('''PREV - Casos conta falsa
\33[1;30;47mOBS: Casos onde a conta não é falsa não possuem apelação → devolver para N1\33[m''')
    elif motivo == 3:
        print('Prev - arquivamento')
    elif motivo == 5:
        print('HUB DO CARD → Análise N1 → Suporte Operacional\nFluxo padrão → Análise N1 → Suporte Operacional')
    elif motivo ==6:
        print('''\33[1;36mBloqueio 27 + status recusado menor de idade\33[m
Se o cliente não completou 16 anos o bloqueio esta correto, e não há ação a ser aplicada pelo Suporte e Docs, o N1 tem orientação direcionada para esse cliente.

\33[1mMas, se o cliente já completou 16 anos (conferir com a RFB), pode ser uma falha na integração com o bureau, sendo assim:\33[m
•Conferir se o cliente já possui 16 anos;
•Conferir se o nome do CPF no HD retorna dados;
•Revalidar o CPF;
•Arquivar a conta e encerrar o ticket;
•Se não retornarem dados o cliente será orientado pelo N1 sobre a impossibilidade de seguir com a criação da conta.''')
    else:
        print('\33[1;30;46mCRIAÇÃO DE CONTAS POR MENORES\33[m')
        print('''\33[1;36mBloqueio 27 + status vínculo com responsável negado\33[m
O usuário com menos de 18 anos que recebe de forma incorreta o bloqueio 27 com status de vínculo com o responsável negado não foi aprovado na documentoscopia ou na biometria.
Tais casos deverão ser encerrados em N1 quando a recusa for legítima, ou encaminhados do N1 para o Suporte Operacional quando for caso de falso negativo.

\33[1mOs tickets que abordem essas contas podem ser devolvidos como encaminhamento incorreto caso subam para o Suporte ou Docs.\33[m''')
elif opção == 3:
    print('\33[1;30;46mBLOQUEIO 42\33[m')
    print('''O bloqueio 42 é associado a contas de clientes menores de idade que foram recusados em alguma etapa da jornada de criação de contas.''')
    print('''STATUS
[1]Vínculo com o responsável negado
[2]Negado menor de idade
[3]Sem Status''')
    status = int(input('Qual o status da conta: Digite a opção: '))
    if status == 1:
        print('Tratativa docs → SCS para arquivamento se necessário')
        print('Nos casos onde o status da conta é vínculo com o responsável negado a tratativa deve ser dada pelo time de Documentação, e só será enviada para o SCS em caso de arquivamento.''')
        print('\33[1;47mCaso o nome, do responsável, informado em cadastro, seja divergente do nome da documentação, analisamos a documentação e arquivamos a conta\33[m')
    elif status == 2:
        print('''[1] Cliente MAIOR de 16 anos
[2] Cliente MENOR de 16 anos''')
        opção = int(input('Digite a opção desejada: '))
        if opção == 1:
            print('Arquivar a conta')
        elif opção == 2:
            print('Relacionamento orienta o cliente')
    elif status == 3:
        print('contas criadas em meados de junho/ julho de 2022 e o STATUS, NOME E RESPONSAVEL LEGAL estiverem em branco →  arquivar.')
elif opção == 4:
    print('\33[1;30;46m MANIPULAÇÃO POR TERCEIROS \33[m')
    print('''Casos com manipulação por terceiros no cadastro e / ou na documentação, buscaremos evidenciar o vínculo dos envolvidos.
\33[1;36m•Sem vínculo:\33[m Fraude (Bloqueio 11);
\33[1;36m•Com vínculo:\33[m Não Fraude (Bloqueio 21).''')
    print('\33[1;36mInformações que podemos utilizar para tomar nossa decisão\33[m')
    print('''•Ligações para validar infos cadastrais, possíveis vínculos, ciência da utilização da conta e contratações dos produtos;
•CTPS validada em contato;
•Xerox e foto de tela do documento:
•Comportamento suspeito aplicar bloqueio de fraude;
•Conta em conformidade solicitar nova documentação com bloqueio 94;
•Quanto mais antiga as movimentações, mais "confiáveis" as contas (Histórico);
•Cuidado com triangulação (Retirada de valor, autofinanciamento, etc.);
•Devemos utilizar o máximo possível de informação dentro do cadastro que consigam provar a veracidade da criação da conta pelo dono do CPF ou
 por alguém vinculado à ele onde conseguimos responsabilizá-lo desta ação.''')
elif opção == 5:
    print('''\33[1m[1] Fraude Confirmada
[2] Fraude de Cartão
[3] Fraude de Identidade
[4] Auto Fraude\33[m''')
    opção = int(input('Digite a opção que quer verificar: '))
    if opção == 1:
        print('\33[1;30;46mFRAUDE CONFIRMADA\33[m')
        print('''•Casos onde o usuário fez o envio de uma documentação falsa em qualquer um dos canais disponíveis (Casos de invasão e TFA devem ser tratados como tal);
•Casos onde a selfie não é condizente com o documento;
•Casos onde o CPF do documento enviado difere do CPF da conta, independente do vínculo.''')
    elif opção == 2:
        print('\33[1;31;40mFRAUDE DE CARTÃO\33[m')
        print('classificamos como fraude de cartão o pagamento realizado sem autorização do titular - terceiro, sem vínculo - do cartão. Pode ter natureza criminal ou não.')
        print('''•Fluxo de cadastro e horário;
•Compartilhamento;
•Log;
•Quem são os titulares;
•Endereço;
•Histórico de utilização:
•Quantidade de transações aprovadas;
•Quantidade de transações recusadas;
•Quantidade de transações não autorizadas.
•Fluxo de transações;
•Pontos de atenção;
•Validações dos cartões (Necessário reanalisar a documentação).''')
    elif opção == 3:
        print('\33[1;30;46mFRAUDE DE IDENTIDADE\33[m')
        print('''As informações inseridas no cadastro não pertencem ao titular do CPF ou a alguma pessoa próxima vinculada. Além disso, '
os dados estão sendo utilizados indevidamente com o intuito de obter ganhos de maneira fraudulenta sem o consentimento do real titular da conta.''')
        print('''→Dados de Cadastro NÃO remetem ao titular do CPF
Email;
Telefone;
Endereço;
Documentação.''')
        print('''\33[1;30;46mPontos de Atenção\33[m
•Informações de cartões / contas bancárias não vinculam ao titular do CPF;
•Compartilhamentos sem vínculos;
•Dados inexistentes ou aleatórios inseridos;
•Endereços divergentes.''')

    elif opção == 4:
        print('\33[1;31;40mAUTO FRAUDE\33[m')
        print('''Se tratam das situações onde o usuário conscientemente faz a contestação do pagamento, essa é uma classificação interna feita pelo time de intercâmbio,
essa classificação é dada quando o time identifica que não há fraude naquela transação.
É importante nesses casos identificar se há boa-fé ou má-fé quando tivermos cadastros vinculados a essas contas.
Precisamos avaliar contrato de CP, PIX, pagamento P2P com saldo.''')
        print('''CENÁRIOS
[1] Desacordo
[2] Golpe Comercial''')
        cenário = int(input('Digite o número do cenário que deseja verificar: '))
        if cenário == 1:
            print('\33[1;31;46DESACORDO\33[m')
            print('''Quebra de acordo entre pagador e recebedor, sem má fé.
•Avaliar se o desacordo teve uma resolução → Qual foi?
•Existem outros tickets do pagador informando que recebeu o produto?
•Avaliar o histórico de transações do vendedor;
•Contestações de pagamentos na conta do vendedor (CBK’s);
•Informações que estão no ticket;
•Meio em que foi realizada a venda;
•Tipo de produto comercializado;
•Informações de instruções de pagamento / negociação.''')
        elif cenário == 2:
            print('\33[1;31;46GOLPE COMERCIAL\33[m')
            print('''Quebra de acordo entre pagador e recebedor, com má fé.
•Avaliar se o desacordo teve uma resolução → Qual foi?
•Existem outros tickets do pagador informando que recebeu o produto?
•Avaliar o histórico de transações do vendedor;
•Contestações de pagamentos na conta do vendedor (CBK’s);
•Informações que estão no ticket;
•Meio em que foi realizada a venda;
•Tipo de produto comercializado;
•Informações de instruções de pagamento / negociação.''')
elif opção == 6:
    print('\33[1;30;46mRe-validar CPF\33[m')
    print('''[1] Nome do CPF  na aba de cadastro do cliente esta incorreto
[2] Usuário com 16 anos ou mais, bloqueio 27 e status negado menor de idade''')
    opção = int(input('Digite a opção desejada: '))
    if opção == 1:
        print('''•Verificar na aba comentários se não já foi feita a alteração por outro analista;
•Revalidar o CPF;
•Registrar nos comentários a ação e o motivo''')
    elif opção == 2:
        print('\33[1;30;42matenção, para essas três informações, não são todos os bloqueios e/ou status:\33[m')
        print('''\33[1;32m•Verificar se o nome do CPF está preenchido (nome não pode estar em branco)
•Revalidar o CPF;
•Registrar em comentários a tratativa\33[m
Arquivar a conta para o cliente criar de novo''')
elif opção == 7:
    print('\33[1;30;46mMANIPULAÇÃO POR TERCEIROS\33[m')
    print('''Casos com manipulação por terceiros no cadastro e / ou na documentação, buscaremos evidenciar o vínculo dos envolvidos.
•Sem vínculo: Fraude (Bloqueio 11);
•Com vínculo: Não Fraude (Bloqueio 21).''')
    print('''Casos onde conseguimos evidenciar a criação do cadastro pelo dono do CPF ou por alguém vinculado à ele;
Os vínculos podem tentar ser verificados através do Bureau, redes sociais, ligações, etc;
Se existirem faturas verídicas já pagas de algum produto (Pelo menos 2) somado ao contexto de uso da conta;
Em casos onde não tivermos certeza de que a selfie pertence ao usuário, podemos utilizar redes sociais para classificar como Não Fraude.''')
