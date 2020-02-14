# ZANK
The Wikipedia for building codes!

## Motivation
This project was made for the purpose of ...

# Learning Outcomes
* 

## Technologies
This project was built with:
* [Python](https://www.python.org/)
* [Django] (https://www.djangoproject.com/) - v2
* [Flask](https://www.fullstackpython.com/flask.html) - v1
* [Jinja2](https://www.fullstackpython.com/jinja2.html)

## How to Use
Visit the live link in order to visit the site and discover full functionality!


## Features
* 

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
Kabsa A - [KabsaA](https://github.com/KabsaA)
Zain Raza - [UPstartDeveloper](https://github.com/UPstartDeveloper)
Vladyslav nykoliuk - [vladyslavnUA](https://github.com/vladyslavnUA)



## Credit
