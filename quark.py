import json
import sys
import random

just_nodes = []
jsoned = {'nodes': [], 'edges': []}

if not sys.argv[1]:
    print ('Usage: helper.py filename')
    quit()

filename = sys.argv[1]
json_file = False

try:
    file = open(filename, 'r')
    lines = file.readlines()
except:
    print('File doesn\'t exist.')
    quit()

def get_rand(occurences):
    sign = random.choice([1, -1])
    unshuffled = list(range(1, 100))
    shuffled = random.sample(unshuffled, 99)
    x, y = random.choice(shuffled), random.choice(unshuffled)
    x = x * sign
    y = random.choice([y, y * -1])
    return x, y

if lines[0][0] == '{':
    json_file = True

if json_file:
    joined_lines = ''.join(lines)
else:
    joined_lines = ','.join(lines)

def generator():
    mod = 0
    for line in lines:
        broke = line.split(',')
        node1 = broke[0]
        node2 = broke[1].strip('\n')
        if node1 not in just_nodes:
            occurences = joined_lines.count(node1)
            rands = get_rand(occurences)
            jsoned['nodes'].append({'label': node1, 'x': rands[0], 'y': rands[1], 'id':node1, 'size':occurences})
            just_nodes.append(node1)
        if node2 not in just_nodes:
            occurences = joined_lines.count(node1)
            rands = get_rand(occurences)
            jsoned['nodes'].append({'label': node2, 'x': rands[0], 'y': rands[1], 'id':node2, 'size':occurences})
            just_nodes.append(node2)
        jsoned['edges'].append({'source':node1,'target':node2,'id':mod,"size":2})
        mod += 3
    return json.dumps(jsoned).replace(' ', '')

if json_file:
    json_dump = joined_lines
else:
    json_dump = generator()

data = 'var rendru = ' + json_dump
savefile = open('%s.js' % filename, 'w+')
savefile.write(data)
savefile.close()

quark = open('quark.html', 'r')
lines = quark.readlines()
lines[6] = '<script id="ourfile" src="%s"></script>\n' % (filename + '.js')
with open('quark.html', 'w+') as quark_save:
    for line in lines:
        quark_save.write(line)

quark.close()
quark_save.close()
quit()