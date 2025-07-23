from flask import Flask, render_template_string, url_for

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {
      margin: 0;
      padding: 0;
      background-color: rgb(224, 63, 3);
      text-align: center;
      font-family: sans-serif;
    }

    .frame img {
      width: 100%;
      height: auto;
      display: block;
      border-radius: 4px;
    }

    /* 📱 адаптація для телефону */
    @media (max-width: 480px) {
      .frame {
        margin: 10px auto;
        padding: 4px;
        border-radius: 6px;
      }
      .frame img {
        border-radius: 3px;
      }
    }
  </style>
</head>
<body>
  <div class="frame">
    <img src="{{ url_for('static', filename='1.jpg') }}">
  </div>
  <div class="frame">
    <img src="{{ url_for('static', filename='2.jpg') }}">
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
