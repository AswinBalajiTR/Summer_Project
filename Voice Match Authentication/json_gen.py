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
            """3""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2025""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Summer""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Voice Auth""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """The goal of this project is to develop a robust voice-based authentication system that verifies a user's identity 
            through both their voice and a unique spoken command. Unlike traditional systems that rely solely on transcription 
            or fixed pitch recognition, this system is designed to accurately match voices even when pitch, tone, or speaking 
            conditions vary—such as speaking softly in an office or with high energy in a noisy environment. By combining speaker
            recognition with command verification, it aims to provide a more secure and user friendly alternative to conventional 
            biometric logins.
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
            Current voice systems primarily focus on speech-to-text or basic voice detection, lacking true voice to voice 
            matching for authentication. However, human voice varies naturally depending on context, mood, and environment 
            posing a major challenge for rigid systems. This project addresses that gap by building a model that learns the 
            unique characteristics of a user's voice across varying pitches and conditions. It ensures that authentication 
            remains consistent and reliable, regardless of how or where the user speaks. This innovation brings voice biometrics
            closer to real-world usability and strengthens the future of secure, hands free authentication in both personal 
            and professional settings.
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
        "Proposed by": "Aswin Balaji Thippa Ramesh, Rahul Arvind, Siddharth Saravanan",
        "Proposed by email": "at119@gwu.edu, rahul.arvind@gwu.edu, siddharth.saravanan@gwu.edu",
        "instructor": "Amir Jafari",
        "instructor_email": "ajafari@gmail.com",
        "github_repo": "https://github.com/AswinBalajiTR/Summer_Project",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + os.sep + f'Arxiv{os.sep}Proposals{os.sep}{data_to_save["Year"]}{os.sep}{data_to_save["Semester"]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + os.sep + f'Arxiv{os.sep}Proposals{os.sep}{data_to_save["Year"]}{os.sep}{data_to_save["Semester"]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy('json_gen.py', output_file_path)
print(f"Data saved to {output_file_path}")
