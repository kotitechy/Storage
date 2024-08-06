def encrpt(text):
    pln_txt = list(text)
    en_txt = []
    print('plain text :',text)
    for i in pln_txt:
        if i == 'a':
            en_txt.append('!@#$%^422')
        elif i == 'b':
            en_txt.append('*)&^%^54')
        elif i == 'c':
            en_txt.append('&^*65')
        elif i == 'd':
            en_txt.append('*&^&544654^')
        elif i == 'e':
            en_txt.append('^#^#^^(*&5746)')
        elif i == 'f':
            en_txt.append('54545454&^%&)*')
        elif i == 'g':
            en_txt.append('@#$dore')
        elif i == 'h':
            en_txt.append('&^*77477^&*')
        elif i == 'i':
            en_txt.append('*&^&^877^&jffuyjh')
        elif i == 'j':
            en_txt.append('^few#^#^^(*&6)')
        elif i == 'k':
            en_txt.append(';;::ewfrghln:;;--')
        elif i == 'l':
            en_txt.append('@#ewfdy$')
        elif i == 'm':
            en_txt.append('&^*ewktuf')
        elif i == 'n':
            en_txt.append('&^*ewktufl32fj')
        elif i == 'o':
            en_txt.append('*&^&ewkfgh^')
        elif i == 'p':
            en_txt.append('^#^#^^(*&6jgwqedfa5445)')
        elif i == 'q':
            en_txt.append(';;:::;;&^%^@)*)!**@!(--')
        elif i == 'r':
            en_txt.append('&^%^()*)(*&()mwfhwekl@#$')
        elif i == 's':
            en_txt.append('&^*/wejfjwlej983298')
        elif i == 't':
            en_txt.append('*&^&^kejwfk2189e23&*8*')
        elif i == 'u':
            en_txt.append('^#^#^^(*&3298dhiuiua6)')
        elif i == 'v':
            en_txt.append(';;54545dgjsjh%^%*:::;;--')
        elif i == 'w':
            en_txt.append('@#gowkns&^($')
        elif i == 'x':
            en_txt.append('&^_)__)(_(__(ejhkhdkwehqk*')
        elif i == 'y':
            en_txt.append('*&^&^wejkhfdi()*&098&&544')
        elif i == 'z':
            en_txt.append('^#^#^^(*&6)')
        elif i == " ":
            en_txt.append('858578')
        
        
    print('encrpted text :',en_txt)
    decrypt(en_txt)
def decrypt(text):
    txt = list(text)
    dct_txt = []
    for i in txt:
        if i == '!@#$%^422':
            dct_txt.append('a')
        elif i == '*)&^%^54':
            dct_txt.append('b')
        elif i == '&^*65':
            dct_txt.append('c')
        elif i == '*&^&544654^':
            dct_txt.append('d')
        elif i == '^#^#^^(*&5746)':
            dct_txt.append('e')
        elif i == '54545454&^%&)*':
            dct_txt.append('f')
        elif i == '@#$dore':
            dct_txt.append('g')
        elif i == '&^*77477^&*':
            dct_txt.append('h')
        elif i == '*&^&^877^&jffuyjh':
            dct_txt.append('i')
        elif i == '^few#^#^^(*&6)':
            dct_txt.append('j')
        elif i == ';;::ewfrghln:;;--':
            dct_txt.append('k')
        elif i == '@#ewfdy$':
            dct_txt.append('l')
        elif i == '&^*ewktuf':
            dct_txt.append('m') 
        elif i == '&^*ewktufl32fj':
            dct_txt.append('n') 
        elif i == '*&^&ewkfgh^':
            dct_txt.append('o')
        elif i == '^#^#^^(*&6jgwqedfa5445)':
            dct_txt.append('p')
        elif i == ';;:::;;&^%^@)*)!**@!(--':
            dct_txt.append('q')
        elif i == '&^%^()*)(*&()mwfhwekl@#$':
            dct_txt.append('r')
        elif i == '&^*/wejfjwlej983298':
            dct_txt.append('s')
        elif i == '*&^&^kejwfk2189e23&*8*':
            dct_txt.append('t')
        elif i == '^#^#^^(*&3298dhiuiua6)':
            dct_txt.append('u')
        elif i == ';;54545dgjsjh%^%*:::;;--':
            dct_txt.append('v')
        elif i == '@#gowkns&^($':
            dct_txt.append('w')
        elif i == '&^_)__)(_(__(ejhkhdkwehqk*':
            dct_txt.append('x')
        elif i == '*&^&^wejkhfdi()*&098&&544':
            dct_txt.append('y')
        elif i == '^#^#^^(*&6)':
            dct_txt.append('z')
        elif i == '858578':
            dct_txt.append(" ")
    print("decrypted Text : ","".join(dct_txt))

def send_msg():
    txt = input('Enter Your text Message: ')
    encrpt(txt)
send_msg()