# Chordity (Ver. 1.0)

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
- Ver 1.1 and Ver 1.# - TBD
    - Some minor bugs with how some page elements are displayed or how certain pages redirect are still being looked into.
    - Need to add terms of service/use page (and other related pages per Dr. Jennex’s consultation).
    - More features as needed based on consultations with Dr. Zhang and Dr. Sen.
    - Potential identity framework integration.
    - Adding “favorite genre”, “pronouns” and “spotlight link” (links to music profiles, websites, etc.) to custom user model.
    - More development on REST API.
    - Hooktheory chord builder and API integration ([https://www.hooktheory.com/api/trends/docs](https://www.hooktheory.com/api/trends/docs)).
        - Intended to be a separate portion of the website, but I would ideally like to add this to the posts/profiles as well.
    - Acquire official domain and hosting (and potential file storage hosting through AWS or a similar service).
    - Potential contact email for inquiries?

This application is still in development, but is intended to be the prototype for my final project in my M.S. Computer Information Systems and Business Analytics Capstone Course (MS CISBA). If you have any questions or inquiries about this application, please feel free to email me at [herndonrex1@gmail.com](mailto:herndonrex1@gmail.com).

I’m looking forward to showing off more progress as I continue developing this application!

Best,

Rex A. Herndon

West Texas A&M University