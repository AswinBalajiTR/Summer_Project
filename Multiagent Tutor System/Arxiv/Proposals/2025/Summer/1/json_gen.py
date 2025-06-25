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
            """1""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2025""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Summer""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """MultiAgent Tutor System""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The goal of this project is to design, develop, and evaluate a multi-agent tutoring system where each 
            AI model serves as a domain specific agent. When a user poses a question, the agents engage in an internal 
            dialogue sharing, debating, and refining ideas to collaboratively generate the most accurate and 
            educationally effective response, simulating the dynamics of a panel of expert tutors.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            The OpenBookQA dataset is a collection of multiple-choice questions designed to evaluate reasoning and 
            knowledge comprehension. It is particularly useful for training AI models in educational contexts, making 
            it an ideal choice for the MultiAgent Tutor System project.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            Traditional tutoring systems often rely on single-agent models that generate static, one-size-fits-all
            responses. A multi-agent AI framework offers a transformative alternative—where each model acts as a domain 
            expert and engages in internal discussions to collaboratively generate accurate, context-aware, and 
            pedagogically rich answers. This approach enables dynamic reasoning, interpretability & human-like 
            collaboration and redefines the tutoring experience through advanced data science and AI, making it more 
            effective, adaptive, and aligned with real-world learning needs.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            The project will proceed in several phases:
            **Requirement Analysis**: Collaborate with educational experts to define learning objectives and performance requirements for the tutoring system.
            **Literature Review**: Review existing tutoring systems and advancements in AI and multiagent frameworks to identify best practices and relevant datasets, including OpenBookQA.
            **System Design**: Design the architecture of the multiagent system, defining agent roles and communication protocols for collaborative responses.
            **Data Collection and Preparation**: Gather and preprocess relevant datasets for training, ensuring data is clean and structured for effective model training.
            **Model Selection and Customization**: Choose suitable open-source language models and customize them using techniques like Retrieval-Augmented Generation (RAG) to align with educational goals.
            **Development of Multiagent Framework**: Implement the multiagent system, enabling agents to interact and collaboratively generate responses through internal dialogue.
            **Testing and Validation**: Conduct iterative testing to evaluate performance metrics such as accuracy and user satisfaction, refining the system based on feedback.
            **Usability Evaluation**: Perform usability testing with end users to assess effectiveness and gather feedback for further improvements.
            **Integration and Deployment**: Develop integration capabilities with existing Learning Management Systems (LMS) and deploy the system for broader accessibility.
            **Final Reporting and Documentation**: Document the development process and prepare a final report summarizing outcomes, performance metrics, and recommendations for future enhancements.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This is a rough timeline for the project:
            **Weeks 1-2**: Requirement analysis and collaboration with educational experts to define objectives and performance requirements.
            **Weeks 3-4**: Conduct literature review on existing tutoring systems and advancements in AI, identifying relevant datasets.
            **Weeks 5-6**: Design the architecture of the multiagent system, define agent roles, and establish communication protocols.
            **Weeks 7-8**: Gather and preprocess relevant datasets for training, ensuring data quality and structure; select and customize open-source language models using techniques like Retrieval-Augmented Generation (RAG).
            **Weeks 9-10**: Develop the multiagent framework, enabling agents to interact and collaboratively generate responses; conduct iterative testing and validation to evaluate performance metrics.
            **Weeks 11-12**: Perform usability testing with end users to assess effectiveness, gather feedback for improvements, and develop integration capabilities with existing Learning Management Systems (LMS); finalize reporting and documentation.
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
            **Complexity of Interdisciplinary Teams**: Designing prompts and interactions to genuinely foster collaboration among diverse teams, requiring careful iteration and feedback.
            **Interdisciplinary Collaboration**: This project spans multiple disciplines (e.g., Public Health, Medicine, Education, Data Science, Software Engineering), necessitating effective communication and understanding across fields.
            **User  Engagement**: Ensuring that the multiagent system maintains user interest and engagement throughout the learning process can be challenging.
            **Scalability**: Developing a system that can efficiently handle a growing number of users and interactions without compromising performance.
            **Integration Challenges**: Ensuring seamless integration with existing Learning Management Systems (LMS) and addressing technical compatibility issues.
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
