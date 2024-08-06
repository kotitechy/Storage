import pytube

modules = dir(pytube)
print("Modules in Pytube:")
i = 0
for module in modules:
    print(i, " ", module, end='\t')
    i+=1

