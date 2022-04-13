Backend Assessment for Parallel Domains
Clone the repository:
~~~~
git clone https://github.com/sshamsi07/Assessment_ParallelDomains.git
~~~~
At Project's root directory run docker build
~~~
docker build -t app.
~~~
Run app container
~~~
docker run -p 8000:8000 app
~~~
Use Base URL as localhost:8000

**Try the endpoints**:

- Fetch list of all artifacts:
~~~~
http://localhost:8000/artifacts
~~~~
- Fetch single artifact using unique identifier(slug):
~~~~
http://localhost:8000/artifacts/artif_1
http://localhost:8000/artifacts/artif_10
http://localhost:8000/artifacts/artif_7
~~~~
- Fetch all artifact records based on the query parameters:
~~~~
http://localhost:8000/artifacts/?category=quantum&platform=Windows
http://localhost:8000/artifacts/?category=rural&platform=Linux
http://localhost:8000/artifacts/?category=Quantum&platform=Windows
http://localhost:8000/artifacts/?category=Ancient&platform=Windows
~~~~
- Store a new artifact:
~~~
http://localhost:8000/artifacts/create
~~~
- With POST request json body as:
~~~
{
        "slug":"artif_12",
        "category":"urban",
        "platform_used":"Linux"
    
}
~~~

**Error Handling**:

- Check for error in query parameter platform parameter.
~~~~
http://localhost:8000/artifacts/?category=quantum&platform=windows
~~~~
- Check for error in query parameter slug when fetching single artifact.
~~~~
http://localhost:8000/artifacts/artif_100
~~~~

**Testing the API:**

To run the tests, navigate to the root folder of the project.
~~~~
python manage.py test
~~~~




