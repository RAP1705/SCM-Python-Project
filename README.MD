### Create a Virtual Environment and Activate it
>> python -m venv venv-scm-b3
>> .\venv-scm-b3\scripts\activate
If there is an error message: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

### Install python libraries (Streamlit)
>> pip install streamlit


### Check any installed library
>> pip show streamlit
>> pip list


### Run Streamlit code
>> streamlit run .\home.py


### Install libraries from requirements.txt
>> pip install -r .\requirements.txt
>> the command prompt must be under the (venv-scm-b3)