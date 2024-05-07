# The Snapgram-API
Welcome to Snapgram, your go-to social media app! Fotogram is a dynamic platform crafted to empower users to share the meaningful moments of their lives.
## Table of Contents 
- [User Stories](#user-stories)
- [Testing](#testing)
- [Database Schema](#database-schema)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)
### User stories
*  Backednd User storys can be found [Here](https://github.com/users/ibrahimjasim/projects/17)

* Welcome to Snapgram, your go-to social media app! Fotogram is a dynamic platform crafted to empower users to share the meaningful moments of their lives.
  
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

## Testing:
### Validator Testing
| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** |
| ----------------------------- | ----------------------- | --------------------------- | ---------- |
| drf_API settings.py | PEP8 validator |No issues found| ✅ |
| drf_API urls.py | PEP8 validator |No issues found| ✅ |
| drf_API views.py | PEP8 validator |No issues found| ✅ |
| drf_API serializers.py | PEP8 validator |No issues found| ✅ |
| Events serializers.py | PEP8 validator |No issues found| ✅ |
| Events models.py | PEP8 validator |No issues found| ✅ |
| Events urls.py | PEP8 validator |No issues found| ✅ |
| Events views.py | PEP8 validator |No issues found| ✅ |
| Posts serializers.py | PEP8 validator |No issues found| ✅ |
| Posts models.py | PEP8 validator |No issues found| ✅ |
| Posts urls.py | PEP8 validator |No issues found| ✅ |
| Posts views.py | PEP8 validator |No issues found| ✅ |
| Likes serializers.py | PEP8 validator |No issues found| ✅ |
| Likes models.py | PEP8 validator |No issues found| ✅ |
| Likes urls.py | PEP8 validator |No issues found| ✅ |
| Likes views.py | PEP8 validator |No issues found| ✅ |
| Followers serializers.py | PEP8 validator |No issues found| ✅ |
| Followers models.py | PEP8 validator |No issues found| ✅ |
| Followers urls.py | PEP8 validator |No issues found| ✅ |
| Followers views.py | PEP8 validator |No issues found| ✅ |
| Profiles serializers.py | PEP8 validator |No issues found| ✅ |
| Profiles models.py | PEP8 validator |No issues found| ✅ |
| Profiles urls.py | PEP8 validator |No issues found| ✅ |
| Profiles views.py | PEP8 validator |No issues found| ✅ |
| Comments serializers.py | PEP8 validator |No issues found| ✅ |
| Comments models.py | PEP8 validator |No issues found| ✅ |
| Comments urls.py | PEP8 validator |No issues found| ✅ |
| Comments views.py | PEP8 validator |No issues found| ✅ |
| Contacts serializers.py | PEP8 validator |No issues found| ✅ |
| Contacts models.py | PEP8 validator |No issues found| ✅ |
| Contacts views.py | PEP8 validator |No issues found| ✅ |
| Contacts urls.py | PEP8 validator |No issues found| ✅ |






### Manual Testing
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



## Database schema
![Api Diagram - SqlDBM - Google Chrome 2023-12-13 13_29_45](https://github.com/ibrahimjasim/API-Project/assets/127301769/9768d5d5-de79-4ee0-abf3-53a9a06ada0a)

## Unfixed Bugs
* None so far.

## Technologies Used:
### Main Languages Used:
* Python

## Frameworks, Libraries & Programs Used:
* Django
* Django RestFramework
* Cloudinary
* Heroku
* Pillow
* Django Rest Auth
* PostgreSQL

## Deployment:
### Project creation:
1. Create the GitHub repository.
2. Create the project app on [Heroku.](https://dashboard.heroku.com/apps/snapgram-api/deploy/github).
3. Add the Postgres package to the Heroku app via the Resources tab.
4. Once the GitHub repository was launched on GitPod, installed the following packages using the `pip install` command:
```
'django<4'
dj3-cloudinary-storage
Pillow
djangorestframework
django-filter
dj-rest-auth
'dj-rest-auth[with_social]'
djangorestframework-simplejwt
dj_database_url psycopg2
gunicorn
django-cors-headers
```
5. Created the Django project with the following command:
```
django-admin startproject project_name .
```
6. Navigated back to [Heroku](heroku.com), and under the Settings tab, added the following configvars:
 - Key: SECRET_KEY | Value: hidden
 - Key: CLOUDINARY_URL | Value: cloudinary://hidden
 - Key: DISABLE_COLLECTSTATIC | Value: 1
 - Key: ALLOWED_HOST | Value: snapgram-api-df7c5b682dbd.herokuapp.com
7. Add two additional configvars once the ReactApp has been created:
 - Key: CLIENT_ORIGIN | Value: [https://react-app-name.herokuapp.com](https://snapgram-pp5-8d26d1fb4bb6.herokuapp.com)
 - Key: CLIENT_ORIGIN_DEV | Value: [https://gitpod-browser-link.ws-eu54.gitpod.io](https://3000-ibrahimjasi-snapgrampp5-i0nap7nt34w.ws-eu112.gitpod.io/)
  - Check that the trailing slash `\` at the end of both links has been removed.
8. Created the env.py file, and added the following variables. The value for DATABASE_URL was obtained from the Heroku configvars in the previous step:
```
import os

os.environ['CLOUDINARY_URL'] = 'cloudinary://hidden'
os.environ['DEV'] = '1'
os.environ['SECRET_KEY'] = 'hidden'
os.environ['DATABASE_URL'] = 'postgres://hidden'
```
### In settings.py: 
9. Add the following to INSTALLED_APPS to support the newly installed packages:
```
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
'rest_framework',
'django_filters',
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
'corsheaders',
```
10. Import the database, the regular expression module & the env.py
```
import dj_database_url
import re
import os
if os.path.exists('env.py')
    import env
```
11. Below the import statements, add the following variable for Cloudinary:
```
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'
```
 - Below INSTALLED_APPS, set site ID:

```
SITE_ID = 1
```
11. Below the import statements, add the following variable for Cloudinary:
```
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'
```
- Below INSTALLED_APPS, set site ID:
```
SITE_ID = 1
```
12. Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
```
13. Set the default renderer to JSON:
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
14. Beneath that, added the following:
```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```
15. Then added:
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
```
16. Updated DEBUG variable to:
```
DEBUG = 'DEV' in os.environ
```
17. Updated the DATABASES variable to:
```
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}
```
18. Added the Heroku app to the ALLOWED_HOSTS variable:
```
os.environ.get('ALLOWED_HOST'),
'localhost',
```
19. Below ALLOWED_HOST, added the CORS_ALLOWED variable as shown in [DRF-API walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/a6250c9e9b284dbf99e53ac8e8b68d3e/0c9a4768eea44c38b06d6474ad21cf75/?child=first):
```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
20. Also added to the top of MIDDLEWARE:
```
'corsheaders.middleware.CorsMiddleware',
```
### Final requirements:
21. Created a Procfile, & added the following two lines:
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi
```
22. Migrated the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
23. Froze requirements:
```
pip3 freeze --local > requirements.txt
```
24. Added, committed & pushed the changes to GitHub
25. Navigated back to heroku, and under the ‘Deploy’ tab, connect the GitHub repository.
26. Deployed the branch.

 ## CREDITS:

### Content:
- The creation of this API database was provided through the step by step guide of the C.I. DRF-API walkthrough project.
