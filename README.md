<h1>Traffic Volumes Web Application</h1>
<h2>Application Architecture</h2>
<p>Developed a web application that reads and visualizes traffic data from the "Traffic Volumes - Provincial Highway System" dataset provided by the Government of Canada. The application processes data from CSV files and displays it in interactive tables and bar charts using the Django framework.
    <ul>
        <li>Utilized Django framework for backend development, following the MVT (Model-View-Template) architecture.</li>
        <li>Integrated Bootstrap for responsive front-end design and Chart.js for dynamic data visualization.</li>
        <li>Wrote custom Python scripts to handle data extraction and processing from CSV files.</li>
        <li>•	Implemented MySQL as the database to store and manage traffic data.</li>
    </ul>
</p>

![Traffic Volumes Web Application](https://github.com/andresporrasdev/Traffic-Volumes-Provincial-Highway-System/blob/main/images/readme/Traffic_arquitecture.jpg)
<ul>
    <li><strong>Frontend</strong>: Bootstrap is used for layout and presentation, while Chart.js is used for displaying data in bar charts.</li>
    <li><strong>Backend</strong>: Written in Python using Django, which follows the MVT (Model-View-Template) pattern.</li>
    <li><strong>Database</strong>: MySQL is used to store the data.</li>
</ul>

![Traffic Volumes Web Application](https://github.com/andresporrasdev/Traffic-Volumes-Provincial-Highway-System/blob/main/images/readme/Traffic_sequence.jpg)

<ul>
    <li>When the app starts, it process the data from the CSV file, which is read using a utility (e.g., readCSV.py).</li>
    <li>After read data from the CSV file, it store it in the MySQL database</li>
    <li>This data is converted into a suitable format and passed to Django views.</li>
    <li>From the views, the data is then sent as JSON to the frontend, where Chart.js renders it in various chart types such as bar charts or line charts</li>
</ul>


<h3>Key Features</h3>
  <ul>
      <li><strong>Reload Data</strong>: Refreshes the data currently in memory.</li>
      <li><strong>Persist Data</strong>: Saves the current data in memory to a CSV file.</li>
      <li><strong>Add New Record</strong>: Redirects to a form for adding new rows to the database.</li>
      <li><strong>Delete Selected</strong>: Deletes the rows selected via checkboxes.</li>
      <li><strong>Display Selected</strong>: Shows only the selected rows on a new page.</li>
      <li><strong>Edit</strong>: Each row has an edit link to modify the selected item via a prefilled form.</li>
      <li><strong>CSV Reload</strong>: Reload data from the CSV file into the MySQL database.</li>
      <li><strong>CSV Persist</strong>: Store data in a new CSV file using the "Persist Data" button.</li>
      <li><strong>Data Visualization</strong>: Display data using Chart.js by passing data as JSON and rendering it in a bar chart.</li>
  </ul>
<h2>Front-end (Presentation Layer)</h2>

![Traffic Volumes Web Application](https://github.com/andresporrasdev/Traffic-Volumes-Provincial-Highway-System/blob/main/images/readme/traffic4.jpg)

<p>The presentation layer uses Django templates to render data:</p>
<ul>
    <li><strong>Django Framework</strong>: Handles the display of data using HTML templates.</li>
    <li><strong>Templates</strong>: Define the layout and structure of web pages.
        <ul>
            <li><code>traffic_data.html</code>: Displays traffic data in a tabular format or as a bar chart using Chart.js.</li>
        </ul>
    </li>
</ul>
<h2>Business Logic Layer</h2>

![Traffic Volumes Web Application](https://github.com/andresporrasdev/Traffic-Volumes-Provincial-Highway-System/blob/main/images/readme/Traffic1.jpg)

<ul>
    <li><strong>Utils</strong>:
        <ul>
            <li><code>readCSV.py</code>: Reads the CSV file and converts the data into a format usable by Django. It creates a list of DTO (Data Transfer Object) objects.</li>
        </ul>
    </li>
    <li><strong>Model</strong>:
        <ul>
            <li>Defines data models using Django’s <code>models.Model</code>. The <code>TrafficData</code> model is used to create and manage tables in the database.</li>
        </ul>
    </li>
    <li><strong>Views</strong>:
        <ul>
    <li>Contains view functions that handle user requests, process data, and return responses. View functions call <code>readCSV</code> to get traffic data and pass it to templates for rendering.</li>
        </ul>
            </li>
</ul>
<h2>Data Source</h2>

![Traffic Volumes Web Application](https://github.com/andresporrasdev/Traffic-Volumes-Provincial-Highway-System/blob/main/images/readme/traffic2.jpg)

<ul>
    <li><strong>CSV File</strong>: <code>Traffic_Volumes_-_Provincial_Highway_System.csv</code></li>
    <li><strong>MySQL Database</strong>: Stores data in memory using Django Framework.</li>
    <li><strong>Open Government Portal</strong>: The dataset is sourced from <a href="https://open.canada.ca/data/en/dataset/b5b01346-6a3f-a523-9f52-c61a52791356">Traffic Volumes - Provincial Highway System</a> on the Government of Canada website.</li>
<li><strong>License</strong>: <a href="https://novascotia.ca/opendata/licence.asp">Open Government License - Canada</a></li>
</ul>
