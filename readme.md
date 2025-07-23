# Segstream Blog API

This Django REST API provides endpoints to manage and query blog topics, blog posts, and authors. It supports advanced filtering and aggregation features, such as searching topics by title, filtering blog posts by author or topic, and retrieving the top authors for each topic.

## Features

- **List and retrieve blog topics and blog posts**
- **Filter topics by title (case-insensitive, partial match)**
- **Filter blog posts by title, author, or topic (case-insensitive, partial match)**
- **For each topic, view the top 3 authors (by number of blog posts written for that topic)**
- **For each blog post, view other topics written by different authors**
- **Browsable API root for easy navigation**

## API Endpoints

| Endpoint                       | Method | Description                                             | Filters/Query Params Example         |
|---------------------------------|--------|---------------------------------------------------------|--------------------------------------|
| `/topics/`                     | GET    | List all topics with top 3 authors for each topic       | `?title=keyword`                     |
| `/topics/<int:pk>/`            | GET    | Retrieve a specific topic                               |                                      |
| `/blogposts/`                  | GET    | List all blog posts                                     | `?title=web&author=alice&topic=django`|
| `/blogposts/<int:pk>/`         | GET    | Retrieve a specific blog post                           |                                      |
| `/api/`                        | GET    | API root overview                                       |                                      |

## Example Filters

- **/topics/**  
  - `title`: Filter topics by keyword in the title (case-insensitive, partial match).

- **/blogposts/**  
  - `title`: Filter blog posts by keyword in the title.
  - `author`: Filter blog posts by author name.
  - `topic`: Filter blog posts by topic title.

## Example Requests

- List all topics containing "django" in the title:

GET /topics/?title=django

- List all blog posts with "web" in the title, by author "alice", and related to the "django" topic:

GET /blogposts/?title=web&author=alice&topic=django