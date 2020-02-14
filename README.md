# ZANK
The Wikipedia for building codes!

## Motivation
This project was made for the purpose of ...

# Learning Outcomes
* Manage Sprint Planning and Sprint Retrospectives and SCRUM to make progress on a team project and ensure the highest chances of success
* Utilize advanced Git, Github and Unix Utilities to streamline their coding effectiveness
* Navigate dynamics of professional teams including conflict, delegation, prioritization, difficult conversations, expectation setting, defining roles and responsibilities
* Deliver a professional investor pitch for a product, articulating evidence of product-market fit, team competency, and product fidelity


## Technologies
This project was built with:
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/) - v2
* [Flask](https://www.fullstackpython.com/flask.html) - v1
* [Jinja2](https://www.fullstackpython.com/jinja2.html)
* [AWS](https://aws.amazon.com/)


## How to Use
Visit the live link in order to visit the site and discover full functionality!


## Features
* Search functionality for building codes!


## Code Snippet
```
@app.route("/search", methods=['POST'])
def search_codes():
    query = request.get("title")
    result = codes.find_one('title', query)
    code_id = result.get('_id')

    return redirect(url_for('show_code', code_id=code_id))
```

## Contributors 
* **Kabsa A** - [KabsaA](https://github.com/KabsaA)
*Frontend Lead*

* **Zain Raza** - [UPstartDeveloper](https://github.com/UPstartDeveloper)
*Product Manager, SCRUM Master, and Design Lead*

* **Vladyslav Nykoliuk** - [vladyslavnUA](https://github.com/vladyslavnUA)
*Backend Lead*

* **Aleia Knight** - [Robotgyal](https://github.com/robotgyal)
*Gitmaster*


## Credit
