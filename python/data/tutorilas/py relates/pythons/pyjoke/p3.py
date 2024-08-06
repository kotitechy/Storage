import pyttsx3

# Get a list of available engines
engines = pyttsx3.init().drivers

print("Available modules in pyttsx3:")
for engine in engines:
    print(engine.name)
