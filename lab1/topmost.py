import wordfreq 
import sys
import urllib.request

                # Importerar modulerna som är nödvändiga

def main():
    try:        # Om den inte hittar en fil ska den skriva ut till användaren att filen inte existerar.

        with open(sys.argv[1], encoding="utf-8") as stopwords:                      # Öppnar andra argumentet som variabeln "stopwords"
            try:                                                                    # Om det är en URL kommer denna få error och går istället igenom den koden som tar emot URL
                with open(sys.argv[2], encoding="utf-8") as inp_file:               # Öppna argument 3 som "inp_file"
                    splitWords = stopwords.read()                                   # Läser igenom stopwords som en string
                    stopwordsList = splitWords.split("\n")                          # Gör stopwords string till en lista 
                    topNumber = int(sys.argv[3])                                    # Topnumber blir fjärde argumentet
                    tokenize = (wordfreq.tokenize(inp_file))                        # Tar ur funktionen tokenize från wordfreq med inp_file som parameter 
                    countWords = (wordfreq.countWords(tokenize,stopwordsList))      # Tar funktionen countWords och använder tokenize och stopwordsList som parametrar
                    printTopMost = (wordfreq.printTopMost(countWords,topNumber))    # Tar funktionen printTopMost och använder countWords and topNumber som parametrar 
                    print(printTopMost)                                             # Printar ut resultatet
            except:
                response = urllib.request.urlopen(sys.argv[2])                      # Använder urllib.request som öppnar URLs 
                lines = response.read().decode("utf8").splitlines()                 # Går igenom texten
                splitWords = stopwords.read()
                stopwordsList = splitWords.split("\n")
                topNumber = int(sys.argv[3])
                tokenize = (wordfreq.tokenize(lines))
                countWords = (wordfreq.countWords(tokenize,stopwordsList))
                printTopMost = (wordfreq.printTopMost(countWords,topNumber))
                print(printTopMost)
    except:
        print("Input file does not exist")                                          # Om fil inte finns printas det ut istället för att få tillbaka error

main()                                                                              # Kallar funktionen
