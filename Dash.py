# Filter
import pandas as pd
import streamlit as st

def filter_and_display_data(df, year, education, status):
    filtered_df = df[(df['Year_Birth'] == year) & 
                     (df['Education'] == education) & 
                     (df['Marital_Status'] == status)]
    
    # Calculate totals for specific columns
    totals = {
        'ID'                : '',
        'Year_Birth'        : '',
        'Education'         : '',
        'Marital_Status'    : '',
        'Income'            : filtered_df['Income'].sum(),
        'Recency'           : filtered_df['Recency'].sum(),
        'Dt_Customer'       : '',
        'MntWines'          : filtered_df['MntWines'].sum(),
        'MntFruits'         : filtered_df['MntFruits'].sum(),
        'MntMeatProducts'   : filtered_df['MntMeatProducts'].sum(),
        'MntFishProducts'   : filtered_df['MntFishProducts'].sum(),
        'MntSweetProducts'  : filtered_df['MntSweetProducts'].sum(),
        'MntGoldProds'      : filtered_df['MntGoldProds'].sum()
    }
    
     # Convert totals dictionary to DataFrame
    totals_df = pd.DataFrame([totals])
    
    # Concatenate the filtered DataFrame with the totals DataFrame
    result_df = pd.concat([filtered_df, totals_df], ignore_index=True)
    
    # Display the result using Streamlit
    st.table(result_df[['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Income', 
                          'Recency', 'Dt_Customer', 'MntWines', 'MntFruits',
                          'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']])
    
    return totals

# Define the main function for your Streamlit app
def main():
    st.title('Market Sales Analysis ')
    
    page = st.sidebar.selectbox("Choose a page", ["Filter Data"])
    
    if page == "Filter Data":
        st.subheader("Filter Data")
        
        # Assume the CSV file is uploaded via Streamlit file uploader
        file_path = 'Example Data.csv'
        df = pd.read_csv(file_path, encoding='ISO-8859-1')

        # Filter DataFrame based on year birth selection
        year = st.selectbox('Year Birth:', df['Year_Birth'].unique())
        filtered_df = df[df['Year_Birth'] == year]

        # Filter DataFrame based on education selection 
        education = st.selectbox('Education:', filtered_df['Education'].unique())
        filtered_df = filtered_df[filtered_df['Education'] == education]

        # Filter DataFrame based on education selection 
        status = st.selectbox('Status:', filtered_df['Marital_Status'].unique())
        filtered_df = filtered_df[filtered_df['Marital_Status'] == status]
        
        st.subheader("Data Based Team")
        totals = filter_and_display_data(filtered_df, year, education, status)
    
        # Display the summary paragraph
        st.subheader("Kesimpulan")
        st.write(f"Analysis yang dihasilkan bahwa kelahiran tahun {year} dengan status {status} memiliki total pembelian wines sekitar {totals['MntWines']} botol, untuk pembelian produk manis {totals['MntSweetProducts']} pcs dan buah buahan sekitar {totals['MntFruits']}")
if __name__ == "__main__":
    main()
