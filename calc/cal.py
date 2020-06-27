from cgi import parse_qs
from template import html 

def application(environ, start_response):
    c = parse_qs(environ['QUERY_STRING'])
    a = c.get('a', [''])[0]
    b = c.get('b', [''])[0]
    sum = 0
    mul = 0
    if '' in [a, b]:
       sum, mul = 0, 0
    if '' not in [a, b]:
       a, b = int(a), int(b)
       sum = a + b
       mul = a * b
    response_body = html % {
              'sum' : sum,
              'mul' : mul
    }
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body] 

