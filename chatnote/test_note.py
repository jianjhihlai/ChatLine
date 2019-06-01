from chatnote.notecost import NoteCost


print("您好，我是您的記帳小幫手")

while True:
    note = input()
    user_id = 'default'
    processor = NoteCost(note, user_id)
    print(processor.response())

