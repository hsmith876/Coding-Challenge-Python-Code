# Coding-Challenge-Python-Code
Python code used for a coding challenge
You're on a website (such as Github!) with a text field which autocompletes usernames as you type. Under the hood, there's an API call which takes in the prefix of a username and then returns all usernames which start with that prefix, lexicographically sorted and truncated at 5 results.

Your task is to use this API call to dump the entire user database, specifically:

Implement the extract function in autocomplete.py. extract should return the whole user database, making calls to query under the hood.

Notes:

You can assume all valid usernames are comprised of lowercase ASCII letters (a-z).
Assume that queries to the API are expensive and should be minimized, but it's more important to have a correct answer and well-structured solution than an optimal answer.
You are welcome to include any tests or documentation that you'd normally provide when checking in to a shared codebase.
Submit your answer as a secret Gist. Please do not make your answers public (and please do not look for solutions from others).
