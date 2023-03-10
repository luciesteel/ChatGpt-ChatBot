# ChatGpt-ChatBot
コンソールから入力した文章をOpenAI AIに送信し、応答文をVOICEVOX APIを通して読み上げます。

# 必要環境
NVIDIA CUDA
Python 3.8.10
VOICEVOX API(https://github.com/VOICEVOX/voicevox_engine)

# 事前準備
OpenAIのアクセストークンを設定しておきます。

```
export OPENAI_API_KEY="sk-xxxx"
```

実行
```
python .\run.py --voicevox_dir="./engines/windows-nvidia" --use_gpu
```

```
python .\chatgpt-voicevox.py
```