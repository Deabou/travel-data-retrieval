# travel-data-retrieval

This repository is dedicated to a Flask-based web API project that retrieves travel data from the Expedia API. The retrieved data is initially stored in an S3 bucket and then accessed by the web application as an intermediary for user interaction.

## Project Structure

The project is structured as follows:

- **api**: Contains modules for interacting with the Expedia API.
- **web_app**: Includes files for the Flask-based web application.
- **s3_interaction**: Manages interactions with the S3 bucket for storing and retrieving travel data.

## Usage

To use the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/travel-data-retrieval.git
   ```

2. Navigate to the project directory:

   ```bash
   cd travel-data-retrieval
   ```

3. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

4. Run the Flask web application:

   ```bash
   poetry run flask run
   ```

## License

This project is licensed under the **Apache License 2.0**.

## Contributing

Contributions to the project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and ensure tests pass.
4. Push your changes to your fork.
5. Submit a pull request detailing the changes you've made.

## Roadmap

The project is currently under development. Here's a roadmap of planned features:

- Implement data retrieval from Expedia API.
- Store retrieved data in S3 bucket.
- Develop Flask-based web API for interacting with the data.
- Enhance security features for handling sensitive data.
- Implement user authentication and authorization.

## Support

For questions, issues, or feature requests, please contact [Bourgeo282@gmail.com](mailto:Bourgeo282@gmail.com).

---

Stay tuned for updates as Lavendar evolves into a comprehensive spending tracking app! If you have any questions or need further assistance, feel free to reach out.
