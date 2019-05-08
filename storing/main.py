import json

student_ids = {'A101','A102','A103'}
games = ('cricket','football','basketball','volleyball','chess')
student_info = {
                'A101':{'name':'Teja','branch':'CSE','year':4},
                'A102':{'name':'Vinay','branch':'Mech','year':4},
                'A103':{'name':'Kanthi','branch':'Civil','year':4},
                'A104':{'name':'Nandan','branch':'BSC','year':3}
                }
sports_subscribed = {
                    'cricket':{'A101','A102','A103'},
                    'basketball':{'A101','A102'},
                    'volleyball':{'A103'}
                }
conv_sports_subscription = {}
# conv_sports_subscription['asdasd'] = "asdasd"
for n in sports_subscribed:
    conv_sports_subscription[n] = list(sports_subscribed[n])
    
# print(conv_sports_subscription)
main_Dictionaries={
    'student_ids': list(student_ids),
    'student_info' : student_info,
    'games' : games,
    'sports_subscribed' : conv_sports_subscription,
}

processedInfo = json.dumps(main_Dictionaries)
print(processedInfo)

def write_to_file(info,filename):
    with open(filename,'w') as myfile:
        json.dump(info,myfile)

write_to_file(main_Dictionaries,'data.txt')
write_to_file(main_Dictionaries,'info.txt')

with open('data.txt') as readfile:
    main = json.load(readfile)

print(main)
main['student_ids'] = set(main['student_ids'])
for n in main['sports_subscribed']:
    main['sports_subscribed'][n] = set(main['sports_subscribed'][n])

print(main)