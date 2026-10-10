# TV3 AI assistance log

AI reviewed the student's supplied Week 1 files and prepared these corrections:
- Rename text_tool.py to text_tools.py to match the test imports.
- Add a transpose docstring comparing C++ and Python.
- Remove top-level demo prints so importing modules has no output.
- Treat punctuation as word separators and return no results for k <= 0.
- Repair GitHub Actions workflow structure and select TV3/variant 3 explicitly.

Before committing, the student must inspect and understand every change,
run the tests locally, and record their own verification result in the PR.
The workflow currently tests TV3 Week 1, not all members or later weeks.
