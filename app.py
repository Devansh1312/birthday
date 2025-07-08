from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Sample photo data - you can replace with your actual photos and messages
PHOTOS = [
    {'filename': 'photo1.jpg', 'message': 'Our first adventure together! ❤️'},
    {'filename': 'photo2.jpg', 'message': 'You always make me smile 😊'},
    {'filename': 'photo3.jpg', 'message': 'Dancing under the stars with you'},
    {'filename': 'photo4.jpg', 'message': 'Your laugh is my favorite sound'},
    {'filename': 'photo5.jpg', 'message': 'Making memories that last forever'},
    {'filename': 'photo6.jpg', 'message': 'You light up every room you enter'},
    {'filename': 'photo7.jpg', 'message': 'Coffee dates and endless conversations'},
    {'filename': 'photo8.jpg', 'message': 'Your kindness inspires me daily'},
    {'filename': 'photo9.jpg', 'message': 'Sunset walks with my favorite person'},
    {'filename': 'photo10.jpg', 'message': 'You make ordinary moments extraordinary'},
    {'filename': 'photo11.jpg', 'message': 'Your strength amazes me every day'},
    {'filename': 'photo12.jpg', 'message': 'Silly moments that mean everything'},
    {'filename': 'photo13.jpg', 'message': 'You are my sunshine on cloudy days'},
    {'filename': 'photo14.jpg', 'message': 'Adventure awaits when I\'m with you'},
    {'filename': 'photo15.jpg', 'message': 'Your dreams are beautiful, just like you'},
    {'filename': 'photo16.jpg', 'message': 'Celebrating another year of your awesomeness'},
    {'filename': 'photo17.jpg', 'message': 'You make 20 look absolutely perfect'},
    {'filename': 'photo18.jpg', 'message': 'Every day with you is a gift'},
    {'filename': 'photo19.jpg', 'message': 'Your smile is contagious'},
    {'filename': 'photo20.jpg', 'message': 'Building dreams together'},
    {'filename': 'photo21.jpg', 'message': 'You are stronger than you know'},
    {'filename': 'photo22.jpg', 'message': 'Creating our own fairy tale'},
    {'filename': 'photo23.jpg', 'message': 'Your passion for life inspires me'},
    {'filename': 'photo24.jpg', 'message': 'Twenty years of being incredible'},
    {'filename': 'photo25.jpg', 'message': 'You deserve all the happiness in the world'},
    {'filename': 'photo26.jpg', 'message': 'Here\'s to many more adventures'},
    {'filename': 'photo27.jpg', 'message': 'You make every day brighter'},
    {'filename': 'photo28.jpg', 'message': 'Your heart is pure gold'},
    {'filename': 'photo29.jpg', 'message': 'Thank you for being you'},
    {'filename': 'photo30.jpg', 'message': 'Happy 20th Birthday, my love! 🎂❤️'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cake')
def cake():
    return render_template('cake.html')

@app.route('/card')
def card():
    return render_template('card.html')

@app.route('/photos')
def photos():
    return render_template('photos.html', photos=PHOTOS)

@app.route('/cut-cake', methods=['POST'])
def cut_cake():
    return jsonify({'status': 'success', 'message': 'Cake cut successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
