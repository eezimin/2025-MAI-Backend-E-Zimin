def app(environ, start_response):
    # Бизнес-логика
    data = b"Hello, world!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])