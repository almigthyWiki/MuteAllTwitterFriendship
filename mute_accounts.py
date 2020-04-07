from time import sleep
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

twitter_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
twitter_auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(twitter_auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
twitter_api.verify_credentials()
counter = 0
try:
    for user in tweepy.Cursor(twitter_api.friends).items():
        counter += 1
        print("Usuarios Silenciados", counter,"| Silenciando {}".format(user.screen_name))
        twitter_api.create_mute(user.id)
        sleep(6)
    print("Todos los usuarios han sido silenciados")
except KeyboardInterrupt as err:
    print()
    print("Adiós...")
