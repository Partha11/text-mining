def tokenize(text):
    """
    Splits sentence by whitespace and removes punctuation
    """
    words = text.lower().split()
    words = [word.strip('.,!?()[]{}":;') for word in words]

    return [word for word in words if word]