import os
import shutil
while True:
    print("D.A.V.E.: What are you going to ask me about?")

    question = input('You: ')
    print("D.A.V.E.: And what should I answer you?")

    answer = input('You: ')
    print("D.A.V.E.: What is the subject of this conversation?")

    sub = input('You: ')
     # Cria o arquivo e escreve a conversa
    title = sub + '.txt'
    file = open(title, 'w')
    conversation = []
    conversation.append(question + '\n')
    conversation.append(answer)
    file.writelines(conversation)
    file.close()
    # movendo arquivo de lugar
    local = os.getcwd()
    shutil.move(title, local+ '/teste')
    print("D.A.V.E.: Should I learn something more?")
    s = input('You: ')
    s = s.lower()
    if s == 'yes':
        continue
    elif s == 'no':
        print('Okay')
        break
    else:
        print("I couldn't understand.")
        break


