# FAQ Assistant

Welcome to the **FAQ Assistant**, a cutting-edge project that combines the power of language models, 
vector databases, and PostgreSQL to create a seamless chatting experience with the RobinHood investing assistant, 
which specialises in Q/A over Robinhood's Investing FAQ.
This messenger allows users to interact with the assistant,
leveraging the capabilities of OpenAI's language model, while also storing and managing chat histories
for further research and analysis and company to reduce costs for technical support.


## Getting Started🚀
1. Clone this repository: `git clone https://github.com/yehorkhod/faq-assistant`  
2. Change directory into the repository: `cd faq-assistant`  
3. Create a virtual environment: `python -m venv venv`
4. Activate it:
   - Windows: `.\venv\Scripts\activate`
   - Mac: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Create a .env file and add your OpenAI API key: `OPENAI_API_KEY = ...` and PostgreSQL URI: `DATABASE_URI = ...`
7. Run `streamlit run app.py` in your terminal
8. Have fun!🤗


## Project Overview🌐
### Technologies Used:
* ChromaDB: A vector database used for efficient storage and retrieval of vectors.
* LangChain: Utilizing the capabilities of OpenAI, LangChain is utilized to construct Language Model (LLM) chains for generating responses in the chat.
* Psycopg2: A PostgreSQL adapter for Python, facilitating seamless interaction with the PostgreSQL database.
* Streamlit: The user interface is developed using Streamlit, offering a user-friendly and interactive platform for chatting.


## Project Structure📂
* requirements.txt: Lists all the dependencies required for the project.
* .env: Configuration file holding secrets such as OpenAI API key and PostgreSQL connection details.
* index/: Directory where the vector store is placed.
* documents_load.py: Script to install data and create the vector store in the index directory.
* model.py: The core of the project, where the Language Model (LLM) chain is constructed.
* chat_to_json_parser.py: Contains functions to dump a list of messages into a JSON format.
* database_initialize.py: Connects and initializes the PostgreSQL database.
* database_interaction.py: Utility functions for easier interaction with the database.
* app.py: The main file where the Streamlit app is implemented.
* strings.py: Holds important strings separated for better code organization.


## Disclaimer⚠️
This project serves as an example of how FAQ Assistant can operate in a fictional setting. 
The use of the name "Robinhood" in this project, as well as any mentions of "Robinhood," is solely for demonstration purposes 
and does not indicate any endorsement, affiliation, or connection with the real company. 
The project author respects the trademarks and terms set by Robinhood and advises users 
to read and adhere to those terms.

If you have any questions about the usage or legality of the content in this project, 
it is recommended to seek legal advice.


## Who, When, Why?
💻 Author: Yehor Khodysko <br />
📅 Version: 1.0 <br />
📜 License: This project is licensed under the MIT License </br>
