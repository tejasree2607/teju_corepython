import streamlit as st
st.header("Grades of a student")
p=st.number_input('project score',min_value=0)
i=st.number_input('internal score',min_value=0)
e=st.number_input('external score',min_value=0)

if st.button("total "):
    if (p >=50 and i >=50 and e >=50):
        total = ((70 / p ) * 100) + ((10 / i ) * 100) +((20 / e ) * 100)
        st.info(total)
        if total>=90:
            st.write(' Grade A')
        elif total>80:
            st.write('Grade B')
        else:
            st.write('Grade C')
    else:
        if p<50:
            st.write('failed in project' , p)
        if e<50:
            st.write('failed in eexternal' , e)
        if i<50:
            st.write('failed in internal' , i)