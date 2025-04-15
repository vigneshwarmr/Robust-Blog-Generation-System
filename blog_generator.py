from llama_cpp import Llama
import os

MODEL_PATH = os.path.join("models", "llama-2-7b-chat.Q4_K_M.gguf")
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

def generate_blog(prompt, max_words, audience):
    system_prompt = f"You are a helpful blog writing assistant. Write a blog post for {audience}. Limit the blog to {max_words} words."
    final_prompt = f"{system_prompt}\n\nTopic: {prompt}\n\nBlog:\n"

    print("\n--- Prompt Sent to Model ---\n", final_prompt)

    output = llm(prompt=final_prompt, max_tokens=max_words * 3, stop=["</s>"])
    blog_text = output["choices"][0]["text"].strip()

    print("\n--- Raw Model Output ---\n", blog_text[:500])  # Show a preview

    words = blog_text.split()
    trimmed_text = " ".join(words[:max_words])
    return trimmed_text
