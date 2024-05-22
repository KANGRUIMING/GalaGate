To activate the program locally, please first type the following command in the terminal:

First, cd into server and create the virtual environment:

```bash
python -m venv venv

venv\bin\activate
```
Second, run the development server:

```bash
cd Backend
pip install flask
pip install -U flask-cors
python3 server.py
```
Third, cd into client and install dependencies:

```bash
npm install
```

Fourth, run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

