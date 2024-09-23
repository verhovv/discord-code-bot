<h1>Discord bot that can test your code</h1>

<h3>How to use it?</h3>
Just reply /run {stdin data} to the message with python code.
Bot will send output data and running time back.

<h3>Installation</h3>
<ol>
  <li>git clone https://github.com/verhovv/discord-code-bot</li>
  <li><a href="https://python-poetry.org/docs/">Install poetry and add it to path</a></li>
  <li>Create an .env file with fields like example.env (BOT_TOKEN, TIME_LIMIT in seconds)</li>
  <li>poetry shell</li>
  <li>poetry install</li>
  <li>python main.py</li>
</ol>
