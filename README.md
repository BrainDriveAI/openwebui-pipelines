> ⚠️ **Archived Project**  
> This project is no longer actively maintained by the original authors.  
> The repository remains available for reference and community use.

# BrainDriveAI's Custom Pipelines for OpenWebUI

Welcome to our collection of **custom OpenWebUI pipelines**! These pipelines enhance the capabilities of your OpenWebUI instance by integrating advanced logic, external services, and modular workflows.  

---

## 🚀 Pipelines Overview  

OpenWebUI pipelines enable **flexible workflows**, empowering users to handle complex tasks efficiently. With support for various providers (e.g., OpenAI, Ollama, PostgreSQL, Neo4j), these pipelines deliver robust memory management, transcript-based chat, and more.  

### Available Pipelines  

#### 1. **Chat with YouTube Pipeline**  

##### OpenAI Version  
- **[Chat with YouTube (OpenAI)](https://github.com/BrainDriveAI/openwebui-pipelines/blob/main/pipelines/chat-with-youtube-openai-pipeline.py)**  
  - **Description:**  
    Searches YouTube videos, retrieves transcripts, generates summaries, and enables Q&A over video transcripts. Uses OpenAI's GPT for processing.  
  - **Features:**  
    - Video transcript retrieval and summarization.  
    - Video content search and Q&A.  
    - Integrates with OpenAI for natural language understanding.  

##### Ollama Version  
- **[Chat with YouTube (Ollama)](https://github.com/BrainDriveAI/openwebui-pipelines/blob/main/pipelines/chat-with-youtube-ollama-pipeline.py)**  
  - **Description:**  
    Similar to the OpenAI version, but uses Ollama's local LLMs for transcript processing.  
  - **Features:**  
    - Local transcript processing with Ollama.  
    - No external API calls, ensuring privacy and cost efficiency.  

---

#### 2. **Memory Pipelines**  

##### OpenAI + PostgreSQL (Supabase)  
- **[Memory Pipeline (OpenAI + PostgreSQL)](https://github.com/Digital-Brain-Builders/openwebui-pipelines/blob/main/pipelines/memory-filter-openai-postgresql-pipeline.py)**  
  - **Description:**  
    A long-term memory pipeline that uses OpenAI for embeddings and Supabase PostgreSQL (with pgvector) for memory storage. Ideal for scalable cloud setups.  
  - **Features:**  
    - Stores and retrieves vectorized memories.  
    - Embedding support via OpenAI models.  
    - Memory storage in Supabase PostgreSQL.  

##### OpenAI + Neo4j (Local/Docker)  
- **[Memory Pipeline (OpenAI + Neo4j)](https://github.com/BrainDriveAI/openwebui-pipelines/blob/main/pipelines/memory-filter-openai-neo4j-pipeline.py)**  
  - **Description:**  
    A local-first memory solution using OpenAI for embeddings and Neo4j for graph-based memory storage. Runs entirely on your device via Docker.  
  - **Features:**  
    - Local vectorized memory storage using Neo4j.  
    - OpenAI-based embeddings for message processing.  
    - Full data persistence on local devices.  

##### Ollama + Neo4j (Local/Docker)  
- **[Memory Pipeline (Ollama + Neo4j)](https://github.com/BrainDriveAI/openwebui-pipelines/blob/main/pipelines/memory-filter-ollama-neo4j-pipeline.py)**  
  - **Description:**  
    Similar to the OpenAI + Neo4j pipeline but uses Ollama’s local LLMs for embedding. Fully local solution with no external dependencies.  
  - **Features:**  
    - Local embeddings using Ollama.  
    - Neo4j for graph-based memory storage.  
    - Privacy-first and cost-effective.  

---

## 📦 Installation and Setup  

### Installing Pipelines  

1. **Copy the GitHub URL** of the pipeline you want to install:  
   - [Chat with YouTube (OpenAI)](https://github.com/BrainDriveAI/openwebui-pipelines/blob/main/pipelines/chat-with-youtube-openai-pipeline.py)  
   - [Chat with YouTube (Ollama)](https://github.com/Digital-Brain-Builders/openwebui-pipelines/blob/main/pipelines/chat-with-youtube-ollama-pipeline.py)  
   - [Memory Pipeline (OpenAI + PostgreSQL)](https://github.com/Digital-Brain-Builders/openwebui-pipelines/blob/main/pipelines/memory-filter-openai-postgresql-pipeline.py)  
   - [Memory Pipeline (OpenAI + Neo4j)](https://github.com/BrainDriveAI/openwebui-pipelines/blob/main/pipelines/memory-filter-openai-neo4j-pipeline.py)  
   - [Memory Pipeline (Ollama + Neo4j)](https://github.com/BrainDriveAI/openwebui-pipelines/blob/main/pipelines/memory-filter-ollama-neo4j-pipeline.py)  

2. **Go to Admin Panel -> Settings -> Pipelines** in your OpenWebUI instance.  
3. **Paste the GitHub URL** in the "Install from GitHub URL" field.  
4. **Click the Install / Download icon** to complete the installation.  

### Setting Up the Dockerized Neo4j Memory Pipelines  

For local Neo4j-based memory pipelines, use the provided `docker-compose.yml` to set up Neo4j and OpenWebUI with pre-installed pipelines.  

#### Steps:  
1. Copy the `docker-compose.yml` file to your system.  
2. Run the following command in the directory containing the file:  
   ```bash
   docker-compose up -d
   ```  
3. Access Neo4j at [http://localhost:7474](http://localhost:7474) (username: `neo4j`, password: `my_password123`).  
4. Your OpenWebUI instance will have the pre-installed memory pipeline ready to use.  

---

## Troubleshooting  

If you encounter issues like:  
```
FieldValidatorDecoratorInfo.__init__() got an unexpected keyword argument 'json_schema_input_type'
```  
Upgrade `pydantic` to version 2.7.4 inside the Docker container:  
```bash
pip install --upgrade pydantic==2.7.4
```  

---

## 📚 References  

- [OpenWebUI Pipelines Documentation](https://github.com/open-webui/pipelines)  
- [Supabase PostgreSQL with pgvector](https://supabase.com/docs/guides/database/extensions/pgvector)  
- [Neo4j Graph Database](https://neo4j.com/)  
- [OpenAI API Documentation](https://beta.openai.com/docs/)  
- [Ollama Documentation](https://www.ollama.com/)  
- [Mem0 Documentation](https://docs.mem0.ai/overview)  

---

## 🌐 License  

This project is licensed under the **MIT License**.  
