# Gist

**A quiet space for sharing thoughts, ideas, observations and opinions.**

Gist is a Django-powered web application for publishing short written posts and having thoughtful conversations around them. The project is being developed with a deliberately simple, writing-first experience: the focus should stay on what people share, not on follower counts, public popularity or social-media noise.

> **Project status:** In active development. This repository describes the current implementation and the intended V1 direction separately. It is not yet ready for production deployment.

## Product direction

The agreed Gist V1 experience is guided by a few principles:

- **Pseudonymous public identity:** people use account usernames publicly. Real names and unnecessary personal details should not be part of the public experience by default.
- **Reading comes first:** visitors should be able to discover and read public Gists without creating an account.
- **Featured, then latest:** the landing page and feed should introduce a curated selection of featured Gists, followed by the newest posts in chronological order.
- **Thoughts over metrics:** engagement should support conversation, not turn the product into a popularity contest.
- **Simple participation:** publishing and interacting should be straightforward, with clear ownership and moderation rules.

Pseudonymous does not mean completely anonymous or untraceable. Gist will retain internal account records so that users can manage their content and the application can enforce security and moderation policies.

## Current implementation

The repository currently contains:

- A Django project with separate `accounts`, `pages` and `gists` applications.
- A custom Django user model.
- Account registration and login routes.
- Gist creation, listing, detail, update and delete views.
- Author ownership checks for editing and deleting Gists.
- A Gist comment model and comment-creation view.
- Like, dislike and repost relationships in the data model.
- Django Admin registration for Gists and comments.
- SQLite as the configured development database.
- Bootstrap-based templates and django-crispy-forms integration.

Some V1 product decisions are not implemented yet. In particular, the landing page still needs its featured-content and latest-content sections; public browsing needs to be completed (the current Gist detail view requires login); and like, dislike and repost actions still need their user-facing workflows. The existence of relationship fields in the database does not mean those interactions are complete.

## Planned V1 experience

The planned user journey is:

1. **Landing page:** explain Gist, show administrator-curated featured posts, then show the latest Gists.
2. **Explore:** browse public Gists in chronological order, with pagination.
3. **Gist detail:** read a complete Gist and its chronological comments.
4. **Publish:** create a Gist with a title and body.
5. **Participate:** comment, like, dislike or repost, subject to authentication and clear interaction rules.
6. **Manage contributions:** edit or delete your own Gists and view your contributions.
7. **Account access:** register, sign in, sign out and recover account access.

For V1, comments are intended to support creation, chronological display and deletion by their author or moderation by an administrator. Comment editing is not planned for V1.

Featured Gists are intended to be selected by administrators rather than ranked automatically by likes or other engagement metrics.

## Technology

- **Backend:** Python and Django
- **Database:** SQLite for local development; PostgreSQL support is planned for deployment
- **Frontend:** Django templates, HTML, CSS, Bootstrap
- **Forms:** django-crispy-forms with crispy-bootstrap5
- **Administration:** Django Admin

The project settings currently identify Django 6.1.1. A pinned dependency manifest and a documented supported Python version still need to be added; the install command below reflects the dependencies currently evident in the project configuration.

## Getting started

### Prerequisites

- Python installed and available on your command line
- Git
- A terminal (PowerShell on Windows, or your preferred shell on macOS/Linux)

### 1. Clone the repository

```bash
git clone https://github.com/SamuelNiiOdoiOddoye/Gist.git
cd Gist
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the current application dependencies

```bash
python -m pip install --upgrade pip
python -m pip install "Django==6.1.1" django-crispy-forms crispy-bootstrap5
```

A committed, fully pinned dependency file should replace this manual installation step as part of the project’s setup and release-readiness work.

### 4. Apply database migrations

```bash
python manage.py migrate
```

The current configuration uses SQLite and creates the local database file when migrations are applied.

### 5. Create an administrator account

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

The Django development server is intended for local development only. It must not be used as the production web server.

## Main application routes

| Route | Purpose |
| --- | --- |
| `/` | Homepage |
| `/gists/` | Gist listing |
| `/gists/gist/<id>/` | Gist detail |
| `/gists/gist/new/` | Create a Gist |
| `/accounts/signup/` | Register |
| `/accounts/login/` | Sign in |
| `/admin/` | Django administration |

Some routes require authentication. The access rules and public-reading experience are being refined as part of V1.

## Project structure

```text
Gist/
├── accounts/          # Custom user model, registration and account views
├── django_project/    # Django project settings and root URL configuration
├── gists/             # Gist and comment models, forms, views and admin
├── pages/             # Homepage views and page routes
├── templates/         # Shared, account and Gist templates
├── manage.py
└── README.md
```

## Development and contribution

Gist is being developed incrementally. Before contributing, please:

1. Read the product direction and current implementation notes above.
2. Keep changes focused and consistent with the writing-first V1 experience.
3. Avoid introducing unnecessary social-network features or public popularity mechanics.
4. Add or update tests when changing behaviour, permissions or data relationships.
5. Do not commit secrets, local databases, personal data or production credentials.

Manual testing and feedback are part of the development process. See the project contributors and acknowledgements below.

## Security and deployment status

**Do not deploy the current configuration as-is to a public production environment.**

The repository still needs a production security pass. In particular:

- The current settings file contains a development secret key and has `DEBUG = True`.
- Production settings, environment-based secrets, allowed hosts, HTTPS and secure cookie settings are not yet configured.
- The current password-reset preview flow must be replaced with a secure, standard password-reset process before public deployment. Reset tokens must never be displayed to the person requesting a reset.
- A production email backend, static-file strategy, PostgreSQL configuration, logging, backups and deployment instructions still need to be completed.
- Automated tests and CI checks need to be expanded to protect authentication, permissions, publishing, comments and engagement workflows.

Use only disposable local development data while these items remain unresolved.

## Contributors and acknowledgements

- **Samuel Nii Odoi Oddoye** — Project owner and developer.
- **Rowena Serwaah Danquah** ([@DSRowena](https://github.com/DSRowena)) — Manual QA testing and feedback.

## Licensing

No `LICENSE` file is currently included in this repository. Until a licence is added, do not assume that the code may be reused, modified, redistributed or commercially exploited. Please contact the repository owner for permission.

---

Gist is being built around a simple idea: **make the thought more important than the person sharing it.**
