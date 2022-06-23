# Curadoria Dialog Flow
 
## Descrição

Este projeto mostra, passo a passo, como extrair dados dos logs do Dialog Flow para um CSV.

Mas deve estar a perguntar, não dá para validar os log no próprio Dialog Flow? Claro que dá, mas fica muito limitado nas análises que pode fazer.<br>
Em primeiro lugar os logs ficam disponíveis por 30 dias. Caso queira por mais tempo, é possível mas terá custos. Por outro lado, se quiser fazer análises macro ou ver tendências, não terá como fazer pela tool. 

Este projeto está dividido em duas partes:<br>
1. Exportar os dados do DF para um ficheiro JSON<br>
2. Ler o ficheiro e recolher alguns dos dados para ficheiro CSV<br>

## Ferramentas usadas

A lista de ferramentas usadas neste projeto são otodas open source. Este foi um ponto assente na minha escolha.

* <b>Github</b> e <b>Github Desktop</b>: para gestão do código [github](https://github.com/)<br>
* <b>Visual Studio IDE</b>: uma ferramenta da Microsoft que ajuda muito na construção do código. [Visual Studio](https://visualstudio.microsoft.com/)<br>
* <b>Dialogflow Essencial</b>: para testar a chamada da API em ambiente chatbot [Dialog Flow](https://dialogflow.cloud.google.com/#/)<br>
* <b>Python</b>: linguagem de programação usada [Python](https://www.python.org/)<br>

## Pressupostos

Vou partir do princípio que já terá instalado no seu computador o GitHub Desktop, o Visual Studio IDE e o Python e que tenha já alguma familiaridade com todas as ferramentas apresentadas anteriormente.<br>

O Dialog Flow Essencial e o Github, apesar de serem free, necessitam de criar conta. Recomendo sempre que possível que utilizem uma verificação dupla no seu login como boa prática em todas as ferramentas web (O Github permite este tipo de segurança).<br>

## Recolher logs do Dialog Flow

Ao entrar no Dialog Flow, deverá escolher o agente pretendido, e no menu "History" não esquecer de colocar o período pretendido.<br>
Este processo está muito bem detalhado no seguinte link [https://botflo.com/how-to-download-dialogflow-es-conversation-logs](https://botflo.com/how-to-download-dialogflow-es-conversation-logs), por isso não o vou desenvolver aqui.<br>

## Tratar dos logs para CSV

Neste etapa recomendo que crie uma pasta de projeto no seu PC (a path e nome do ficheiro json não deverá ter espaços, ou vai ter problemas durante o processo).<br>

Deverá copiar o seu ficheiro JSON recolhido na etapa anterior para a pasta que criou, assim como o ficheiro curadoria.py que pode descarregar deste git. <br>

Deverá abrir uma linha de comando/terminal (no caso do windows é digitar CMD botão Start do Windows). Ir para a pasta criada (cd /sua_path/).<br>

Para executar esta o código de tratamento do log, basta executar o comando:<br>

> python curadiria.py -i <inputfile> -o <outputfile>

onde <inputfile> deverá ser substituído pelo nome do ficheiro JSON e <outputfile> pelo nome do ficheiro CSV <br>

No final e caso tudo tenha corrido bem, irá encontrar o seu ficheiro CSV na pasta de projeto.<br>

É possível que ao executar o projeto tenha algum erro por falta de bibliotecas. Se isso acontecer deverá instalar a ou as bibliotecas em falta com o comando no terminal:<br>

> pip install nome_da_biblioteca

No ficheiro de excel terá os seguintes campos:
* startTime: inicio do diálogo (um diálogo pode ter várias iterações entre o user e o bot)
* endTime: fim do diálogo
* duration: duração (endTime - startTime) em segundos 
* userQuery: entrada, pode ser a welcome ou dada pelo user
* response: resposta do bot
* intent: intent usada para a resposta
* responseTime: altura em que foi dada a resposta
* sessionId: id único dentro de um diálogo
    
O código é muito simples e está bem comentado. 


