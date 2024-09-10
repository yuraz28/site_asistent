# Асситент по сайту

## Введение

### Цель проекта - создать ассистента, который может консультировать пользователя по поводу информации с сайта, используя CLI

### Задачи:

* Реализовать загрузку и разбиение на чанки странички
* Перевести все чанки в эмбеддинги и сохранить в векторную базу данных FAISS
* Создать агента и скачать промпт для ChatGPT-4o
* Написать интерфейс взаимодействия с системой

## Quickstart

1. Clone the repository
```commandline
git clone https://github.com/yuraz28/site_assistent.git
```

2. Install venv
```commandline
pip install -r requirements.txt
```
3. Add your OpenAI token in config.py or .env file
config.py
```python
config = {
    "api_key": "e-aefifuwpf....."
}
```
.env file
```commandline
OPENAI_API_KEY="e-aefifuwpf....."
```
4. Run
```commandline
python main.py --link https://.....
```
Описание параметров для запуска:
```commandline
--link #Link to you website
--save_bd #True: save db file "faiss_index" (default: False)
--search_type  #Type search on db (default: similarity)
--link_prompt #link from the website https://smith.langchain.com/hub (default: hwchase17/openai-tools-agent)
```

## Возможное развитие:

* Использовать для развёртывания приложения docker
* Возможность заменить ChatGPT на Open source модель
* Разработка API
* Сохранение истории диалога (langchain.memory)