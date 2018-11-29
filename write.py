import config

def Write(config.spreadsheeturl):

        filename = 'data.xlsx'
        r = requests.get(config.spreadsheeturl, stream=True)

        if r.status_code == 200:
                if os.path.isfile('data.xlsx'):
                        os.remove('data.xlsx')

                with open(filename, 'wb') as f:
                        f.write(r.content)
                        return "Spreadsheet Updated"
