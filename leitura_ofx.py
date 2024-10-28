import xml.etree.ElementTree as ex
extrato = ex.parse('Extrato.ofx')
raiz = extrato.getroot()
for stmttrn in extrato.findall('.//STMTTRN'):
    fitid = stmttrn.find('FITID').text
    memo = stmttrn.find('MEMO').text
    trnamt = stmttrn.find('TRNAMT').text
    trntype = stmttrn.find('TRNTYPE').text
    dtposted = stmttrn.find('DTPOSTED').text
    print([fitid, memo, trnamt, trntype, dtposted])
#Explicação linha a linha
#Linha 1: Importar biblioteca xml.etree.ElementTree e chamar de ex. A biblioteca importada
# é utilizada na manipulação do XML.
#Linha 2: Criar variável extrato, que recebe a função parse, função que lê  e recebe o 
# arquivo ofx a ser lido entre parênteses
#Linha 3: Criar variável raiz, que recebe a variável extrato com a função getroot, que 
# permite o acesso ao arquivo ofx
#Linha 4: Criar loop for com iteração a cada stmttrn, que é a tag dentro do ofx que descreve
# a transação realizada. A ideia foi iterar sobre todas as tags stmttrn usando a função
# find all, que retorna todas as tags do tipo requerido pelo usuário na inicialização do for
#Linha 5: Criar variável fitid, que recebe o iterável stmttrn e a função find, para localizar
# a informação dentro do stmttrn, o .text retorna uma string. O fitid é o id da transação. 
#Linha 6: Criar variável memo, que recebe o iterável stmttrn e a função find, para localizar
# a informação dentro do stmttrn, o .text retorna uma string. O memo é a informação
#  da transação. 
#Linha 7: Criar variável trnamt, que recebe o iterável stmttrn e a função find, para localizar
# a informação dentro do stmttrn, o .text retorna uma string. O trnamt é a quantidade de 
# dinheiro envolvida na transação.
#Linha 8: Criar variável trntype, que recebe o iterável stmttrn e a função find, para localizar
# a informação dentro do stmttrn, o .text retorna uma string. O trntype é o tipo de transação.
#Linha 9: Criar variável trntype, que recebe o iterável stmttrn e a função find, para localizar
# a informação dentro do stmttrn, o .text retorna uma string. O dtposted é a data da transação.
#Linha 10: Imprimir em formato de lista o fit id, o memo, o trntmat, o trntype e o dtposted. A]
# lista foi o formato encontrado para condensar as informações sobre cada transação