def review_code(code: str) -> str:
    if code[:5] == '```py':
        code = code[5:-3]

    if code[:3] == '```':
        code = code[3:-3]

    return code


SECRET_PASSCODE = 'Всем привет из яндекса!'
