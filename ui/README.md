# User Interface Plan

## Overview
This folder contains the planning and frontend code for the Smart Virtual Assistant. Currently, this is a placeholder. In future iterations, we will build an interactive web-based chat interface using **Streamlit**.

## How the UI will call the Backend
Since our backend is currently a local Python package (`src/assistant/`), the UI (Streamlit app) will interact with it by directly importing the backend modules. 

The flow will be:
1. The user types a query (e.g., "where is the IT helpdesk?") into the UI chat input box.
2. The Streamlit app captures this text and passes it to the backend function (e.g., `assistant.rules.reply(text)`).
3. The backend processes the text, looks up the data (from `data/offices.csv`), and returns a formatted string.
4. The Streamlit app receives the string and displays it in the chat history on the screen.

## UI Mockup
Here is the initial design/mockup for our chat interface:

![Chat UI Mockup](../docs/ui_mockup.png)
