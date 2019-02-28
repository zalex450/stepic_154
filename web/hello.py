def task_1_9(environ, start_response):
    body = ""
    for cur in environ["QUERY_STRING"].split('&'):
        body += cur + '\n'
        
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return body
