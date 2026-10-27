
import matplotlib.pyplot as plt

def word_statistic(file_path = "lion.txt", out_file_path = "word_stat.txt"):

    file = open(file_path , 'r' , encoding ='utf-8')
    text = file.read().lower()

    delims = '!"#\'()*+-=,./:;<>?[\\]^—'

    for delim in delims:
        text = text.replace(delim , " " )

    words = text.split()
    total_words = len(words)

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted( word_count.items() , key=lambda item: item[1] , reverse=True )  

    with open(out_file_path, "w", encoding="utf-8") as out_file:
        out_file.write(f"{'WORD: ':<20} | {'COUNT: ' :<24} | {'PERCENT: ':<20}" + '\n') 
               
        for word , count in sorted_words :
            if (total_words > 0):
                percent = (count / total_words) * 100
            else : percent = 0
            out_file.write(f"{word :<20} | {count:<24} | {percent:<5.2f}%" + '\n')


        letter_count = {}
    for char in text:
        if char.isalpha():  
            letter_count[char] = letter_count.get(char , 0) + 1

    
    sorted_letters = sorted(letter_count.items(), key=lambda item: item[0])
    letters = [item[0] for item in sorted_letters]
    counts = [item[1] for item in sorted_letters]

    
    plt.figure(figsize=(14, 6))
    plt.bar(letters, counts, color="skyblue", edgecolor="black")
    plt.title(f"Встречаемость букв в тексте ({file_path})", fontsize=14)
    plt.xlabel("The Letters", fontsize=12)
    plt.ylabel("Repet count", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.show()



word_statistic()