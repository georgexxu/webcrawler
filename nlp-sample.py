from pycorenlp import StanfordCoreNLP
import goslate
gs = goslate.Goslate()
nlp = StanfordCoreNLP('http://localhost:9000')
result=gs.translate('this good', 'en')
res = nlp.annotate(result,
                   properties={
                       'annotators': 'sentiment',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })
for s in res["sentences"]:
    print ("%d: '%s': %s %s" % (
        s["index"],
        " ".join([t["word"] for t in s["tokens"]]),
        s["sentimentValue"], s["sentiment"]))