import unicodedata

def replace_accents_characters(str):
    '''
    Function to replace accented characters with their corresponding non-accented ascii characters
    '''
    return unicodedata.normalize('NFKD', str).encode('ascii', 'ignore').decode('utf-8')
