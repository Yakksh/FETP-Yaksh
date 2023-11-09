# Flask Google Sign-in

This is a simple Flask application that demonstrates Google sign-in functionality.

## Setup

### Prerequisites

Make sure you have Python and pip installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Yakksh/FETP-Yaksh.git
   ```

2. Navigate to the project directory:

   ```bash
   cd FETP-Yaksh
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up a Google API project and obtain the client ID and client secret.

2. Replace the placeholders in `app.py` with your Google client ID and client secret.

3. Run the application:

   ```bash
   python -u app.py
   ```

4. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
