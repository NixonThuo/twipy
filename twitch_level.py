from twitch import TwitchClient
import datetime
import threading


def checkActivetUsers():
    threading.Timer(1.0, checkActivetUsers).start()  # called every second
    timenow = datetime.datetime.now()
    f = open('twitch_active_viewers.txt', 'w')
    print timenow
    f.write(timenow.strftime("%Y-%m-%d %H:%M:%S") + '\n')
    client = TwitchClient('k0tqqij2xwujktxleoxyj8i6fa9jzv')
    user_id = ''
    users = client.users.translate_usernames_to_ids(['treeboydave'])
    for user in users:
        print('%s: %s' % (user.name, user.id))
        f.write(user.name + ':' + user.id + '\n')
        user_id = user.id
    stream = client.streams.get_stream_by_user(user_id)
    print('%s: %s' % (stream[u'game'], stream[u'viewers']))
    f.write(stream[u'game'] + ':' + str(stream[u'viewers']) + '\n')
    f.close()


checkActivetUsers()
