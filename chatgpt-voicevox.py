import openai
import os
import requests
import json
import pyaudio
import time

openai.api_key = os.getenv('OPENAI_API_KEY', 'default')

msg = [{"role": "system", "content": "あなたは賢いAIです。"}]

while True:
    prompt = input("> ").strip()
    if prompt in ["quit", "exit"]:
        break
    msg.append({"role": "user", "content": prompt})
    res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msg, max_tokens=1024, temperature=0.5)
    ans = res["choices"][0]["message"]["content"].strip()
    print(ans)
    res1 = requests.post('http://127.0.0.1:50021/audio_query',params = {'text': ans, 'speaker': 1})
    res2 = requests.post('http://127.0.0.1:50021/synthesis',params = {'speaker': 1},data=json.dumps(res1.json()))

    data = res2.content

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=24000,
                output=True)

    time.sleep(0.2)

    stream.write(data)

    stream.stop_stream()
    stream.close()

    p.terminate()
    msg.append({"role": "assistant", "content": ans})
    if res["usage"]["total_tokens"] > 3000:
        msg.pop(1)