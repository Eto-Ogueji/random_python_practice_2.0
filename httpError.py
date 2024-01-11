def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 414:
            return "I am a teapot"
        case _:
            return "Something's wrong with the internet"
