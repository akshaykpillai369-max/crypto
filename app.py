import streamlit as st
from menu import Menu


def main():

    menu = Menu()

    st.title("Welcome To Real Time Currency Exchange Rates")
    st.write("***ALL CONVERSIONS ARE BASED ON THE EXCHANGE WITH USD***")

    columns = st.columns(3)
    results = menu.api_call()

    for index, (key, value) in enumerate(results.items()):

        with columns[index % 3] :

            with st.container(border= True):
                st.markdown(f"### CURRENCY : {key}")
                st.write(f"**VALUE** : {value}")


if __name__ == '__main__':
    main()
