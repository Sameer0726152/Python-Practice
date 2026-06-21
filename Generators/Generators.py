def serve_chai():
    yield "Masala"
    yield "Ginger"
    yield "Elaichi"

stal = serve_chai()
for i in stal:
    print(i)

def get_chai():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

chai = get_chai()
print(chai)
print(next(chai))
print(next(chai))