import json
import os
import shutil


def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)


data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """7""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2025""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Interprofessional Education (IPE): Medicine and Public Health""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The goal of this project is to design, develop, and validate a multi-agent chatbot that is capable of facilitating educational conversations representing diverse team members in typical medical setting. Interprofessional Education (IPE) is a collaborative method to develop students as future team members working with colleagues from different fields. IPE occurs when students from two or more professions learn about, from, and with each other. Specifically, the project will focus on:
            Customizing an open-source LLM (e.g., LLaMA3) using Retrieval-Augmented Generation (RAG) and/or fine-tuning techniques (e.g., LoRA) to create a chatbot agents tailored for IPE experiences.
            Evaluating the chatbot's performance (e.g., adherence to instructions, depth of interactions, representation of professional fields) by simulating diverse student interactions using multiple LLM agents.
            Conducting user interface (UI) and usability testing to improve user experience.
            Optionally, integrating Learning Tools Interoperability (LTI) features to enable seamless usage in Learning Management Systems (LMS).
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            The dataset for fine-tuning and customization is still TBD. However, data will likely consist of relevant open-source academic texts,
             dialogue datasets, and domain-specific content to build the required context for medical field perspectives.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            Generative AI (genAI) technology offers a novel approach to supporting IPE given that routinely the diversity of team member participants is limited, and some fields are under-represented in IPE training but influential in "real world" teams. By using LLM-based chatbots for this educational
             interventions, there is potential to both improve how learning experiences are delivered and  enhance student post-IPE performance . In this project, we will explore how an AI-driven team collaboration can  act as an educational 
             intervention.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            The project will proceed in several phases:
            **Requirement Analysis**: Collaborate with lead researchers to define key components of IPE experiences and specify chatbot performance
            requirements.
            **Development**: Customize one or more open-source LLMs to create the initial version of the chatbot using RAG and fine-tuning methods.
            **Validation**: Conduct multi-agent testing to evaluate the chatbot's performance across multiple medical/health domains and with varied inputs, focusing on 
            metrics such as adherence to guidelines, professional field representations, and ability to stay on topic.
            **Usability Evaluation**: Perform usability testing with end users, including metrics for user satisfaction, ease of use, and learning outcomes.
            **(Optional) Integration**: Develop LTI integration to connect the chatbot with existing LMS tools to ensure accessibility for students in course
            environments.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This is a rough timeline for the project:
             **Weeks 1-2**: Familiarization with project requirements, intellectual humility constructs, and open-source tools.
             **Weeks 3-8**: Design, develop, and build a working prototype.
             **Weeks 9-12**: Iterative testing and improvement of chatbot performance, incorporating feedback from simulated interactions.
             **Weeks 13-16**: Multi-agent testing and usability evaluation.
             **Weeks 17-18**: Final reporting, documentation, and presentation of outcomes.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            This project is suitable for a team of 2-3 students, given the scope and need for interdisciplinary collaboration.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            Potential challenges for this project include:
             **Limited Training Data**: Finding appropriate datasets for Retrieval-Augmented Generation or fine-tuning the LLM may be a limiting factor.
             **Complexity of Interdisciplinary Teams**: Designing prompts and interactions to genuinely foster  collaborations of diverse teams, requiring careful iteration and feedback.
             **Interdisciplinary Collaboration**: This project spans multiple disciplines (e.g., Public Health, Medicine, Education, Data Science, Software Engineering), 
             requiring effective collaboration and understanding across fields.
            """,

        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Dr. Ryan Watkins and Andy Wiss",
        "Proposed by email": "rwatkins@gwu.edu",
        "instructor": "Amir Jafari",
        "instructor_email": "ajafari@gmail.com",
        "github_repo": "https://github.com/amir-jafari/Capstone",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + os.sep + f'Arxiv{os.sep}Proposals{os.sep}{data_to_save["Year"]}{os.sep}{data_to_save["Semester"]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + os.sep + f'Arxiv{os.sep}Proposals{os.sep}{data_to_save["Year"]}{os.sep}{data_to_save["Semester"]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy('json_gen.py', output_file_path)
print(f"Data saved to {output_file_path}")
