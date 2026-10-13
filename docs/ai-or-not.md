AI or Not? 

Component: ai-service
Issue: #50
Purpose: Identify 10 questions that require AI and 10 questions that can be solved without AI.

1. Questions That Need AI

No.	Question	Needs AI?	Reason
1	Can you explain recursion in Python in simple terms?	Yes	AI can adapt explanations to the student’s understanding.
2	Can you summarize this long article?	Yes	AI can understand and summarize natural language.
3	Can you suggest a personalized study plan?	Yes	AI can interpret learning goals and individual needs.
4	Can you explain why my Python code is incorrect?	Yes	AI can analyze code and explain possible mistakes.
5	Can you translate this paragraph into Vietnamese?	Yes	AI can interpret context and translate natural language.
6	Can you generate practice questions from this lesson?	Yes	AI can understand educational content and create relevant questions.
7	Can you evaluate the clarity of my written answer?	Yes	AI can analyze meaning, structure, and writing quality.
8	Can you suggest improvements to my essay?	Yes	AI can provide context-aware writing suggestions.
9	Can you explain this complex scientific concept using an example?	Yes	AI can generate flexible explanations and examples.
10	Can you identify the main idea of this paragraph?	Yes	AI can interpret meaning and extract important information.

2. Questions That Do Not Need AI

No.	Question	Needs AI?	Reason
1	What is 15 + 25?	No	Basic arithmetic can be calculated directly.
2	What is the average of five grades?	No	A mathematical formula produces an exact result.
3	Is this number even or odd?	No	The modulo operator can determine the answer.
4	How many students are in this list?	No	A simple counting function is sufficient.
5	Can you sort these numbers in ascending order?	No	A standard sorting algorithm solves this task.
6	Is this password field empty?	No	A basic validation rule can check the input.
7	What is today’s date?	No	The system clock provides the current date.
8	Convert 120 minutes into hours.	No	A simple mathematical conversion is sufficient.
9	Does this student’s grade meet the passing threshold?	No	A conditional comparison gives an exact answer.
10	Can you display my saved timetable?	No	The application can retrieve structured data directly.

3. Conclusion

AI should be used for tasks that require natural language understanding, contextual reasoning, personalized explanations, or content generation.

Traditional programming should be preferred for tasks involving mathematical calculations, data validation, sorting, structured data retrieval, and other deterministic operations.

Using AI only when necessary helps reduce computational costs, improve response speed, and increase system reliability.

4. Acceptance Criteria

* [x]	List 10 questions that need AI.
* [x]	List 10 questions that do not need AI.
* [x]	Provide a one-line reason for every question.
* [x]	Present the results in Markdown tables.
* [x]	Prepare the content for docs/ai-or-not.md.

Related Issue: #50
Component: ai-service
