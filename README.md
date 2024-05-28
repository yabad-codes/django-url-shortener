# URL Shortener

## Link Model

- user_id(int, nullable)
- url(url)
- short_url(url)
- title(string)
- description(text)
- image(string)
- views_count(int)
- created_at(date)
- destroyed_at(date)

## Visitor's version

- visitors can short their long url
- store it in local storage
- copy it to clipboard
- url got destroyed after 1 hour

## User's version

- users can short their long url
- store it in a database with their accounts
- copy it to clipboard
- see stats about the views
- url got destroyed after 1 year
