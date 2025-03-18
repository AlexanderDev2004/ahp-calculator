if ! python -c "import fastapi" &> /dev/null
then
    pip install fastapi
fi

if ! python -c "import jinja2" &> /dev/null
then
    pip install jinja2
fi

if ! command -v uvicorn &> /dev/null
then
    pip install uvicorn
fi

uvicorn main:app --host 127.0.0.1 --port 3500 --reload