import requests, time, json
import sqlite3


def redundancia0(b):
    try:
        r = requests.get(f'http://pladixoficial.ddns.net/bin.php?bin={b}').text

        r = json.loads(r)

        tipo = r['tipo']
        level = r['nivel']
        banco = r['banco']
        pais = r['pais']
        bandeira = r['bandeira']

        return bandeira, tipo, level, banco, pais

    except: 
        return '', '', '', '', ''


def redundancia3(b):
    try:
        r = requests.get(f'http://pladixoficial.ddns.net/bin.php?bin={b}').text

        r = json.loads(r)

        bandeira = r['bandeira']
        tipo = r['tipo']
        level = r['nivel']
        banco = r['banco']
        pais = r['pais']

        return bandeira, tipo, level, banco, pais
        
    except:
        return '', '', '', '', ''


def redundancia1(b):
    try:
        r = requests.get(f'http://pladixoficial.ddns.net/bin.php?bin={b}').json()
        bandeira = r['bandeira']
        tipo = r['tipo']
        level = r['nivel']
        banco = r['banco']
        pais = r['pais']

        return bandeira, tipo, level, banco, pais
    
    except:
        return '', '', '', '', ''


def redundancia2(b):
    try:
        r = requests.get(f'https://lookup.binlist.net/{b}').json()
        try:
            bandeira = str(r['scheme']).replace('None', '').upper()
        except:
            bandeira = ''
        
        try:
            tipo = str(r['type']).replace('None', '').upper()
        except:
            tipo = ''
        
        try:
            level = str(r['brand']).replace('None', '').upper()
        except:
            level = ''
        
        try:
            banco = str(r['bank']['name']).replace('None', '').upper()
        except:
            banco = ''
        
        try:
            pais = str(r['country']['name']).replace('None', '').upper()
        except:
            pais = ''

        return bandeira, tipo, level, banco, pais
    
    except:
        return '', '', '', '', ''



def redundancia4(b):
    try:
        r = requests.get(f'http://pladixoficial.ddns.net/bin.php?bin={b}').text

        load = json.loads(r)

        banco = load['banco']
        bandeira = load['bandeira']
        level = load['nivel']
        if bandeira == 'HIPERCARD':
            level = 'HIPERCARD'
        if level == '':
            level = 'INDEFINIDO'
        tipo = load['tipo']
        pais = load['pais']
        
        return banco, bandeira, level, tipo, pais

    except:
        return '', '', '', '', ''



def bin_checker(bi):
    bandeira = 'INDEFINIDO'
    tipo = 'INDEFINIDO'
    level = 'INDEFINIDO'
    banco = 'INDEFINIDO'
    pais = 'INDEFINIDO'

    a = redundancia3(bi)

    bandeira = a[0]
    tipo = a[1]
    level = a[2]
    banco = a[3]
    pais = a[4]

    if a[0] == 'AMERICAN EXPRESS':
        level = 'AMERICAN EXPRESS'

    if level == 'INDEFINIDO' or level == '':
        r = redundancia1(bi)
        bandeira = r[0]
        tipo = r[1]
        level = r[2]
        banco = r[3]
        pais = r[4]

        if level == 'INDEFINIDO' or level == '':
            pais = ''
            a = redundancia0(bi)
            pais = a[4]
            bandeira = a[0]
            tipo = a[1]
            level = a[2]
            banco = a[3]

            if level == 'INDEFINIDO' or level == '':
                principal = redundancia2(bi)
                
                level = principal[2]
                bandeira = principal[0]
                banco = principal[3]
                tipo = principal[1]
                pais = principal[4]

    return bandeira, tipo, level, banco, pais

