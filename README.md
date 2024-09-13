<h1>Traffic Volumes Web Application</h1>
<h2>Application Architecture</h2>
<p>This application follows the MVC (Model-View-Controller) pattern using the Django framework with Bootstrap for presentation. The backend processes data from the Traffic Volumes - Provincial Highway System dataset provided by the Government of Canada. Here’s an overview of its key components and functionalities:</p>
<ul>
    <li><strong>Backend</strong>: Written in Python using Django, which follows the MVT (Model-View-Template) pattern.</li>
    <li><strong>Database</strong>: MySQL is used to store the data.</li>
    <li><strong>Frontend</strong>: Bootstrap is used for layout and presentation, while Chart.js is used for displaying data in bar charts.</li>
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
<ul>
    <li><strong>CSV File</strong>: <code>Traffic_Volumes_-_Provincial_Highway_System.csv</code></li>
    <li><strong>MySQL Database</strong>: Stores data in memory using Django Framework.</li>
    <li><strong>Open Government Portal</strong>: The dataset is sourced from <a href="https://open.canada.ca/data/en/dataset/b5b01346-6a3f-a523-9f52-c61a52791356">Traffic Volumes - Provincial Highway System</a> on the Government of Canada website.</li>
<li><strong>License</strong>: <a href="https://novascotia.ca/opendata/licence.asp">Open Government License - Canada</a></li>
</ul>
<h2>Setup and Installation</h2>
<ol>
    <li><strong>Clone the Repository</strong>:
        <pre><code>git clone https://github.com/yourusername/your-repository.git</code></pre>
    </li>
    <li><strong>Install Dependencies</strong>:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Configure Database</strong>: Update the <code>DATABASES</code> setting in <code>settings.py</code> with your MySQL database credentials.</li>
    <li><strong>Apply Migrations</strong>:
        <pre><code>python manage.py migrate</code></pre>
    </li>
    <li><strong>Run the Development Server</strong>:
        <pre><code>python manage.py runserver</code></pre>
    </li>
</ol>
<p>For further details, please refer to the <a href="https://docs.djangoproject.com/en/stable/">Django documentation</a> and the <a href="https://getbootstrap.com/docs/5.0/getting-started/introduction/">Bootstrap documentation</a>.</p>
   
      
