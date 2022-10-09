import tweepy

CONSUMER_KEY = '#'
CONSUMER_SECRET = '#'
ACCESS_KEY = '#'
ACCESS_SECRET = '#'

# authorization
auth = tweepy.OAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

choice = "YES"
while(choice == "YES"):
    print("Enter the correct user ID of the person")
    user = input()
    
    print("Enter the number of tweets you want to reply to")
    count = int(input())

    print("Enter what you want to reply with")
    message = input()

    tweets = api.user_timeline(user,count = count)

    if(len(tweets) == 0):
        print("No tweets available for the user " + user)
    else:
        for tweet in tweets:
            api.update_status(message , in_reply_to_status_id = tweet.id)
            print("Replied ---->" + message + "to --->  https://twitter.com/twitter/statuses/" +  str(tweet.id))

    print("Type YES to continue, NO to exit")

print("Thank you")

