from bitcoinrpc.authproxy import AuthServiceProxy
import PySimpleGUI as sg

def main():
    CLIENT_URL= 'http://student:WYVyF5DTERJASAiIiYGg4UkRH@blockchain.oss.unist.hr:8332'

    client=AuthServiceProxy(CLIENT_URL)
    info= client.getblockchaininfo()

    formated_informations = ''
    for key, item in info.items():
        formated_informations += str(key) + ' : ' + str(item).replace('{','').replace('}','').replace("'",'').replace(',',', ').title()+'\n'
    
    sg.popup(formated_informations,title='BlockChain Informations')
   
if __name__=='__main__':
    main()