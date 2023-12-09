# FAQ Assistant

Welcome to the **FAQ Assistant**, a bleading-edge project that combines the power of language models, 
vector databases, and PostgreSQL to create a seamless chatting experience with the RobinHood investing assistant, 
which specialises in Q/A over Robinhood's Investing FAQ. This messenger allows users to interact with the assistant,
leveraging the capabilities of OpenAI's language model, while also storing and managing chat histories
for further research and analysis and company to reduce costs for technical support.


## Getting Sturted🚀
1. Clone this repo `git clone https://github.com/yehorkhod/faq-assistant`  
2. CD into the directory `cd faq-assistant`  
3. Create a virtual environment `python -m venv envname`
4. Activate it: 
   - Windows: `.\envname\Scripts\activate`
   - Mac: `source envname/bin/activate`
5. Install the required dependencies `pip install -r requirements.txt`
6. Create .env file and add there your OpenAI API key `OPENAI_API_KEY = ...` and PostgreSQL URI `DATABASE_URI = ...`
7. In terminal run `steamlit run app.py`
8. Have fun!🤗


## Project Overview🌐
### Technologies Used:
* ChromaDB: A vector database used for efficient storage and retrieval of vectors.
* LangChain: Harnessing the power of OpenAI, LangChain is employed to build Language Model (LLM) chains
for generating responses in the chat.
* Psycopg2: A PostgreSQL adapter for Python, enabling smooth interaction with the PostgreSQL database.
* Streamlit: The user interface is built using Streamlit, providing a user-friendly and interactive platform for chatting.


## Project Structure📂
* requirements.txt: Lists all the dependencies required for the project.
* .env: Configuration file holding secrets such as OpenAI API key and PostgreSQL connection details.
* index/: Directory where the vector store is placed.
* documents_load.py: Script to install data and create the vector store in the index directory.
* model.py: The heart of the project, where the Language Model (LLM) chain is constructed.
* chat_to_json_parser.py: Contains functions to dump a list of messages into a JSON format.
* database_initialize.py: Connects and initializes the PostgreSQL database.
* database_interaction.py: Utility functions for easier interaction with the database.
* app.py: The main file where the Streamlit app is implemented.
* strings.py: Holds significant strings separated for better code organization.


## Disclaimer⚠️
This project is an illustration of how FAQ Assistant can work in a fictional context. 
The name "Robinhood" used in this project, including any references to "Robinhood" is for demonstration purposes only 
and does not imply any endorsement, affiliation, or association with the actual company. 
The project author acknowledges the trademarks and terms outlined by Robinhood and encourages users 
to review and comply with those terms.

If you have any questions about the usage or legality of the content in this project, 
it is recommended to seek legal advice.


## Who, When, Why?
💻 Author: Yehor Khodysko <br />
📅 Version: 1.0 <br />
📜 License: This project is licensed under the Apache License 2.0 </br>  ###
