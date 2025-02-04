from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(pet_name, color):
    # temperature -> how creative you want model to be 0: safe - 1: creative
    llm = OpenAI(temperature=0.7)
    prompt_template_name = PromptTemplate(
        input_variables=["pet_name", "colot"],
        template="I have a pet {pet_name} and I want to name it. It is {color} color. Suggest five cool names for my pet.",
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="names")
    response = name_chain({'pet_name':pet_name, 'color':color})

    return response


if __name__ == '__main__':
    print(generate_pet_name("elephant", "black"))
    