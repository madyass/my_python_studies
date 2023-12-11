import random

def choose_word(topic):#asks user to choose a topic
    words_dict = {
        'animals': ['zebra', 'cat', 'elephant', 'wolf', 'donkey','monkey'],
        'fruits': ['cherry', 'banana', 'orange', 'grape', 'stawberry','grapefruit'],
        'countries': ['united states', 'england', 'france', 'japan', 'scotland','germany']
    }
    
    return random.choice(words_dict.get(topic,['a']))#select random word topic which is selected by user 

def draw (wrong):#draws hangman ,depends on wrong number
    if wrong==1:
        print("""
             --------------   
             |            |
             |            |
             |          -----
             |          |   |
             |          |   |
             |          -----
             |
             |
             |
             |
             |
             |
             |
             | 
              """)
                      
    elif wrong==2: 
        print("""
             --------------   
             |            |
             |            |
             |          -----
             |          |   |
             |          |   |
             |          -----
             |            |     --
             |            |    /
             |            |---/
             |
             |
             |
             |
             | 
              """)     
    elif wrong==3:
        print("""
             --------------   
             |            |
             |            |
             |          -----
             |          |   |
             |          |   |
             |          -----
             |     --     |     --
             |       \    |    /
             |        \---|---/
             |
             |
             |
             |
             | 
              """) 
    elif wrong==4:
        print("""
             --------------   
             |            |
             |            |
             |          -----
             |          |   |
             |          |   |
             |          -----
             |     --     |     --
             |       \    |    /
             |        \---|---/
             |            |
             |            |
             |             \ 
             |              \    
             |               \ 
              """) 
    elif wrong>=5:
        print("""
             --------------   
             |            |
             |            |
             |          -----
             |          |   |
             |          |   |
             |          -----
             |     --     |     --
             |       \    |    /
             |        \---|---/
             |            |
             |            |
             |           / \ 
             |          /   \    
             |         /     \ 
              """) 
        print("\n_______GAME OVERR_______\n")
        return True
    return False
            

                          
print("-------WELCOME TO THE HAGNMAN GAME--------")

topics=["animals","fruits","countries"]

selected_topic = input("Please choose a topic (animals, fruits, countries): ").lower()

while selected_topic not in topics:#is user topic in topics
    selected_topic = input("Please choose one of from these topisc (animals, fruits, countries): ").lower()

word=choose_word(selected_topic)

word_temp=[]#user's word

for i in range(len(word)):
    if word[i]!=" ": #for breaks
            word_temp.append("_")
    else:
        word_temp.append(" ")

user_entries=[]

wrong=0#the number of user's mistakes  

while wrong < 5:
    entry_temp = input("Please enter a letter: ")
    
    while entry_temp in user_entries:
        entry_temp = str(input("Please enter a letter which is not entered before: "))
    
    if len(entry_temp)>1 or type(entry_temp)!=str:#for get letter which is proper
        print("your enter must be a letter and string!")
        continue

    entry_temp=entry_temp.lower()
    
    user_entries.append(entry_temp)
    print("Your entries:", " ".join(user_entries))

    if entry_temp in word:
        for i in range(len(word)):
            if entry_temp == word[i]:
                word_temp[i] = entry_temp
        print(" ".join(word_temp))
    else:
        wrong += 1
        if draw(wrong):
            print("correct answer was:",word)
            break#finish game

    if "_" not in word_temp:
        print("\nCongratulations! correct answers is",word)
        break