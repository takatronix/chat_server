# LLM Relay Server

### Description
This is a relay server for the LLM. It is responsible for handling requests from the client and forwarding them to the appropriate service. It also handles the responses from the services and sends them back to the client. 

### Setup and run

### .env file
Create a `.env` file in the root of the project with the following content:
```
PORT_PUBLIC=12000
PORT_CONTAINER=8000
OPENAI_API_KEY=openai-api-key
CLAUDE_API_KEY=claude-api-key
GROQ_API_KEY=groq-api-key
```

```
pip install -r requirements.txt
python main.py
```
### Docker
To run the server using docker, use the following command:
```
docker compose up --build
```

