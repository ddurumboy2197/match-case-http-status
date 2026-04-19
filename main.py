def http_status_code(status_code):
    match status_code:
        case 200:
            return "OK"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"

# Test qilish
print(http_status_code(200))  # OK
print(http_status_code(400))  # Bad Request
print(http_status_code(401))  # Unauthorized
print(http_status_code(403))  # Forbidden
print(http_status_code(404))  # Not Found
print(http_status_code(500))  # Internal Server Error
print(http_status_code(999))  # Unknown Status Code
