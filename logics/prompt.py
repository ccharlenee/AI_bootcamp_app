from langchain_core.prompts import PromptTemplate
from helper_functions import llm

def create_single_pdf_chain():
    """
    Takes:
    {
        "context": "text from a single paper"
        "question": "...user query..."
        }
    Returns a summary for that paper only.
    """
    policy_prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are advising policy officers at Singapore’s National Parks Board (NParks).

Using the specific document, 
generate a summary of the key results from the study in bullet points,
then use the results to product a policy-relevant summary for Singapore including:                                          

- Key findings
- Evidence strength
- Implications for Singapore's policy landscape
- Recommended actions for Singapore 
- Risks or limitations

Consider Singapore's: urban density and land constraints

Write clearly and professionally, free of jargon.

Context:
{context}

Question: 
{question}

Policy Summary:
"""
    )

    def llm_wrapper(input_dict):
        prompt_text = policy_prompt.format(**input_dict)
        return llm.get_completion(prompt_text)

    return llm_wrapper