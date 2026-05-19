from flask import (
    Flask,
    render_template,
    jsonify,
    request
)

from datetime import datetime

import os
import time
import random
import platform

from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)

from langchain_community.vectorstores import (
    Chroma
)

from langchain_core.prompts import (
    ChatPromptTemplate
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from langchain_core.runnables import (
    RunnablePassthrough
)

from langchain_ollama import (
    ChatOllama,
    OllamaEmbeddings
)


app = Flask(__name__)


# ======================================
# Configuration
# ======================================

UPLOAD_FOLDER = "uploads"

CHROMA_DB = "chroma_db"

os.makedirs(

    UPLOAD_FOLDER,

    exist_ok=True
)

os.makedirs(

    CHROMA_DB,

    exist_ok=True
)


# ======================================
# Ollama Embeddings
# ======================================

embedding_model = OllamaEmbeddings(

    model="nomic-embed-text"
)


# ======================================
# Ollama LLM
# ======================================

llm = ChatOllama(

    model="gemma3"
)


# ======================================
# Analytics Variables
# ======================================

api_counter = 0

quotes = [

    "AI is transforming the future.",

    "Flask powers scalable APIs.",

    "Build intelligent systems.",

    "Think. Build. Deploy.",

    "Innovation starts with curiosity."

]


# ======================================
# Home Route
# ======================================

@app.route("/")
def home():

    return render_template(

        "index.html"
    )


# ======================================
# Dashboard API
# ======================================

@app.route("/api/dashboard")
def dashboard():

    global api_counter

    start_time = time.time()

    api_counter += 1

    response_time = round(

        (time.time() - start_time) * 1000,

        2
    )

    return jsonify({

        "status": "success",

        "developer": "Ajay Kumar",

        "role": "Senior ML Engineer",

        "quote": random.choice(quotes),

        "api_hits": api_counter,

        "timestamp": datetime.now().strftime(

            "%d-%m-%Y %H:%M:%S"
        ),

        "system": {

            "python_version":
            platform.python_version(),

            "platform":
            platform.system(),

            "processor":
            platform.processor()
        },

        "performance": {

            "response_time_ms":
            response_time
        }

    })


# ======================================
# Skills API
# ======================================

@app.route("/api/skills")
def skills():

    return jsonify({

        "skills": [

            "Python",

            "Flask",

            "Machine Learning",

            "RAG",

            "LangChain",

            "ChromaDB",

            "RequireJS",

            "REST APIs",

            "Ollama",

            "Vector Databases"

        ]
    })


# ======================================
# Upload PDF API
# ======================================

@app.route(

    "/api/upload",

    methods=["POST"]
)
def upload_pdf():

    if "file" not in request.files:

        return jsonify({

            "status": "error",

            "message": "No file uploaded"

        })


    file = request.files["file"]


    filepath = os.path.join(

        UPLOAD_FOLDER,

        file.filename
    )

    file.save(filepath)


    # Load PDF

    loader = PyPDFLoader(filepath)

    documents = loader.load()


    # Split Documents

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=50
    )

    chunks = splitter.split_documents(

        documents
    )


    # Create Vector Store

    vectorstore = Chroma.from_documents(

        documents=chunks,

        embedding=embedding_model,

        persist_directory=CHROMA_DB
    )
    return jsonify({

        "status": "success",

        "message":
        "PDF uploaded and indexed successfully"

    })


# ======================================
# Ask Question API
# ======================================

@app.route(

    "/api/ask",

    methods=["POST"]

)
def ask_question():

    try:

        data = request.get_json()

        question = data.get("question")


        if not question:

            return jsonify({

                "status": "error",

                "message": "Question is required"

            })


        # Load Vector Store

        vectorstore = Chroma(

            persist_directory=CHROMA_DB,

            embedding_function=embedding_model
        )


        retriever = vectorstore.as_retriever()


        # Prompt

        template = """

        Answer the question based only
        on the provided context.

        Context:
        {context}

        Question:
        {question}

        """


        prompt = ChatPromptTemplate.from_template(

            template
        )


        # Format Documents

        def format_docs(docs):

            return "\n\n".join(

                doc.page_content

                for doc in docs
            )


        # RAG Pipeline

        rag_chain = (

            {

                "context":
                retriever | format_docs,

                "question":
                RunnablePassthrough()

            }

            | prompt

            | llm

            | StrOutputParser()
        )


        answer = rag_chain.invoke(

            question
        )


        return jsonify({

            "status": "success",

            "answer": answer

        })


    except Exception as e:

        print(e)

        return jsonify({

            "status": "error",

            "message": str(e)

        }), 500
# ======================================
# Main
# ======================================

if __name__ == "__main__":

    app.run(

        debug=True
    )