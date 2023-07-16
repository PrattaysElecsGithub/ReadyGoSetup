from flask import Flask as f

app = f(__name__, template_folder="envfiles")


# ════════════════ WEBPAGES AREA ══════════════════
@app.route("/")
def welcome():
    return "<br>Welcome To The ReadyGoSetup Server!</br><br>This Server Is Hosted On Your Machine(bc i dont have a " \
           "server), </br><br>" \
           "With Frequent updates on GitHub!</br><br>Auto-Updating Is A Future Idea!</br>"


@app.route("/tptenvsetup")
def tptenv():
    with open("envfiles/tpt.txt", 'r') as tpt:
        tptenv_text = tpt.read()

    return tptenv_text


# ════════════════════════════════════════════════

app.run(port=6543)
