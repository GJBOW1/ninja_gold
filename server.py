# Ninja Gold Assignment - Coding Dojo - Gregg Bowen

from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'Not all who wander are lost.'

@app.route('/', methods=['GET','POST'])
def home():
    if 'gold' and 'message' not in session:
        session['gold'] = 0
        session['message'] = []
        return render_template('index.html')
    else: 
        return render_template('index.html')
    

@app.route('/process_money', methods=['GET', 'POST'])
def process():

    if 'farm' == request.form['real_estate']:
        gold = random.randint(10, 20)
        session['gold'] = session['gold'] + gold
        print('Gold = ', gold)
        session['message'].append(f"Earned {gold} from the farm!")
        print(session['message'])
        return redirect('/')

    if 'cave' == request.form['real_estate']:
        gold = random.randint(5, 10)
        session['gold'] = session['gold'] + gold
        print('Gold = ', gold)
        session['message'].append(f"Earned {gold} from the cave!")
        print(session['message'])
        return redirect('/')

    if 'house' == request.form['real_estate']:
        gold = random.randint(2, 5)
        session['gold'] = session['gold'] + gold
        print('Gold = ', gold)
        session['message'].append(f"Earned {gold} from the house!")
        print(session['message'])
        return redirect('/')
    
    if 'casino' == request.form['real_estate']:
        gold = random.randint(-50, 50)
        session['gold'] = session['gold'] + gold
        print('Gold = ', gold)
        if gold <= -1:
            session['message'].append(f"Entered a casino and lost {abs(gold)} gold... Ouch!")
        elif gold == 0:
            session['message'].append(f"Entered a casino and neither gained or lost anything!")
        else:
            session['message'].append(f"Entered a casino and earned {gold}... Great job!")
        return redirect('/')
    


if __name__ == "__main__":
    app.run(debug=True, port=5001)
