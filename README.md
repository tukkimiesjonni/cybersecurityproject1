# Threddit

This repository is made as a project for a University of Helsinki course. I am trying to recreate the functionality of Reddit and make a simplistic website with said functionality. Anonymously browsing users will be able to view threads and their comments. Registered users will be able to create new threads, comment on threads and up- or downvote threads.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Progress](#progress)

## Installation

Insert instructions on how to install and set up the project here.

## Usage

I am assuming that users of this program have downloaded PostgreSQL using the provided installation script. Therefore:

Start a database in your home directory with inputting `start-pg.sh`. Make sure to keep the script running.

Open a new window in your terminal and input `createdb dbname`. After this you will e able to open a connection to that database from you homedirectory by typin `psql`. There you can execute SQL commands. Start by executing the `schema.sql` file there.

After the schema is executed, you will be able to run the flask program in the project directory terminal using `flask run`.

## Contributing

Jonni Tukkimies

## License

Insert license here.

## Progress

Currently, I have managed to make almost all of the necessary templates and static css files in order for the project to work. In terms of functionality, users are able to register, sign in and sign out from the website. Users will also be able to create new threads but they are yet to be displayed on the site.

