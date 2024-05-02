# Chordity (Ver. 1.2)
[https://chordity.onrender.com/](https://chordity.onrender.com/)

---

**Welcome to Chordity - a web based chat platform focused around connecting musicians and collaborating together to inspire and kickstart new tracks!**

As of right now, here’s an overview on what I’ve created during the past few months of development, and here’s the general roadmap for what I plan to work on in future releases.

- Ver. 1.0 - Released on 4/2/2024
    - General foundation created primarily using Django Framework.
    - General models developed for rooms, topics, messages, and users.
    - Swapped out default Django user model for custom user model, which includes the ability to add a bio and avatar to your profile. :)
    - Imported custom front-end styling and integrated back-end for dynamic views.
    - Added CRUD pages for profiles, messages, and posts.
    - Added search bar to find different posts or topics.
    - Added navbar for quick access functions.
    - Worked on mobile responsiveness.
    - Created basic Django REST API (no official documentation so far, but it is only equipped with a few different functions at the moment. If running locally, can be found at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) or a similar URL).
    - Currently using SQLite DB architecture, and there are no plans of changing this at this time.
    - Currently using default Django admin console for superusers - also no plans of changing this at this time.
    - CSRF protection added via CSRF tokens on all forms. See this [link](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/web_application_security) for more info on Django security features.
- Ver 1.1 - Released on 5/1/2024
    - Several minor bugs with dynamic rendering and styling have been addressed.
    - Added terms and conditions page, and a link to it on the user registration page.
    - Anonymous user survey page added, can be accessible from the navbar once signed in.
    - Updated color pallete.
    - Restrictions added on Chordity API.
- Ver 1.2 - Released on 5/2/2024
    - Added AWS S3 bucket integration for static files.
    - Upgraded database from MySQL to PostgreSQL.
    - Added environment variables, turned off debugging features, and added security features for production deployment.
    - Deployed website and started metric integration using Render [https://chordity.onrender.com/](https://chordity.onrender.com/).
- Ver 1.3 and beyond - (TBD)
    - Potential identity framework integration.
    - Adding “favorite genre”, “pronouns” and “spotlight link” (links to music profiles, websites, etc.) to custom user model.
    - More development on REST API.
    - Hooktheory chord builder and API integration ([https://www.hooktheory.com/api/trends/docs](https://www.hooktheory.com/api/trends/docs)).
        - Intended to be a separate portion of the website, but I would ideally like to add this to the posts/profiles as well.
    - Potential contact email for inquiries.

This application is still in development, but is intended to be the prototype for my final project in my M.S. Computer Information Systems and Business Analytics Capstone Course (MS CISBA). If you have any questions or inquiries about this application, please feel free to email me at [herndonrex1@gmail.com](mailto:herndonrex1@gmail.com).

I’m looking forward to showing off more progress as I continue developing this application!

Best,

Rex A. Herndon

West Texas A&M University
