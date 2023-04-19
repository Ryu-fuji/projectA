import os
import openai
openai.api_key = os.getenv("CHATGPTAPI")
messages = []

# 指定できるroleはassistant, system, userの3種類
messages.append({"role": "system", "content": "あなたはChatGPTです。Userからの質問に答えてください。"})

answer = input("何泊で生きたいですか？： ")
messages.append({"role": "assistant", "content": "何泊で行きたいですか？"})
messages.append({"role": "user", "content": answer+"で行きたいです。"})

answer = input("どこの地方の山に登りたいですか？： ")
messages.append({"role": "assistant", "content": "どこの地方の山に登りたいですか？"})
messages.append({"role": "user", "content": answer+"の山に登りたいです。"})


messages.append({"role": "user", "content": "要望に合った山と登山コースを教えてください。"})

# userはユーザからのセリフ
# assistantはChatGPT自身のセリフ
# systemとassistantの違いはよくわからない

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)

print(response["choices"][0]["message"]["content"])