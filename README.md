# portfl
My Portfolio

# Local Setup
- Enable virtual environment for python
  `python3 -m venv ../portfl`
- Activate virtual environment
  `. ./bin/activate`

# Install Flask
`pip3 install Flask`

- Set Environment Variables
    `export FLASK_ENV=development` # Only set this for development and not production
    `export FLASK_APP=server.py`

- # Run App
  `flask run` 

- Generate Requirements.txt file dynamically
  `pip freeze > requirements.txt`


