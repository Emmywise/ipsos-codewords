# Flask Backend for Codeword Actions API

This application serves as the backend for the Codeword Actions system, providing a REST API to manage codewords and their associated actions.

## Features

- Look up the action ID associated with a given codeword.
- Retrieve all codewords associated with a given action ID.

## Getting Started
Clone the repository and navigate to the backend directory named codewords

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python app.py  

API Endpoints
GET /action/by_codeword/<codeword>: Returns the action ID for a given codeword.
GET /action/by_id/<action_id>: Returns all codewords for a given action ID.
Testing
Use Postman or curl to test the API endpoints.



# React Frontend for Codeword Actions

This React application serves as the frontend for the Codeword Actions system, providing a user-friendly interface to interact with the Flask backend.

- **User Input**: Allows users to input codewords and retrieve associated action IDs.
- **Action ID Retrieval**: Enables users to input action IDs to fetch and display associated codewords.

## Getting Started
Clone the repository and navigate to the frontend directory named codewords-frontend

# Install Dependencies

Using npm: npm install
using Yarn: yarn install

Start the development server:
Using npm: npm start
using Yarn: yarn start


# The API will be using port 3000, feel free to use a different port for the frontend
# A json file that contain samples of json data has been included in to help setup the application faster