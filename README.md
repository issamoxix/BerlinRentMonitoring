# BerlinRentMonitoring
This code runs a program that crawls data from two websites, eBay and Wg-Gesucht, at the same time using separate threads. Before starting the crawling process, it sends an email notification to the user about the start time. The program waits for both threads to finish before ending. The purpose of this code is to automate the process of collecting data from these websites and provide the user with a notification when the process starts.
## Installation

Install project requirements using pip :

```
pip install -r requirements.txt
```

## Configuration

The application requires a secrets file to function properly. Please create a secrets.json file in the root directory of the project and set the required credentials. Here is an example of what the secrets.json file should look like:

```json
{
  "sender": {
    "email": "sender@example.com",
    "password": "senderpassword"
  },
  "recipient": {
    "email": "recipient@example.com"
  },
  "server": {
    "smtp_server": "smtp.example.com",
    "port": 587
  }
}
```
Note: You must set the credentials in the secrets.json file before running the application.

## Usage

To run the application, navigate to the project directory and run the following command:


```bash 
python main.py
```

This will start the application and perform the scraping