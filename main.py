import argparse
from menegers import get_full_web_text, get_chunks, create_bd, create_agent


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start")
    parser.add_argument('--link', required=True, help='Link to you website')
    parser.add_argument('--save_bd', default=False, help='True: save db file "faiss_index"')
    parser.add_argument('--search_type', default="similarity", help='Type search on db')
    parser.add_argument('--link_prompt',
                        default=r"hwchase17/openai-tools-agent",
                        help=r'link from the website https://smith.langchain.com/hub')
    args = parser.parse_args()

    print(args)

    text = get_full_web_text(args.link)
    texts = get_chunks(text)
    retriever = create_bd(texts, save=args.save_bd, search_type=args.search_type)
    agent = create_agent(retriever, link_prompt=args.link_prompt)

    print("Привет!\nЯ твой помощник, можете задавать вопросы по вашему сайта\nЕсли хотите закончить, то напишите exit")

    while True:
        que = input("Вы: ")
        if que == "exit":
            break
        answer = agent.invoke({"input": que})
        print(f"Бот: {answer['output']}")
