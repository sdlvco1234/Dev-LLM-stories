from flask import Flask, render_template, request
import os
import ollama

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/gallery')
def gallery_flexbox():
   file_names = os.listdir('./static/pics/')
   files_path = []
   for file in file_names:
      path = '../static/pics/' + file
      files_path.append(path)

   return render_template('gallery_flexbox.html', mes_fichiers=files_path, a=0)

@app.route('/page')
def Page2():
   return render_template('Page2.html')

@app.route('/description')
def Description():
   url = "static/pics/Reksio6.jpeg"
   response = ollama.chat(model='llava', 
   messages=[{
        'role': 'user', 
        'content': 'describe this image',
        'images': [url]
    }],
   )
   lama_response = response['message']['content']
   app.logger.info(lama_response)
   return render_template("description.html", url=url, lama_response=lama_response)
   


if __name__ == "__main__":
   app.run(debug=True)

