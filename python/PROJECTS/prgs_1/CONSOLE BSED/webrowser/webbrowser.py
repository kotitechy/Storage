from googlesearch import search
import webbrowser

query = input("Enter Here to Search : ")


for url in search(query):
    print(url)
    webbrowser.open(url)