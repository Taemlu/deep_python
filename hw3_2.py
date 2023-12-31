# В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = '''Мистер и миссис Дурсль проживали в доме номер четыре по Тисовой улице 
и всегда с гордостью заявляли, что они, слава богу, абсолютно нормальные люди. 
Уж от кого-кого, а от них никак нельзя было ожидать, чтобы они попали в какую-нибудь странную или загадочную ситуацию. 
Мистер и миссис Дурсль весьма неодобрительно относились к любым странностям, загадкам и прочей ерунде.
Мистер Дурсль возглавлял фирму под названием "Граннингс", которая специализировалась на производстве дрелей. 
Это был полный мужчина с очень пышными усами и очень короткой шеей. 
Что же касается миссис Дурсль, она была тощей блондинкой с шеей почти вдвое длиннее, чем положено при её росте. 
Однако этот недостаток пришёлся ей весьма кстати, 
поскольку большую часть времени миссис Дурсль следила за соседями и подслушивала их разговоры. 
А с такой шеей, как у неё, было очень удобно заглядывать за чужие заборы. 
У мистера и миссис Дурсль был маленький сын по имени Дадли, и, по их мнению, 
он был самым чудесным ребёнком на свете.
Семья Дурслей имела всё, чего только можно пожелать. Но был у них и один секрет. 
Причём больше всего на свете они боялись, что кто-нибудь о нём узнает. 
Дурсли даже представить себе не могли, что с ними будет, если выплывет правда о Поттерах.
Миссис Поттер приходилась миссис Дурсль родной сестрой, но они не виделись вот уже несколько лет. 
Миссис Дурсль даже делала вид, что у неё вовсе нет никакой сестры, 
потому что сестра и её никчёмный муж были полной противоположностью Дурслям.
'''
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~—"

cleaned_text = ''.join(char for char in text if char not in punctuation)
cleaned_text = cleaned_text.lower()

word_counts = {}
for word in cleaned_text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

top_10_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[
               :10]

for i, item in enumerate(top_10_words, start=1):
    print(f'{i:>2}.', item[0], '-', item[1])