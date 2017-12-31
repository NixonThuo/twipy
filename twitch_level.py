# pip install python-twitch-client
from twitch import TwitchClient
import datetime
import threading


offlineSeconds = 0


def checkActivetUsers():
    global offlineSeconds
    twitchthread = threading.Timer(
        5.0, checkActivetUsers)
    if(offlineSeconds <= 600):
        twitchthread.start()
    else:
        twitchthread.cancel()
    timenow = datetime.datetime.now()
    f = open('twitch_active_viewers.txt', 'a+')
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
    if isinstance(stream, dict):
        offlineSeconds = 0
        print('%s: %s' % (stream[u'game'], stream[u'viewers']))
        f.write('\n Game -' + stream[u'game'] +
                ': viewers - ' + str(stream[u'viewers']) + '\n\n')
    else:
        offlineSeconds = offlineSeconds + 5
        print 'Channel Currently Offline'
        f.write('Channel Currently Offline \n\n')
    f.close()


checkActivetUsers()
