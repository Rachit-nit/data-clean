import streamlit as st
import pandas as pd
import io
import plotly.express as px
from streamlit import bar_chart


@st.cache_data
def convert_df(dataframe):
    return dataframe.to_csv(index=False).encode('utf-8')

st.title("**BytePolish**")
st.title("Data cleaning")

file = st.file_uploader("Upload a csv file to clean", type=["csv"])

if file:
    if "df" not in st.session_state or st.session_state.get("uploaded_file_name") != file.name:
        st.session_state.df = pd.read_csv(file)
        st.session_state.uploaded_file_name = file.name

    st.success("You have uploaded the file")
    st.info("Check sidebar for data summary")

    df = st.session_state.df

    st.sidebar.subheader("Data Summary")
    st.sidebar.dataframe(df.describe())

    st.subheader("Data preview")
    st.dataframe(df,use_container_width=True)
    st.markdown("---")

    removeDuplicates=st.checkbox("Remove Duplicates?")
    if removeDuplicates:
        df=df.drop_duplicates()
        st.session_state.df = df
        st.info("Removed all duplicates")
    st.markdown("---")


    missing_action = st.selectbox(
        "How should we handle missing (blank) values?",
        ["Do Nothing", "Drop rows with missing values", "Fill missing text with 'Unknown' & numbers with 0"]
    )

    if missing_action == "Drop rows with missing values":
        df = df.dropna()
        st.session_state.df = df
        st.info("Dropped all rows containing empty cells.")

    elif missing_action == "Fill missing text with 'Unknown' & numbers with 0":
        num_cols = df.select_dtypes(include=['number']).columns
        obj_cols = df.select_dtypes(include=['object']).columns
        df[num_cols] = df[num_cols].fillna(0)
        df[obj_cols] = df[obj_cols].fillna("Unknown")
        st.session_state.df = df
        st.info("Filled blank cells with default values.")

    st.markdown("---")

    column_list = df.columns.tolist()
    columns_to_drop = st.multiselect("Drop these Columns",column_list)
    if columns_to_drop:
        existing_cols_to_drop = [col for col in columns_to_drop if col in df.columns]
        if existing_cols_to_drop:
            df = df.drop(columns=existing_cols_to_drop)
            st.session_state.df = df
            st.info("The chosen columns have been dropped.")

    current_columns = df.columns.tolist()

    st.markdown("---")

    if current_columns:
        columns_type_convert = st.selectbox("Change type of which column", current_columns)
        target_type = st.selectbox("Target Data type", options=["int64", "float64", "str", "datetime"])

        if st.button("Convert Data type"):
            try:
                if target_type == "datetime":
                    df[columns_type_convert] = pd.to_datetime(df[columns_type_convert])
                else:
                    df[columns_type_convert] = df[columns_type_convert].astype(target_type)

                st.session_state.df = df  
                st.success(f"Successfully converted {columns_type_convert} to {target_type}")
                st.rerun()
            except Exception as e:
                st.error("Could not convert data: The column might contain invalid characters.")
    else:
        st.warning("No columns left to convert.")

    st.markdown("---")

    st.subheader("Visualize data")
    plot_choice = st.selectbox("What type of plot do you want?", options=["Scatter Plot", "Bar Chart", "Histogram"])
    plot_df = df.sample(n=15000, random_state=42) if len(df) > 15000 else df
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

    if plot_choice == "Scatter Plot":
        x_axis = st.selectbox("Select x axis (Numeric)", options=numeric_columns, key="scatter_x")
        y_axis = st.selectbox("Select y axis (Numeric)", options=numeric_columns, key="scatter_y")

        if x_axis and y_axis:
            scatterPlot = px.scatter(plot_df, x=x_axis, y=y_axis)
            st.plotly_chart(scatterPlot)

    if plot_choice == "Bar Chart":
        x_options = categorical_columns if categorical_columns else column_list

        x_axis = st.selectbox("Select x axis (Text/Labels)", options=x_options, key="bar_x")
        y_axis = st.selectbox("Select y axis (Numeric Values)", options=numeric_columns, key="bar_y")

        if x_axis and y_axis:
            barChart = px.bar(plot_df, x=x_axis, y=y_axis)
            st.plotly_chart(barChart)

    if plot_choice == "Histogram":
        x_axis = st.selectbox("Select column to count", options=column_list, key="hist_x")

        if x_axis:
            histoGram = px.histogram(plot_df, x=x_axis)
            st.plotly_chart(histoGram)

    st.markdown("---")


    st.subheader("Final Cleaned Data Preview")
    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.subheader("Export & Lifecycle Management")

    col1, col2 = st.columns(2)

    with col1:
        csv_buffer = st.session_state.df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Export Cleaned Dataset",
            data=csv_buffer,
            file_name="cleaned_data.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col2:
        if st.button(" Clear App Memory & Start Fresh", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
            
    with st.bottom:
        st.divider()
        st.caption("© 2026 BytePolish. All rights reserved.")
        st.markdown("[GitHub] : https://github.com/Rachit-nit • [LinkedIn] : https://www.linkedin.com/in/rachit-saxena-25-/")


else:
    st.warning("Please upload a file")

