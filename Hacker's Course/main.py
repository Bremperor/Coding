option=""
while option!="QUIT":
    # Import library of functions we will use for filewriting .etc
    import lib.backend

    print("Welcome to this text only Youtube that I cloned! ")
    new_account=input('Do you have a channel (Y for yes, N for no): ')

    channel_name=""
    sub_count=0
    videos_list=[]
    subscriptions=[]

    

    if new_account=="Y":
        channel_name=input("Enter existing name: ")
        sub_count=lib.backend.get_channel_videos(channel_name)
        video_list=lib.backend.get_channel_videos(channel_name)
    elif new_account=="N":
        channel_name=input("What is your new channel name? ")
        sub_count=lib.backend.get_channel_subscriber_number(channel)

    def subscribe_to_channel(channel_name):
        subscriptions.append(channel_name)
        lib.backend.subscribe_to_channel(channel_name)

    def print_menu():
        print("Search bar")
        print("")

    def print_channel_stat(channel_name):
        print("Name: ", lib.backend.get_channel_name(channel_name))
        print("Sub count", lib.backend.get_channel_subscriptions(channel_name))
        print("Videos: ", lib.backend.get_channel_videos(channel_name))
        print("Subscriptions: ", lib.backend.get_channel_subscriptions(channel_name))

    def subscribe_to_channel(channel_name):
        subscriptions.append(channel_name)
        lib.backend.subscribe_to_channel(channel_name)

    def search_bar():
        channel_search=input("Enter channel name: ")
        print_channel_stat(channel_search)

        
        check_subscribe=""
        while check_subscribe!="Y" and check_subscribe!="N":
            check_subscribe=input("Would you like to subscribe: ")
            if check_subscribe=="Y":
                subscribe_to_channel(channel_search)
            elif check_subscribe=="N":
                print("Ok, not subscribed")

    print("Welcome to this Youtube with only text! ")
    option=input("To stop using Youtube, type QUIT ")

