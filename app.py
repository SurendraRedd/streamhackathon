import streamlit as st
from datetime import timedelta
conn = st.experimental_connection('pets_db', type='sql')

# View the connection contents.
conn

with conn.session as s:
    st.markdown(f"Note that `s` is a `{type(s)}`")
    s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    s.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

pet_owners = conn.query('select * from pet_owners', ttl=timedelta(minutes=10))
st.dataframe(pet_owners)