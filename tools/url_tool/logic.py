from urllib.parse import quote_plus, unquote_plus

def encode_url(url: str) -> str:
    return quote_plus(url, safe='')  # Encode everything

def decode_url(url: str) -> str:
    return unquote_plus(url)
