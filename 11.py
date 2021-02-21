import streamlit as st
import pandas as pd
import numpy as np
import laba1 


def choose_region():
    regions = {'Vinnytsia':1, 'Volyn':2, 'Dnipropetrovsk':3,'Donetsk':4,'Zhytomyr':5,
          'Transcarpathian':6, 'Zaporozhye':7, 'Ivano-Frankivsk':8, 
         'Kyiv':9, 'Kirovograd':10, 'Luhansk':11, 'Lviv':12, 
         'Mykolayivs':13, 'Odessa':14, 'Poltava':15, 'Rivne':16, 
         'Sumy':17, 'Ternopil':18, 'Kharkiv':19, 'Kherson':20,
         'Khmelnytsky':21,'Cherkasy':22,'Chernivtsi':23,
           'Chernihiv':24,'Crimea':25}
    regions_name = list(regions.keys())  

    region = st.selectbox('Choose a region: ', regions_name )

    index = regions.get(region)

   # df = laba1.list1[index]
    return region, index


def choose_weeks():
    begin = st.number_input('Choose begin of weeks:', value = 1, min_value = 1, max_value  = 52)
    end = st.number_input('Choose end of weeks:', value = 1, min_value = 1, max_value  = 52)
   
    return begin, end

def choose_option():
  
    templist = ['VCI', 'TCI', 'VHI']

    option = st.selectbox('Which do you want to see?',templist)
    'You selected: ', option
  

    return option   

def choose_year():
    year = st.number_input('Choose year:', value = 1981, min_value = 1981, max_value  = 2020)
    return str(year)

    
def choose_years():
    begin = st.number_input('Choose begin of years:', value = 1981, min_value = 1981, max_value  = 2020)
    end = st.number_input('Choose end of years:', value = 1981, min_value = begin, max_value  = 2020)
    
    return str(begin), str(end)
    
    
    
   
def main():
    page = st.sidebar.selectbox("Choose a page", ["Tables", "Line charts", 'Bar Charts']) 
    if page == "Tables":
        region, index = choose_region()
        df = laba1.list1[index]
        begin, end = choose_weeks()
        df_weeks = df[df.Week.between(begin,end)]
        option = choose_option()
       
        new_df = df_weeks[['Year', 'Week', option]]
                # write dataframe to screen
        'Region: ', region
        st.write(new_df)
   
    elif page == "Line charts":
        import plotly_express as px
        region, index = choose_region()
        df1 = laba1.list1[index]
        year = choose_year()
        df1 = df1.loc[df1['Year'] == year] 
        option = choose_option()
        df_years= df1.loc[df1[option] !=-1] 
        new_df = df_years[['Year', 'Week', option]]
        st.write(new_df)
        fig = px.line(new_df, x ='Week',y= option)
        st.plotly_chart(fig)
    elif page == "Bar Charts":
        import matplotlib.pyplot as plt
        import altair as alt
        pd.plotting.register_matplotlib_converters()
        import seaborn as sns
        region, index = choose_region()
        df1 = laba1.list1[index]
        begin, end = choose_years()
        df_years = df1[df1.Year.between(begin,end)]
        option = choose_option()
        df_years= df_years.loc[df_years[option] !=-1] 
        #new_df = df_years[['Year', columns = option]]
        
        #chart_data = df_years((end, begin),
       # columns=[option])
        
        st.write(alt.Chart(df_years).mark_bar().encode(
        x=alt.X('Year', sort=None),
        y=option,))

        #st.bar_chart(chart_data)
        
        #a = sns.barplot(x=new_df['Year'], y=new_df[option]) 
        #st.bar_chart(new_df) 
       

if __name__ == "__main__":
    main()
