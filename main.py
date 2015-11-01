from allergy.allergy import allergy


def input_output():
    input_str = input().split(" ")
    friend_cnt = int(input_str[0])
    dish_cnt = int(input_str[1])
    friends = input().split(" ")
    friends_for_dishes = []
    if len(friends) != friend_cnt:
        print("error!")
        return
    for i in range(dish_cnt):
        input_str = input().split(" ")
        friend_cnt_for_dish = int(input_str[0])
        friends_for_dish = input_str[1:]
        friends_for_dishes.append(friends_for_dish)
        if len(friends_for_dish) != friend_cnt_for_dish:
            print("error!")
            return

    print(allergy(friends, friends_for_dishes))


def execute(func):
    n = int(input())

    for i in range(n):
        func()


execute(input_output)
