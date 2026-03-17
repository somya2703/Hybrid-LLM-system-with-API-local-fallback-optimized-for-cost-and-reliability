from llama_cpp import Llama
from langchain_openai import ChatOpenAI
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

from config.settings import TOP_K_RESULTS, MODEL_PATH, OPENAI_MODEL
from src.logger import get_logger

logger = get_logger("rag")

# ---- Load local LLM once ----
logger.info("Loading local LLM...")

llm_local = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    n_threads=4
)


def run_local_llm(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""<|system|>
You are a helpful assistant. Answer ONLY using the provided context.
If the answer is not in the context, say "I don't know".

Context:
{context}

<|user|>
{query}

<|assistant|>
"""

    output = llm_local(
        prompt,
        max_tokens=200,
        temperature=0.7,
        top_p=0.9,
        stop=["<|user|>"]
    )

    return output["choices"][0]["text"].strip()


def generate_answer(query, vectorstore):
    logger.info("Running RAG pipeline")

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": TOP_K_RESULTS}
    )

    docs = retriever.invoke(query)

    # ---- OPENAI IS THE PRIMARY SOURCE ----
    try:
        logger.info("Trying OpenAI...")

        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(
                model=OPENAI_MODEL,
                temperature=0
            ),
            retriever=retriever,
            return_source_documents=True
        )

        result = qa_chain({"query": query})

        answer = result["result"]

        return {
            "answer": answer,
            "source": "openai"
        }

    except Exception as e:
        logger.warning(f"OpenAI failed: {e}")
        logger.info("Falling back to local LLM...")

        try:
            answer = run_local_llm(query, docs)

            return {
                "answer": answer,
                "source": "local_llm",
                "error": str(e)
            }

        except Exception as local_error:
            logger.error(f"Local LLM failed: {local_error}")

            return {
                "answer": "Both OpenAI and local model failed.",
                "source": "error",
                "error": f"{e} | {local_error}"
            }