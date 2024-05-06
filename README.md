## User stories
Welcome to Snapgram, your go-to social media app! Fotogram is a dynamic platform crafted to empower users to share the meaningful moments of their lives.
| Category  | User Action                               | Purpose                                      | API Feature                 |
|-----------|-------------------------------------------|----------------------------------------------|-----------------------------|
| Auth      | Register for an account                   | Have a personal profile with a picture        | dj-rest-auth                |
| Auth      | Register for an account                   | Create, like, and comment on posts           | Create post, Create comment, Create like |
| Auth      | Register for an account                   | Follow users                                 | Create follower             |
| Posts     | Visitor - View a list of posts            | Browse the most recent uploads                | List/Filter posts           |
| Posts     | Visitor - View an individual post         | See user feedback, i.e., likes and read comments | Retrieve post            |
| Posts     | Visitor - Search a list of posts          | Find a post by a specific artist or title    | List/Filter posts           |
| Posts     | Visitor - Scroll through a list of posts  | Browse the site more comfortably              | List/Filter posts           |
| Posts     | User - Edit and delete my post            | Correct or hide any mistakes                 | Update property, Destroy property |
| Posts     | User - Create a post                      | Share my moments with others                 | Create post                 |
| Posts     | User - View liked posts                   | Go back often to my favorite posts            | List/Filter posts           |
| Posts     | User - View followed users' posts         | Keep up with my favorite users' moments      | List/Filter posts           |
| Likes     | User - Like a post                        | Express my interest in someone's shared moment | Create like                |
| Likes     | User - Unlike a post                      | Express that my interest in someone's shared moment has faded away | Destroy like |
| Comments  | User - Create a comment                   | Share my thoughts on other people's content  | Create comment              |
| Comments  | User - Edit and delete my comment         | Correct or hide any mistakes                 | Update comment, Destroy comment |
| Profiles  | User - View a profile                     | See a user's recent posts, followers, following count data | Retrieve profile, List/Filter posts |
| Profiles  | User - Edit a profile                     | Update my profile information                 | Update profile              |
| Followers | User - Follow a profile                   | Express my interest in someone's content     | Create follower             |
| Followers | User - Unfollow a profile                 | Express that my interest in someone's content has faded away and remove their posts from my feed | Destroy follower |
| Events    | User - Create an event                    | Organize and share upcoming events           | Create event                |
| Events    | User - View upcoming events               | Stay informed about upcoming activities      | List/Filter events          |
| Contacts  | User - Submit Support Request              |     Address user queries and technical issues.     | POST /support/contact       |
| Contacts  | User - Send Feedback	              |     Collect user feedback for platform improvement.       | POST /feedback/submit      |
| Contacts  | User - Report Problems              |     Address user queries and technical issues.       | POST /report/issue    |

## Database schema.
![Api Diagram - SqlDBM - Google Chrome 2023-12-13 13_29_45](https://github.com/ibrahimjasim/API-Project/assets/127301769/9768d5d5-de79-4ee0-abf3-53a9a06ada0a)
