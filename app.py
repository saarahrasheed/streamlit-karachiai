import streamlit as st 
import pandas as pd



def main():
    st.title('Air Passengers Analysis')
    
    # read data file 
    data = pd.read_csv('AirPassengers.csv')
    
    # obtain year from date 
    data['Year'] = data['Month'].apply(lambda x: x.split('-')[0])
    
    # show unique years
    year = st.selectbox('Select year', data['Year'].unique())
    
    # button trigger
    button = st.button('Show results')
    if button:
        # if button is pressed, subset data on selected year
        subset = data[data['Year'] == year]
        # show subset table
        st.table(subset)
    
    
    
if __name__ == '__main__':
    main()

    