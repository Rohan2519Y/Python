# import webbrowser
# import os

# html_content = """
# <!DOCTYPE html>
# <html>
# <head><title>Text to Speech</title></head>
# <body>
# <h2>Text to Speech</h2>
# <textarea id="text" rows="5" cols="50">Hello! This is text to speech.</textarea><br><br>
# <button onclick="speak()">Speak</button>
# <button onclick="window.speechSynthesis.cancel()">Stop</button>

# <script>
# function speak() {
#   const text = document.getElementById('text').value;
#   const utter = new SpeechSynthesisUtterance(text);
#   window.speechSynthesis.speak(utter);
# }
# </script>
# </body>
# </html>
# """

# # Save and open in browser
# with open("tts.html", "w") as f:
#     f.write(html_content)

# webbrowser.open("file://" + os.path.abspath("tts.html"))
# print("Opened in browser!")



from elevenlabs.client import ElevenLabs

client = ElevenLabs(api_key="key")

audio = client.text_to_speech.convert(
    text="hello",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_turbo_v2",
)

# Save and play
with open("output.mp3", "wb") as f:
    for chunk in audio:
        f.write(chunk)

import os
os.startfile("output.mp3")  # Windows auto-play
print("Done! Playing output.mp3")