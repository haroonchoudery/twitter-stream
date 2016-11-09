import tweepy

consumer_key = "xI1HAahzW99fuitHnMuyuZ8fc";

consumer_secret = "JddkBAIepqL9K8N3qDUF9w6JXOu0ieiXhxsQCRMPTv5UIZwomR";

access_token = "17651073-ykFBS4fXM83XqQTFq9uZ8T0o7WbKi0uu5HfdQ27H6";

access_token_secret = "E3VrnFHssSWOQRjAm8weSL5LM0qNK8OCQZViVBuhPMcKU";

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



