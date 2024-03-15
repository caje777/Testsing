from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']

    number_of_vowels = 0
    number_of_consonants = 0
    number_of_y = 0
    number_of_spaces = 0
    number_of_sentences = 0

    for letter in text:
        if letter.lower() in 'aeiou':
            number_of_vowels += 1
        elif letter.lower() in 'qwrtpsdfghjklzxcvbnm':
            number_of_consonants += 1
        elif letter.lower() == 'y':
            number_of_y += 1
        elif letter == ' ':
            number_of_spaces += 1
        elif letter in '!.?':
            number_of_sentences += 1

    number_of_letters = number_of_vowels + number_of_consonants + number_of_y
    number_of_words = len(text.split())

    return render_template('result.html', vowels=number_of_vowels, consonants=number_of_consonants, letters=number_of_letters, y=number_of_y, spaces=number_of_spaces, words=number_of_words, sentences=number_of_sentences)

if __name__ == '__main__':
    app.run(debug=True)
