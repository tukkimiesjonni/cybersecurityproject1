# Threddit

This repository is made as a project for a University of Helsinki course. I am trying to recreate the functionality of Reddit and make a simplistic website with said functionality. Anonymously browsing users will be able to view threads and their comments. Registered users will be able to create new threads, comment on threads and up- or downvote threads.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Progress](#progress)

## Installation

I am assuming that users of this program have downloaded PostgreSQL using the provided installation script. Therefore:

Start a database in your home directory with executing the script `start-pg.sh`. Make sure to keep the script running.

Open a new window in your terminal and execute `createdb dbname`. After this you will be able to open a connection to that database from you home directory by executing `psql`. There you can execute SQL commands. Start by executing the contents of `schema.sql` file there.

After the schema is executed, you will be able to run the flask program in the project directory terminal using `flask run`.

Now, the website will run locally on your machine and you should be able to test it.

## Usage

Insert info abot the usage here.

## Contributing

Jonni Tukkimies

## License

Insert license here.

## Progress

At this time, the project is at a state, where users can happily create accounts, view and add new threads. Every thread has it's own URL where in the future comments for the specific thread can be viewed and added. I haven't implement any voting system yet. Currently the threads are in wrong order on the home page, but I will fix that.

Future improvements are going to be:
- Sorting of the threads
- Maybe adding different genres like "politics", "technology", "sports" and etc
- Voting system
- Adding the comments

