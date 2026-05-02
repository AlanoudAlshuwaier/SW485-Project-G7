# Prompt Design Rationale

## Template Design Overview

### Template 1: Simple Explanation

**Goal:** Explain the prediction to the patient in plain, friendly language.

**Target user:** Patients with no medical background.

**Design choice:** Short response (3–5 sentences), no medical jargon, reassuring tone.


---

### Template 2: Personalized Explanation

**Goal:** Provide a personalized explanation by linking the prediction to the patient’s specific values.

**Target user:** Patients who want a more relevant and tailored explanation of their results.

**Design choice:** Uses the patient’s actual data (e.g., age, lab values) to make the explanation more meaningful and engaging, while still keeping the language simple and easy to understand. Maintains a supportive tone without using complex medical terminology.

**Implementation note:** Outputs were saved to files instead of displayed in the notebook to avoid truncation and ensure complete evaluation.


---

### Template 3: Detailed Reasoning

**Goal:** Provide a structured explanation of the prediction by breaking down key medical indicators and explaining their role in the result.

**Target user:** Users who want a deeper understanding of how specific lab values contribute to the prediction.

**Design choice:** Focuses on explaining important features in a structured way (what it is, what it indicates, and its relevance to liver health). This improves transparency and helps users understand the reasoning behind the prediction without overwhelming them.


---

### Template 4: Step-by-Step Reasoning

**Goal:** Provide a detailed step-by-step analysis of each lab value and how it supports or contradicts the prediction.

**Target user:** Advanced users who want full interpretability and reasoning transparency.

**Design choice:** Evaluates each value individually against normal ranges and builds a logical conclusion. This maximizes interpretability but increases response length.


---

## Testing & Comparative Analysis

### Test Setup

Each prompt template was tested using three different cases from the dataset:
- Patient 1: Liver Disease Detected (row 0)
- Patient 2: No Liver Disease (row 315)
- Patient 3: Liver Disease Detected (row 440)

All templates were applied to the same test cases to ensure a fair comparison.


---

### Qualitative Evaluation

| Template        | Relevance   | Detail      | Clarity    | Personalization | Safety |
|----------------|------------|------------|------------|----------------|--------|
| T1 Simple      | Medium     | Low        | Very High  | Low            | High   |
| T2 Personalized| High       | Medium     | High       | High           | High   |
| T3 Detailed    | Very High  | High       | Medium     | Medium         | High   |
| T4 Step-by-step| Very High  | Very High  | Medium     | Low            | High   |


### Analysis

The templates showed clear differences in their outputs based on their structure and purpose.

The simple template produced very clear and easy-to-understand responses, but lacked detail and did not explain the reasoning behind the prediction.

The personalized template improved relevance by incorporating patient-specific values, making the response more engaging and meaningful.

The detailed template provided structured explanations of key medical indicators, improving transparency and helping users understand the reasoning behind the prediction.

The step-by-step template offered the most comprehensive reasoning by analyzing each value individually, but its length made it less suitable for non-expert users.


---

### Quantitative Analysis

| Template        | Avg Response Length | Keyword Usage | Readability |
|----------------|----------------|--------------|-------------|
| T1 Simple      | 80          | 3-4          |Very Easy        |
| T2 Personalized| 200         | 8-10       | Easy        |
| T3 Detailed    | 220           | 12-14         | Medium      |
| T4 Step-by-step| 230      | 15-18    | Hard        |


---

**Note:** The quantitative metrics (average response length and keyword usage) were calculated by taking the average across the three test cases for each template. This approach ensures a fair and consistent comparison between templates by reducing the impact of variation in individual responses.

### Handling Output Truncation During Testing

During testing, some model responses were truncated when displayed in the notebook due to output length limits. To ensure complete and accurate evaluation, outputs were saved directly to text files instead of relying on printed results.

This approach allowed:
- Capturing the full response without loss of information  
- Reviewing outputs more clearly  
- Supporting fair comparison between templates  

This improved the reliability of the evaluation process.


---





