import sys, getopt
import pandas as pd
import json
from datetime import datetime

def readFileJson(fileName):
    # Como obter o json dos logs: https://botflo.com/how-to-download-dialogflow-es-conversation-logs/

    f = open(fileName, encoding='utf-8')
    data = json.load(f)
    return data

def processJson(data):

    # Criar um dataframe vazio para receber todas as iterações
    df = pd.DataFrame(columns = ['sessionId', 'startTime', 'endTime', 'duration', 'userQuery', 'response', 'intent', 'responseTime'])

    # recolha da informação do JSON

    startTime=""      #inicio do diálogo (um diálogo pode ter várias iterações entre o user e o bot)
    endTime=""        #fim do diálogo
    duration=""       #duração (endTime - startTime) em segundos 
    userQuery=""      #entrada, pode ser a welcome ou dada pelo user
    response=""       #resposta do bot
    intent=""         #intent usada para a resposta
    responseTime = "" #altura em que foi dada a resposta
    sessionId = ""    #único dentro de um diálogo

    for dialogos in data['sessionConversations']:
        startTime=datetime.strptime(dialogos['startTime'][0:19], '%Y-%m-%dT%H:%M:%S')
        endTime=datetime.strptime(dialogos['endTime'][0:19], '%Y-%m-%dT%H:%M:%S')
        duration_segundos = (endTime-startTime).seconds
        for interacoes in dialogos['interactions']:
            userQuery = interacoes['v2Response']['queryResult']['queryText'].replace(chr(13), '').replace(chr(10), '').replace(';', '').replace('"', '')
            try:
                response = interacoes['v2Response']['queryResult']['fulfillmentText'].replace(chr(13), '').replace(chr(10), '').replace(';', '').replace('"', '')
            except:
                for text, payload in interacoes['v2Response']['queryResult']['fulfillmentMessages'][1].items():
                    response = str(payload['richContent']).replace(chr(13), '').replace(chr(10), '').replace(';', '').replace('"', '') #.replace(chr(13), '').replace(chr(10), '').replace(';', '') #interacoes['v2Response']['queryResult']['fulfillmentMessages'].replace(chr(13), '').replace(chr(10), '').replace(';', '')
                    break
            intent = interacoes['v2Response']['queryResult']['intent']['displayName'].replace(chr(10), '').replace(';', '').replace('"', '')
            responseTime = datetime.strptime(interacoes['responseTime'][0:19], '%Y-%m-%dT%H:%M:%S')
            sessionId = interacoes['conversationResponseJson']
            sessionId = sessionId[sessionId.find("sessionId")+13:sessionId.find("timestamp")-6]

            df = df.append({'sessionId': sessionId, 
                    'startTime': startTime, 
                    'endTime': endTime, 
                    'duration': duration_segundos, 
                    'userQuery': userQuery, 
                    'response': response, 
                    'intent': intent, 
                    'responseTime': responseTime}, ignore_index = True)
    return df

def saveFileCSV(df, fileName):
    #gravar para CSV o resultado (pode ter que alterar a path)
    df.to_csv(fileName, index=False, encoding='utf_8_sig') #utf-8





def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('curadoria.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('curadoria.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print ('Input file:', inputfile)
    print ('Output file:', outputfile)

    data = readFileJson(inputfile)
    df = processJson(data)
    saveFileCSV(df, outputfile)
    print('Processo terminado')

if __name__ == "__main__":
   main(sys.argv[1:])



'''
Como extrair logs do DialogFlow para CSV

Vida pessoal!

Acredito que muitos de vocês tenham a necessidade de criar métricas dos vossos projetos
'''