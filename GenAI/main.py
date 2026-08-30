import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hii! My name is Sameer"
tokens = enc.encode(text)
print("Tokens :", tokens )
encoded = [25216, 3274, 0, 3673, 1308, 382, 174803]
return_text = enc.decode(encoded)
print("Text :", return_text)