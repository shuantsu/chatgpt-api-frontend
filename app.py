from flask import Flask, request, make_response, render_template
import openai, time, json, markdown

config = json.loads(open('config.json','r',encoding='utf8').read())

openai.organization = config['openai.organization']
openai.api_key = config['openai.api_key']

app = Flask('app')

def ask_chatgpt(model, question):
    t1 = time.time()
    response = openai.ChatCompletion.create(
    model=model,
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": question},
        ]
    )
    elapsed = '%0.2f'%(time.time()-t1)

    result = ''
    for choice in response.choices:
      result += choice.message.content
      
    html = markdown.markdown(result, extensions=['tables','fenced_code'])
    return render_template("md2html.html", content=html, elapsed=elapsed, prompt=question)

@app.route('/search')
def search():
  return """
  <script async src="https://cse.google.com/cse.js?cx=42b66c5df499946db">
</script>
<div class="gcse-search"></div>
"""

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/app', methods=['POST','GET'])
def main_app():
	if request.method == 'POST':
		return ask_chatgpt(request.form.get('model'), request.form.get('question',''))
	else:
		return render_template('form.html')

app.run(debug=True)