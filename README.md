Mentoring-Match-App
===================

Matches students to students in order to facilitate learning.

Requirements:
- Python 2.7
- MySQL 5+
- Django 1.4

Setup:
- Set up Python, Django, MySQL (see internet for details)
- Check out repo
- Run setup/dev-setup.sh (creates the database and user on the MySQL side, syncs the django application to the database, autocreates the superuser)

Some notes:
- If you want to wipe all user data, run setup/dev-teardown.sh.
- Options for dev-setup and dev-teardown can be seen with [script] -h.
- Contact Dorrene Brown (deb3323@rit.edu) for the mentoring superuser password if the mentoring superuser is autogenerated.

Styling
- CSS styles for the site use [Compass][1], a Ruby gem that both compiles
  [SASS][2] and provides useful mixins and frameworks for building frontends.
  Make sure Ruby is installed (use [RVM][3] on Unix systems), and run `bundle
  install` to make sure the required gems are installed on your system.
- Run `compass watch` in an app's "static/" directory if it contains a
  `config.rb` file, and all of the `.sass` files will compile to `.css`.
  Simply link to the `CSS` files from app templates like normal.
- Both the `.scss` and `.css` files should be checked into the repository -
  [Read this post by Eric Meyer][4] for more information.


[1]: http://compass-style.org
[2]: http://sass-lang.com
[3]: https://rvm.io/
[4]: http://compass-style.org/blog/2011/05/09/compass-django/
