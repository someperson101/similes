import random
import time

def sbx(stx, lst):
    if sbj is stx:
        global adj
        adj = random.choice(lst)

def obx(otx, lst):
    if adj is otx:
        global obj
        obj = random.choice(lst)

sbjs = ['Men', 'Women', 'Cats', 'Dogs', 'Humans']
man = ['athletic', 'unintelligent']
wmn = ['intelligent', 'unathletic']
cat = ['unintelligent', 'lazy']
dog = ['intelligent', 'playful']
hmn = ['athletic', 'intelligent']
ath = ['Olympic champion', 'Russian']
unt = ['doorknob', 'idiot']

while True:
    sbj = random.choice(sbjs)
    sbx('Men', man)
    sbx('Women', wmn)
    sbx('Cats', cat)
    sbx('Dogs', dog)
    sbx('Humans', hmn)
    obx('athletic', ath)
    obx('unintelligent', unt)
    print(sbj + ' are as ' + adj + ' as a ' + obj + '.')
    time.sleep(0.5)
