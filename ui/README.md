# UI Plan

## Purpose

This directory will contain the Smart Virtual Assistant user interface.
The planned interface will use Streamlit or Gradio in Week 7; the team will
confirm the framework before implementation.
No UI implementation is required for Lab 1.

## Planned features

- A text input for the user's question.
- A submit button to send the question to the assistant.
- An area displaying the assistant's response.
- A helpful message when no matching office is found.

## Interaction flow

1. The user enters a question, such as `Where is the IT Helpdesk?`.
2. The user submits the question.
3. The UI passes the text to `assistant.rules.reply(message)`.
4. The UI displays the returned response without changing office details.

Expected example: `IT Helpdesk: room E.005, open Mon-Fri 08:00-17:00.`

For an empty question, display `Please type a question.`. For an unknown office,
display the backend's fallback response and suggest an available office name.

## Data integration

The UI will call the backend in `src/assistant/`.
The backend will use office information from `data/offices.csv`.
The CSV schema, sample-data limitations, and update responsibilities are documented
in [`data/README.md`](../data/README.md). Lab 1 uses the command-line entry point;
there is no web UI or UI installation command yet.

## Planned acceptance checks

- Submitting a known office name shows its room and opening hours.
- Empty input and an unknown office produce useful messages without a crash.
- Mixed-case office names work consistently with the backend.
- The question input has a visible label and supports keyboard submission.
- Responses wrap and remain readable on a narrow mobile screen.

## Owner

Member 3: ykeban2516.
