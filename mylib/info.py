# -*- coding: UTF-8 -*-


from PyPDF2 import PdfFileReader

def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        pagenum = pdf.getNumPages()
    '''
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title
    '''
    information = {'author':info.author,'creator':info.creator,
                   'producer':info.producer,'subject':info.subject,
                   'title':info.title,'pagenum':pagenum}
    return information
