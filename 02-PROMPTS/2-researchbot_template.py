from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""Summarize the research paper titled {user_input} in a {style_input} tone, with a length of approximately {length_input} words. The summary should cover the main objective of the study, the methodology or experimental setup, and highlight any important mathematical models, equations, or formulations, explaining them briefly where appropriate. It should also include the key results and findings, along with the conclusion or broader implications of the work. Ensure that both the technical and mathematical aspects are clearly conveyed in a way that aligns with the chosen tone and summary length.""",
    input_variables=['user_input', 'style_input','length_input'],
    validate_template=True
)


template.save('research_query_template.json')