
# NewsPortal

A full-featured **Django-based News Portal** with trending news, featured stories, weekly top news, breaking news, categories, tags, search functionality, and newsletter subscriptions.

---

## Features

* Home page with **Featured Story**, **Trending News**, **Weekly Top News**, and **Breaking News Ticker**.
* **Latest News** page with pagination.
* Category and tag-based post filtering.
* **Search bar** to search posts by title or content.
* Sidebar widgets: Most Popular posts, Advertisement, and Newsletter subscription.
* Post detail pages with full content, author, and published date.
* **Admin panel** for managing posts, categories, tags, advertisements, comments, and newsletters.
* Responsive design with **Bootstrap 5** and optional dark mode.
* AJAX-powered newsletter subscription form.

---

## Technologies

* **Backend:** Django 5.x, Python 3.13
* **Frontend:** HTML5, CSS3, Bootstrap 5, jQuery
* **Database:** SQLite (default)
* **Rich Text Editor:** django-summernote

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/newsportal.git
cd newsportal
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## Project Structure

```
newsportal/
├── newspaper/
│   ├── templates/newsportal/
│   │   ├── home/
│   │   ├── list/
│   │   ├── base.html
│   │   └── nav.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── manage.py
└── requirements.txt
```

---

## Admin Panel

* Accessible at `/admin/`.
* Manage **Posts**, **Categories**, **Tags**, **Advertisements**, **Comments**, and **Newsletters**.
* Use **django-summernote** to add rich-text content for posts.

---

## Search

* URL: `/search/?query=<search-term>`
* Searches **title** and **content** of active posts with published date.
* Pagination supported.

---

## Newsletter

* Users can subscribe via the sidebar form.
* AJAX-powered submission shows success or failure messages instantly.
* Emails are stored in the `Newsletter` model.

---

## License

MIT License.

