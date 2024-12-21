# Inventory App

#### The Inventory App is a Python-based console application that allows users to manage users, products, and categories in a simple inventory database. The app uses SQLite as its database and organizes functionality into different modules for easy maintainability.

#### By **Yakubu Esuza**


## Features

- **User Management**: Add, delete, view, and search for users.
- **Product Management**: Add, delete, view, and search for products.
- **Category Management**: Add, delete, view, and search for categories.


## How to Use

### Requirements

- Python 3.8 or higher
- Pipenv (for managing dependencies)
- SQLite (built into Python)

#### Installation Process

1. Clone this repository using:


   ```bash
   git@github.com:Esuza-arch/inventory-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd inventory-app
   ```

3. Install the required dependencies:

Install the required dependencies. If no dependencies are specified in the project, ensure you have Python's sqlite3 module available, as it is built-in for most installations.
   ```bash
   Pipenv install
   Pipenv install sqlite3
   ```

4. Verify the project structure:

Ensure the directory structure looks like this:
inventory-management-system/
- |── app.py
- |── lib/
-    |── db/
-    |   ── database.py
-    |── models/
--        ── user.py
--        ── product.py
--        ── category.py


### Running the application

Set the Working Directory: Ensure you are in the root directory (inventory-management-system) where app.py is located.


Run the Application: Execute the following command in your terminal:

```bash
   python app.py
   ```


Interact with the Application: Follow the on-screen prompts to navigate the menu and manage users, products, and categories.


## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

- Email: <yakubuesuza@gmail.com>

## License

MIT License

Copyright &copy; 2024 Yakubu Esuza

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
