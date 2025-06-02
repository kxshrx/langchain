from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite')


# model to gen notes + quiz then togehter otu

notes_prompt = PromptTemplate(
    template="for the given topic about {topic} give me notes of length 250 words",
    input_variables=['topic']
)

quiz_prompt = PromptTemplate(
    template="for the given topic about {topic} generate me a multipel choice and multi answer questions totalling to 4 questions",
    input_variables=['topic']
)


merge_prompt = PromptTemplate(
    template="merge the notes {notes} in top section with the quiz {quiz} in the below section to the end user as proper learning material ",
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": notes_prompt | model | parser,
    "quiz": quiz_prompt | model | parser,

})

merge_chain = merge_prompt | model | parser

chain = parallel_chain | merge_chain


response = chain.invoke({'topic':'thermodynamics'})

print(response)

chain.get_graph().print_ascii()











# OUTPUT OF THE ABOVE CODE


# ## Thermodynamics: A Quick Overview & Quiz

# Thermodynamics is the study of energy transfer and transformation, particularly involving heat, work, and internal energy. It's governed by four fundamental laws that dictate the behavior of energy in various systems. Understanding thermodynamics is crucial in fields like engineering, chemistry, and physics.

# **The Zeroth Law** establishes thermal equilibrium, stating that if two systems are each in thermal equilibrium with a third system, they are also in thermal equilibrium with each other. This essentially defines temperature.

# **The First Law** is the law of conservation of energy. It states that the change in internal energy (ΔU) of a closed system equals the heat added to the system (Q) minus the work done by the system (W): ΔU = Q - W. This means energy cannot be created or destroyed, only converted from one form to another.

# **The Second Law** introduces the concept of entropy, which is a measure of disorder. It states that the total entropy of an isolated system can only increase or remain constant in a reversible process. This implies that natural processes tend towards increasing disorder, explaining the direction of spontaneous changes. It also defines the limitations of converting heat into work, introducing the concept of efficiency.

# **The Third Law** states that the entropy of a perfect crystal at absolute zero (0 Kelvin) is zero. This implies that it is impossible to reach absolute zero in a finite number of steps.

# These laws are applied to various systems, from engines and refrigerators to chemical reactions and biological processes, providing a framework to understand and predict energy transformations.

# **Now, test your knowledge with these questions:**

# **Question 1: Multiple Choice**

# Which of the following statements accurately describes the First Law of Thermodynamics?

# (a) Energy can be created or destroyed in a closed system.
# (b) The total energy of an isolated system is constant.
# (c) The entropy of an isolated system always decreases.
# (d) Heat always flows from a hot object to a cold object.
# (e) Work is always done on a system.

# **Correct Answer: (b)**

# **Question 2: Multiple Answer**

# Which of the following are state functions in thermodynamics? (Select all that apply)

# (a) Heat (Q)
# (b) Work (W)
# (c) Internal Energy (U)
# (d) Enthalpy (H)
# (e) Temperature (T)
# (f) Path (P)

# **Correct Answers: (c), (d), (e)**

# **Question 3: Multiple Choice**

# A gas expands isothermally (constant temperature). Which of the following statements is/are TRUE regarding the process?

# (a) The internal energy of the gas increases.
# (b) The gas does no work.
# (c) Heat is absorbed by the gas from its surroundings.
# (d) The enthalpy change is zero.
# (e) The pressure of the gas remains constant.

# **Correct Answers: (c), (d)**

# **Question 4: Multiple Answer**

# Which of the following processes are considered adiabatic? (Select all that apply)

# (a) A slow, reversible expansion of a gas in a perfectly insulated container.
# (b) A rapid compression of a gas in a poorly insulated container.
# (c) A process where no heat transfer occurs between the system and its surroundings.
# (d) A process where the temperature of the system remains constant.
# (e) The expansion of a gas in a vacuum (free expansion).

# **Correct Answers: (a), (b), (c), (e)**


#                     +---------------------------+                      
#                     | Parallel<notes,quiz>Input |                      
#                     +---------------------------+                      
#                        ***                   ***                       
#                    ****                         ****                   
#                  **                                 **                 
#     +----------------+                          +----------------+     
#     | PromptTemplate |                          | PromptTemplate |     
#     +----------------+                          +----------------+     
#              *                                           *             
#              *                                           *             
#              *                                           *             
# +------------------------+                  +------------------------+ 
# | ChatGoogleGenerativeAI |                  | ChatGoogleGenerativeAI | 
# +------------------------+                  +------------------------+ 
#              *                                           *             
#              *                                           *             
#              *                                           *             
#     +-----------------+                         +-----------------+    
#     | StrOutputParser |                         | StrOutputParser |    
#     +-----------------+                         +-----------------+    
#                        ***                   ***                       
#                           ****           ****                          
#                               **       **                              
#                     +----------------------------+                     
#                     | Parallel<notes,quiz>Output |                     
#                     +----------------------------+                     
#                                    *                                   
#                                    *                                   
#                                    *                                   
#                           +----------------+                           
#                           | PromptTemplate |                           
#                           +----------------+                           
#                                    *                                   
#                                    *                                   
#                                    *                                   
#                       +------------------------+                       
#                       | ChatGoogleGenerativeAI |                       
#                       +------------------------+                       
#                                    *                                   
#                                    *                                   
#                                    *                                   
#                           +-----------------+                          
#                           | StrOutputParser |                          
#                           +-----------------+                          
#                                    *                                   
#                                    *                                   
#                                    *                                   
#                       +-----------------------+                        
#                       | StrOutputParserOutput |                        
#                       +-----------------------+    