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

    
    