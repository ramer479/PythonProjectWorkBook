
def get_count(word, name1, name2):
    names =  name1+name2
    count = 0
    for i in range(0,len(word)):
        # if word[i] in names:
        #     for m in range(0,len(names)):
        #         if word[i] == names[m]:
        #             count += 1
        char_count = names.count(word[i])
        count += char_count
    return count

def get_count_way_elobarate(word, name1, name2):
    names =  name1+name2
    count = 0
    for i in range(0,len(word)):
        if word[i] in names:
            for m in range(0,len(names)):
                if word[i] == names[m]:
                    count += 1
    return count

if __name__ == "__main__":
    print("Welcome to Love calculator")
    p1 = input("Please enter Person#1 name: ").lower()
    p2 = input("Please enter Person#2 name: ").lower()

    word1 = "True".lower()
    word2 = "Love".lower()

    word1_count = get_count(word1,p1,p2)
    word2_count = get_count(word2,p1,p2)
    love_percent = int(str(word1_count)+str(word2_count))

    if love_percent < 10 or love_percent >= 90:
        print(f"Your score is **{love_percent}**, you go together like coke and mentos.")
    elif love_percent > 40 and love_percent <= 50:
        print(f"Your score is **{love_percent}**, you are alright together.")
    else:
        print(f"Your score is **{love_percent}**.")