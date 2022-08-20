# Filesystem API Service
- This project is a simple implementation of remote file storage service built using flask.
- In this porject file system of the machine on which this api is hosted will be used to perform the operations listed in the api.

- **API**:
  - Create a file - `/create/<string:file_name>`
  - Delete a file - `/delete/<string:file_name>`
  - Update a file - `/update/<string:file_name>`
  - Get a file - `/file/<string:file_name>`