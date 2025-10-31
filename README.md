# behave-api-automation

## Installations

- python3.9+: [python3](https://www.python.org/downloads/)
- pycharm IDE: [pycharm](https://www.jetbrains.com/pycharm/download/?section=mac)
- Behave: `pip3 install behave`
- Requests: `pip3 install requests`
- Pydantic: `pip3 install pydantic`
- HTML Reporter: `pip3 install behave-html-formatter`

## CLI
Run All:
```
behave
```

Run Single Feature: `behave {path to feature file}` 
```
behave features/features/create_user_api/create_user_api.feature  
```

Run via Single Tag:
```
behave --tags=users
```

Run via Multi Tags:
```
behave --tags=users --tags=resource
```

Run and change output file location:
```
 behave -f behave_html_formatter:HTMLFormatter -o reports/reporters.html
```


## Docs

- Behave:
    - [Behave](https://behave.readthedocs.io/en/stable/tutorial/)
    - [Behave Intro](https://www.tutorialspoint.com/behave/behave_introduction.htm)
- ReqRes: [ReqRes](https://reqres.in/)
- Requests: [Requests Library](https://requests.readthedocs.io/en/latest/api/#)
- Pydantic:
    - [Pydantic API](https://docs.pydantic.dev/latest/api/base_model/)
    - [Base Model](https://docs.pydantic.dev/latest/concepts/models/)
- Gherkin: [Gherkin](https://cucumber.io/docs/gherkin/reference)






# behave-api-automation
