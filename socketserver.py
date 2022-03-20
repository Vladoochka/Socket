import json
import socket


def json_file(url):
    with open('views'+'/' + f'{url}' + '.json', 'r') as file:
        response = file.read()
        return json.loads(response)


URLS = {
    '/api/users?page=2': json_file('page=2'),
    '/api/users?delay=3': json_file('delay=3'),
    '/api/users/2': json_file('user_2'),
    '/api/unknown': json_file('unknown'),
    '/api/unknown/2': json_file('unknown_2'),
}


def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)


def generate_headers(method, url):
    if method == 'POST':
        if 'login' in url:
            if 'password' in url:
                return ('HTTP/1.1 200 OK\n\n', 200)
            else:
                return ('HTTP/1.1 400 Bad Request\n\n', 400)
        elif 'register' in url:
            if 'password' in url:
                return ('HTTP/1.1 200 OK\n\n', 200)
            else:
                return ('HTTP/1.1 400 Bad Request\n\n', 400)
        else:
            return ('HTTP/1.1 201 OK\n\n', 201)
    if method == 'GET':
        if not url in URLS:
            return ('HTTP/1.1 404 Not found\n\n', 404)
        else:
            return ('HTTP/1.1 200 OK\n\n', 200)
    if method == 'PUT':
        return ('HTTP/1.1 200 OK\n\n', 200)
    if method == 'PATCH':
        return ('HTTP/1.1 200 OK\n\n', 200)
    if method == 'DELETE':
        return ('HTTP/1.1 204 No Content\n\n', 204)


def generate_content(code, url, method):
    if code == 404:
        return '{}'
    if code == 400:
        return '{"error": "Missing password"}'
    if code == 204:
        return ' '
    if code == 200:
        if method == 'GET':
            return '{}'.format(URLS[url])
        else:
            return url
    if code == 201:
        return url


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url, method)

    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request)
        print()
        print(addr)

        response = generate_response(request.decode('utf-8'))

        client_socket.sendall(response)
        client_socket.close()


if __name__ == "__main__":
    run()
