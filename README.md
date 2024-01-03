# Filter Application with Flask

This Flask project, named "Filter Application," consists of the following structure:

## Project: Flask

- **Location:** `Filter Application Flask/Flask`
- **Files:**
  - `app.py`: Main Flask application file.
  - `static`: Directory for static assets (CSS, JS, images, etc.).
  - `templates`: Directory for HTML templates.
    - `index.html`: Home page template.
    - `process.html`: Template for processing form data.

### Main Flask Application (`app.py`)

This file (`app.py`) contains the main Flask application code. It defines two routes:

1. **Home Route (`'/'`):**
   - Renders the `index.html` template.

2. **Process Route (`'/process'`):**
   - Handles both POST and GET requests.
   - Retrieves form data (start year, end year, select city) from the request.
   - Calls the `select_artworks_db` function with the provided parameters.
   - Renders the `process.html` template with the processed data.

### Database Query Function (`select_artworks_db`)

This function connects to a MySQL database hosted at "ec2-18-221-156-42.us-east-2.compute.amazonaws.com" using credentials (`user='root'`, `password='ceit2018'`, `database='Artwork_db'`). It performs a SELECT query to retrieve artwork information based on provided criteria (start year, end year, select city).

The SQL query joins the `Author` and `Artwork` tables and filters the results based on birth years and the selected city. The retrieved data is then printed and returned.

## How to Use

1. Ensure you have Python and Flask installed on your system.
2. Navigate to the `Filter Application Flask/Flask` directory.
3. Run the Flask application using the command: `python app.py`.
4. Open a web browser and go to [http://localhost:5000/](http://localhost:5000/) to access the home page.
5. Fill out the form on the home page and submit it to view filtered artwork information on the process page.

Feel free to explore and modify the code according to your requirements. Ensure that you have the required MySQL database accessible with the provided credentials.

Happy filtering!
