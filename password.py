from zipfile import ZipFile
with ZipFile('guido_secrets.zip') as zf:
    password = b'BFDL' 
    # the above is equivalent to:
    # password_str = 'BFDL'
    # password = password_str.encode('ascii')
    # because if we have a variable that is a str type, it can be encoded 
    # into a bytes object with the .encode function into ascii
    zf.extractall(pwd=password)
