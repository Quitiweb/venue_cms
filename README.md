# Venue CMS

## Versions used for this project
1) `Python==3.8.10`
2) `Django==4.1.1`
3) `djangorestframework==3.13.1`

## How to install Venue CMS locally
1) Get the app from [GitHub repository](https://github.com/Quitiweb/venue_cms/) or unzip it from the file sent via email
2) From `venue_cms` folder, run `make install` (creates a virtual env)
3) Run `make init_database` (creates the database and admin superuser)
4) Run `make start_django_server` (starts the backend server)

## FlowChart

![img.png](img.png)

## Pending points

- [x] HTML template for `Views/GET` Campaigns, Venues, Faucets, etc.
- [x] Add `New` button
- [x] Create `Add new record` template
- [x] `Add` views and forms
- [x] Add `Actions` column
- [x] Deletes
- [x] Edits
- [x] HTML template for EDITs (or maybe one for each)
- [x] EDIT Forms
- [ ] Administration section
- [ ] Notifications: saving, updating and deleting
- [ ] Error messages: required fields

### Notes

- Material Dashboard revamp:
    - `apps.home.config.py` (I've deleted this. It looks that it works right)
