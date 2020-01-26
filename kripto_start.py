from bitcoinrpc.authproxy import AuthServiceProxy
import PySimpleGUI as sg

def main():
    sg.theme('DarkAmber')
    
    
    CLIENT_URL= 'http://student:WYVyF5DTERJASAiIiYGg4UkRH@blockchain.oss.unist.hr:8332'
    client=AuthServiceProxy(CLIENT_URL)
    
    def blockchain_info():
        info= client.getblockchaininfo()

        formated_informations = ''
        for key, item in info.items():
            formated_informations += str(key) + ' : ' + str(item).replace('{','').replace('}','').replace("'",'').replace(',',', ').title()+'\n'
    
        sg.popup(formated_informations,title='Informacije o BlockChain-u')

    
    layout_start = [
          [sg.Button('Blockchain Info')],
          [sg.Button('2')], 
          [sg.Button('3')], 
          [sg.Quit()]
          ]
    
    window = sg.Window('YOUR BLOCKCHAIN').Layout(layout_start)
    
    while True:
        event, value = window.read()
        if event in (None, 'Quit'):
            break
        
        elif event == 'Blockchain Info':
            blockchain_info()
    
if __name__=='__main__':
    main()