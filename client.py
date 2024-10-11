from openai import OpenAI

# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(api_key = "sk-VOkleE2Xrqif43yja8dDSoSz6ZfnvFRoAkNYTeks-qT3BlbkFJ87_orFgetkc9k99jyrjTujKoUp7hyEGEQKtPrIFnQA",
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a virtual assistant, skilled in  general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "What is Coding"}
  ]
)
print(completion.choices[0].message.content)