# Library REST API
This project is a simple example of how to process queries on two database instances.
The main application of this project is library, where we have only two models: `book` and `reader`.
Application made as a django rest service and have endpoints:
- Export  all data
```
http://0.0.0.0/api/v1/export_all_data/
```
- View info about reader by id
```
http://0.0.0.0/api/v1/get_reader_info/{id}/
```
## Getting Started
### Prerequisites
To run this project you need to install `docker`, `git`, and `docker-compose` on your local machine.
Clone the project:
```bash
git clone https://github.com/86Ilya/Library
```
### Run application
This application configured to run on 80 port. So you need the root privilegies.
Execute the following commands in the project folder to run the application:
```bash
cp env_example .env
sudo ./deploy.sh
```
## Running the tests
To run the automated tests execute the following command:
```bash
sudo docker exec -it library_web_1 python manage.py test
```
## Some thoughts about balancing queries
1. Python is not the best tool for balancing short and simple queries, the time of query processing by the interpreter can be much longer than the time of query processing in the database.

2. In this task, I decided not to make a perfect balancing, I made an application where balancing can be easily changed.

3. I don't think we need to check if the database is alive because it's not a pool of redis. If the database is unavailable, it is a system failure.
