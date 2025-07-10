from nltk.tokenize import sent_tokenize

def chunk_text(text, max_tokens=300):
    sentences = sent_tokenize(text)
    chunks, chunk = [], ""
    for sentence in sentences:
        if len(chunk.split()) + len(sentence.split()) <= max_tokens:
            chunk += " " + sentence
        else:
            chunks.append(chunk.strip())
            chunk = sentence
    if chunk:
        chunks.append(chunk.strip())
    return chunks
