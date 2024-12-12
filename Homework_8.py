import re
def replace_time(text):
 return re.sub(r'\d{2}:\d{2}(:\d{2})?', '(TBD)', text)
text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
result = replace_time(text)
print(result)


import re
def find_abbreviations(text):
 abbreviations = re.findall(r'\b[A-Z]{2,}\b', text)
 return abbreviations
text = "ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п."
abbreviations = find_abbreviations(text)
print(abbreviations)
import re
s='Владимир устроился на работу в одно очень важное место. И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п. '
x=re.findall(r'\b[А-ЯЁ][А-ЯЁ ]*[А-ЯЁ]\b',s)
print(x)