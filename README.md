## User stories
Welcome to Snapgram, your go-to social media app! Fotogram is a dynamic platform crafted to empower users to share the meaningful moments of their lives.
| Category  | User Action                               | Purpose                                      | API Feature                 |
|-----------|-------------------------------------------|----------------------------------------------|-----------------------------|
| Auth      | Register for an account                   | Gain access to personalizing, sharing, and interacting on the platform        | dj-rest-auth                |
| Posts     |View a list of posts as a visitor          | Browse recent uploads to see what's new                |List/Filter posts          |
| Posts     |View an individual post as a visitor        | SDelve deeper into posts, including comments and likes | Retrieve post            |
| Posts     | Search for posts as a visitor        | Find posts by artist or title    | List/Filter posts           |
| Posts     |Scroll through posts as a visitor  | Enjoy a seamless browsing experience              | List/Filter posts          |
| Posts     |Create, edit, and delete posts as a user            | Correct or hide any mistakes                 | Create, Update, Destroy post |
| Posts     | User - Create a post                      | Share moments, adjust them, or remove them                | Create post                 |
| Posts     | View liked and followed users' posts as a user                  |Revisit favorite moments or catch up on followed profiles            | List/Filter posts           |
| Likes     |Like and unlike posts as a user                      | Show or withdraw appreciation for posts | Create, Destroy like             |
| Comments  | Create, edit, and delete comments as a user                  | Engage with posts, refine or remove comments  | Create, Update, Destroy comment             |
| Profiles  | View and edit profiles as a user                    | Explore user details and update own profile info | Retrieve, Update profile |
| Followers |Follow and unfollow profiles as a user                  | Connect with or disconnect from other users     |Create, Destroy follower             |
| Events    |Create, view, edit, and delete events as a user                   |Organize, explore, modify, or remove upcoming events          | Create, List/Filter, Update, Destroy event               |
| Contacts  | Submit support requests and send feedback as a user            |     Resolve issues and improve platform experience    |Create a Cntact message    |

## Manual Testing: 
| Model      | Endpoint            | Create | Retrieve | Update | Delete | Filter        | Text Search   |
|------------|---------------------|--------|----------|--------|--------|---------------|---------------|
| Users      | users/              | Yes    | Yes      | Yes    | No     | No            | No            |
|            | users/:id/           | Yes    | Yes      | Yes    | No     | No            | No            |
| Profiles   | profiles/           | Yes (signals) | Yes  | Yes    | No     | Following,    | Name          |
|            | profiles/:id/        | Yes (signals) | Yes  | Yes    | No     | Name          |               |
| Followers  | followers/          | Yes    | Yes      | No     | Yes    | No            | No            |
|            | followers/:id/       | Yes    | Yes      | No     | Yes    | No            | No            |
| Likes      | likes/              | Yes    | Yes      | No     | Yes    | No            | No            |
|            | likes/:id/           | Yes    | Yes      | No     | Yes    | No            | No            |
| Comments   | comments/           | Yes    | Yes      | Yes    | Yes    | Post          | No            |
|            | comments/:id/        | Yes    | Yes      | Yes    | Yes    | Post          | No            |
| Posts      | posts/               | Yes    | Yes      | Yes    | Yes    | Profile,      | Title         |
|            | posts/:id/           | Yes    | Yes      | Yes    | Yes    | Liked, Feed   | Title         |
| Events     | events/              | Yes    | Yes      | Yes    | Yes    | No            | Title         |
|            | events/:id/          | Yes    | Yes      | Yes    | Yes    | No            | Title         |
| Contacts   | contacts/            | Yes    | Yes      | Yes    | Yes    | No            | Name          |
|            | contacts/:id/        | Yes    | No      | No    | No    | No            | Name          |



## Database schema.
![Api Diagram - SqlDBM - Google Chrome 2023-12-13 13_29_45](https://github.com/ibrahimjasim/API-Project/assets/127301769/9768d5d5-de79-4ee0-abf3-53a9a06ada0a)
