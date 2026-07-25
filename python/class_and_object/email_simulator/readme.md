# Email Simulator

A simple, terminal-based email simulation written in Python. This project demonstrates core Object-Oriented Programming (OOP) concepts, including class instantiation, encapsulation, and object interaction.

## How It Works

The system is built on three primary classes that interact with one another:

### 1. `Email` Class
Represents a single email message.
*   **Attributes:** `sender`, `receiver`, `subject`, `body`, `timestamp`, and a boolean `read` status.
*   **Functionality:** Can mark itself as read, format its own data for a full display, and provide a string summary (Read/Unread status, sender, subject, and time).

### 2. `Inbox` Class
Acts as the storage mechanism for a user's emails.
*   **Attributes:** A list called `emails`.
*   **Functionality:** Handles the logic for receiving, listing, reading, and deleting emails based on their index position in the list.

### 3. `User` Class
Represents an individual interacting with the system.
*   **Attributes:** A `name` and their own dedicated `Inbox` object.
*   **Functionality:** Acts as the controller. It can send emails (which pushes an `Email` object directly into another `User`'s `Inbox`), check its own inbox, read specific messages, and delete them.

## Execution

When you run the script, the `main()` function executes a predefined scenario:
1.  Creates two users: 'Tory' and 'Ramy'.
2.  Tory sends an email to Ramy.
3.  Ramy replies to Tory.
4.  Ramy checks his inbox, opens the first email, deletes it, and checks his inbox again to verify the deletion.

## How to Run

1.  Ensure you have Python installed on your machine.
2.  Clone or download this repository.
3.  Navigate to the directory containing the file in your terminal.
4.  Execute the script using:
    ```bash
    python email_simulator.py
    ```

## Limitations
*   **No Persistent Storage:** This runs entirely in memory. All users and emails are destroyed when the script finishes executing.
*   **No Interactive UI:** Currently, actions are hardcoded in the `main()` function for demonstration purposes. It does not accept real-time command-line input.
