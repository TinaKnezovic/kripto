
from bitcoinrpc.authproxy import AuthServiceProxy
import PySimpleGUI as sg


def block_stats(client, visina):
    stats = client.getblockstats(client.getblockhash(visina))

    if stats != Exception:
        output = ''

        for key, item in stats.items():
            output += str(key) + ' : ' + str(item).replace(
                '{', '').replace('}', '').replace("'", '').replace(',', ', ').title()+'\n'

        sg.popup(output, title='Info')


def get_block(client, visina):

    info = client.getblock(client.getblockhash(visina))

    if info != Exception:
        output = ''

        for key, item in info.items():
            output += str(key) + ' : ' + str(item).replace(
                '{', '').replace('}', '').replace("'", '').replace(',', ', ').title()+'\n'

        sg.popup(output, title='Info')


def layout():

    layout = [
             
        [sg.Image(r'img.gif'), sg.Text('Unesite visinu bloka'), sg.InputText(key='visina'), sg.Button('Get block'), sg.Button('Get stats')],

    ]
    return layout


def main():

    url = '(pristupnipodaci)'

    # Connect to blockchain.oss.unist.hr
    client = AuthServiceProxy(url)

    # Create GUI window.
    sg.change_look_and_feel('DarkAmber')
    window = sg.Window('Block Info', layout(), size=(800, 50))

    while True:
        event, values = window.read()
        if event in (None,):  # if user closes window
            break

        if event == 'Get block':
            get_block(client, int(values['visina']))

        if event == 'Get stats':
            block_stats(client, int(values['visina']))
    window.close()


if __name__ == '__main__':
    main()
