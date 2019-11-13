import random
from flask import Flask, render_template_string, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flag{e4rth_4nd_ch1k1b4mb0ni}'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            text = request.values.get('meme_text')
            rzhaka = request.values.get('rzhaka_maximum')
            if text is not None:
                if 'config' in text:
                    return 'Ваш мем содержит запрещенную мнемонику 😳'

                if rzhaka == 'on':
                    rzhaka = '<script src="/static/rzhaka.js"></script>'
                else:
                    rzhaka = ''

                return render_template('meme.html', rzhaka = rzhaka,
                                       meme = render_template_string('<div class="meme">%s</div>' % text))

        except Exception as e:
            print(e)
            return 'Internal Server Error'

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
