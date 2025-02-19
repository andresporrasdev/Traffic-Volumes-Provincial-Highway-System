# Traffic Volumes Web Application

## Application Architecture
Developed a web application that reads and visualizes traffic data from the "Traffic Volumes - Provincial Highway System" dataset provided by the Government of Canada. The application processes data from CSV files and displays it in interactive tables and bar charts using the Django framework.

- Utilized Django framework for backend development, following the MVT (Model-View-Template) architecture.
- Integrated Bootstrap for responsive front-end design and Chart.js for dynamic data visualization.
- Wrote custom Python scripts to handle data extraction and processing from CSV files.
- Implemented MySQL as the database to store and manage traffic data.

## MVT Implementation
![Traffic Volumes Web Application](https://raw.githubusercontent.com/andresporrasdev/Traffic-Volumes-Provincial-Highway-System/main/images/readme/Traffic_arquitecture.jpg)

## Flow Design
![Traffic Volumes Web Application](https://raw.githubusercontent.com/andresporrasdev/Traffic-Volumes-Provincial-Highway-System/main/images/readme/Traffic_sequence.jpg)

- When the app starts, it processes the data from the CSV file, which is read using a utility (e.g., readCSV.py).
- After reading data from the CSV file, it stores it in the MySQL database.
- This data is converted into a suitable format and passed to Django views.
- From the views, the data is then sent as JSON to the frontend, where Chart.js renders it in various chart types such as bar charts or line charts.

## Key Features
- **Reload Data**: Refreshes the data currently in memory.
- **Persist Data**: Saves the current data in memory to a CSV file.
- **Add New Record**: Redirects to a form for adding new rows to the database.
- **Delete Selected**: Deletes the rows selected via checkboxes.
- **Display Selected**: Shows only the selected rows on a new page.
- **Edit**: Each row has an edit link to modify the selected item via a prefilled form.
- **CSV Reload**: Reload data from the CSV file into the MySQL database.
- **CSV Persist**: Store data in a new CSV file using the "Persist Data" button.
- **Data Visualization**: Display data using Chart.js by passing data as JSON and rendering it in a bar chart.

## Front-end (Presentation Layer)
![Traffic Volumes Web Application](https://raw.githubusercontent.com/andresporrasdev/Traffic-Volumes-Provincial-Highway-System/main/images/readme/traffic4.jpg)

The presentation layer uses Django templates to render data:
- **Django Framework**: Handles the display of data using HTML templates.
- **Templates**: Define the layout and structure of web pages.
  - `traffic_data.html`: Displays traffic data in a tabular format or as a bar chart using Chart.js.

## Business Logic Layer
![Traffic Volumes Web Application](https://raw.githubusercontent.com/andresporrasdev/Traffic-Volumes-Provincial-Highway-System/main/images/readme/Traffic1.jpg)

- **Utils**:
  - `readCSV.py`: Reads the CSV file and converts the data into a format usable by Django. It creates a list of DTO (Data Transfer Object) objects.
- **Model**:
  - Defines data models using Django’s `models.Model`. The `TrafficData` model is used to create and manage tables in the database.
- **Views**:
  - Contains view functions that handle user requests, process data, and return responses. View functions call `readCSV` to get traffic data and pass it to templates for rendering.

## Data Source
![Traffic Volumes Web Application](https://raw.githubusercontent.com/andresporrasdev/Traffic-Volumes-Provincial-Highway-System/main/images/readme/traffic2.jpg)

- **CSV File**: `Traffic_Volumes_-_Provincial_Highway_System.csv`
- **MySQL Database**: Stores data in memory using Django Framework.
- **Open Government Portal**: The dataset is sourced from [Traffic Volumes - Provincial Highway System](https://open.canada.ca/data/en/dataset/b5b01346-6a3f-a523-9f52-c61a52791356) on the Government of Canada website.
- **License**: [Open Government License - Canada](https://novascotia.ca/opendata/licence.asp)
