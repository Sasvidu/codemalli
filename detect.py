def detect_si_en(text):
    sinhala_chars = 0
    english_chars = 0
    
    for ch in text:
        # Sinhala Unicode range
        if '\u0D80' <= ch <= '\u0DFF':
            sinhala_chars += 1
        # English alphabets (basic Latin)
        elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            english_chars += 1
    
    if sinhala_chars > english_chars:
        return 'si'
    elif english_chars > 0:
        return 'en'
    else:
        return 'unknown'
