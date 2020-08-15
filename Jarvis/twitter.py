def tweet():
    import tweepy
    API_key = 'udpDbEQdg1R3iIzu7WpnV5zKZ'
    API_key_secret = 'SaOEr2H5h9PZR4N7sPhVCqyt27TicxUapIOMCt75POufqHEt9N'
    Access_token ='1278607790995464192-PGe452I5xcWrkGQSMdcNRbLWeJEkzg'
    Access_token_secret = 'Vw3y6DbTiAGtBVBcMrPcmvcKB45PUj4HjoKZN5lJ9DjUJ'

    def OAuth():
        try:
            auth = tweepy.OAuthHandler(API_key,API_key_secret)
            auth.set_access_token(Access_token,Access_token_secret)
            return auth
        except Exception as e:
            return None

    oauth = OAuth()
    api = tweepy.API(oauth)

    api.update_status('Hey this is my first tweet!')
    print('A tweet is posted')
tweet()

           