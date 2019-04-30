get_game_subscribers = input("Enter game c-cricket v-volleyball b-basketball : ")
        if get_game_subscribers == "all":
            for k,v in sports_subscribed.items():
                print(k,"subscribed students:")
                for s in v:
                    print(student_info[s]['name'])
        elif get_game_subscribers == "c":
            print("Cricket subscribed students:")
            for v in sports_subscribed['cricket']:
                print(student_info[v]['name'])
            # print(sports_subscribed)
        elif get_game_subscribers == 'cb':
            crick_basket = sports_subscribed['cricket'].intersection(sports_subscribed['basketball'])
            for s in crick_basket:
                print(student_info[s]['name'])
            print(crick_basket)