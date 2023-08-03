# GatiVidhi: Third Party Legal Claims
The project GatiVidhi aims to generate the written statement from the legal documents such as Petition and Investigation Report online thus taking less time than generating documents online.Thus the name of the project stands for Gati(speed) in Vidhi(legal principles).

<img src=https://github.com/kesavsanthosh/GatiVidhi/assets/138132906/4bb44c97-33a6-434e-b5a6-4bd05eec1c9a height=200 width=300>

## 📝 Project Highlight: 'Third Party Legal Claims' 📝

In this hackathon, our objective was to develop a cutting-edge solution to streamline the process of creating written statements for insurance companies, enabling them to effectively defend against insurance claims. Our project, 'Third Party Legal Claim,' tackled this challenge with innovative technology and seamless integration.

## The Challenge
The insurance industry often faces the cumbersome task of analyzing image-based documents submitted by claimants to process their insurance claims. Manually converting image documents into text files for further analysis is time-consuming and error-prone, leading to delays and inefficiencies in handling claims.

## Overview of our solution
In recent times, the legal landscape has witnessed an unsettling rise in false third-party legal claims, which poses a significant challenge to the justice system and adversely impacts individuals, businesses, and society at large. 
The insurance company have to make sure that all the policies being true. Creating the final draft is time consuming task as the format is almost similar for all the cases and there are many conditions in which the final verdict is same. 
Our aim is to develop a solution to prepare the draft so that the insurance company could easily check the draft and verify whether the claim is valid or not. We are using Machine Learning and NLP models to automatically generate case drafts.

## Process Flow
<img src=https://github.com/kesavsanthosh/GatiVidhi/assets/138132906/ec362288-f0ea-4e9e-8cd1-0f8353a5d966 height=300 width=400>

## Solution architecture
<img src=https://github.com/kesavsanthosh/GatiVidhi/assets/138132906/d9664cc9-6f4a-43ac-b0e9-c71e2d9d98d6 height=600 width=800>

## How is our solution different?

### Multilingual Approach:
Information is shared across borders and languages in this interconnected world. By incorporating multiple languages into the system, it becomes more relevant and valuable for users worldwide, enabling them to understand and digest content in their preferred language.
We will be allowing the user to give the input files in any language they are comfortable in. This will make the system user friendly and easy to access by the users. 
We will be, first, detecting the language using langdetect library and then we will be translating the text to the standard language English or the language in which the lawyer is comfortable in using GoogleTranslator from deep_translator library in Machine Learning.

### Different types of data:
Legal claims often involve various types of evidence, including written documents, audio recordings, and images. Allowing different file formats ensures that all relevant evidence can be submitted and considered during the claim drafting process. This comprehensive inclusion helps in presenting a more complete and accurate representation of the case.
The audio recordings and images can be converted into text. Then the text can be pre-processed, and drafts can be generated using the same.
The audio recordings can be converted to texts using pydub library and google speech recognition function and pytesseract library can be used to convert images to text.

### ROUGE to evaluate the Drafts
ROUGE evaluates summaries using algorithms and predefined metrics, ensuring consistent, standardized evaluation across various summarization systems. Rouge-score library from Machine Learning can be used to evaluate the summaries extracted from the relevant documents.
This will help lawyers to get the most accurate draft and help the user claim the expenses legally.

### Legal Knowledge-Base
A legal knowledge base offers centralized access to legal information, enabling professionals and the public to understand legal concepts and resources. A comprehensive legal knowledge base saves time and costs by enabling professionals to quickly access relevant information.
This system will help the lawyer to search for any complex legal jargon feature during the study of the draft. The Legal Knowledge-Base System allows us to keep the extracted information into separate categories, subcategories and topics.

## Risks/Challenges/Dependencies
### Document and Evidence Management:
 Effective legal claims management requires accurate indexing, retrieval, and maintenance of large volumes of documents, preventing errors and oversight.

### Content Variability:
 Texts can vary significantly in terms of domain, genre, language style, and length. The system should be adaptable enough to handle different types of content effectively. Ensuring that the system performs well across diverse text sources can be a challenge.

### Document and Evidence Management: 
Effective legal claims management requires accurate indexing, retrieval, and maintenance of large volumes of documents, preventing errors and oversight.

### Context Understanding: 
Texts often contain references to previous information or contextual cues that help in understanding the cases fully. Ensuring that the system accurately captures and utilizes the relevant context is a challenge. In some cases, the system may generate summaries that are disconnected from the overall context.

### Evaluation Metrics:
 Assessing text summarizer performance is challenging, with ROUGE metrics having limitations in quality and readability. Developing comprehensive evaluation methods remains a challenge.

### Scalability: 
Scalability is crucial for websites with high traffic or complex functionalities. Flask's simplicity helps, but potential bottlenecks like database performance, caching, and load balancing must be addressed.

## The Solution
To overcome these challenges, our team devised an ingenious solution. Leveraging the power of Optical Character Recognition (OCR) technology, we automated the conversion of image-based documents into easily manageable text files. Next, we utilized the Natural Language Toolkit (NLTK) to efficiently pre-process the textual data, ensuring accuracy and coherence.

The integration of the GPT API into our project was the real game-changer, as its advanced language processing capabilities enabled swift completion of written statements for insurance companies, saving time and significantly improving accuracy and quality.
