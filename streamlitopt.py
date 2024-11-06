# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px

# --- Title and Introduction ---
st.title("📊 Interactive Visualizations with Plotly and Streamlit")
st.write("Explore interactive visualizations of data with Plotly. This demo uses the **tips** dataset to show examples of bar and histogram charts.")

# --- Sidebar: Author Information ---
st.sidebar.header("Visualization Skill Workshop - Plotly")
name = st.sidebar.text_input("Enter your name:", "Siddharth S Gadekar")
course = st.sidebar.text_input("Enter your Course name:", "Semester-I BTech")
instructor_name = st.sidebar.text_input("Enter Instructor's name:", "Prof. Ashwini Mathur _ SOCSE")

# Display author information in the sidebar if provided
st.sidebar.markdown("---")
if name and course and instructor_name:
    st.sidebar.markdown(
        f"**Project by:** {name}  \n"
        f"**Course:** {course}  \n"
        f"**Instructor:** {instructor_name}"
    )

# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset

# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(tips.head())

# --- Task 1: Interactive Bar Chart ---
st.subheader("Task 1: Bar Chart - Average Tip by Day")
# Create a bar chart
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='simple_white'
)
fig2.update_layout(title_font_size=18, title_x=0.5)
st.plotly_chart(fig2)

# --- Task 2: Interactive Histogram Chart ---
st.subheader("Task 2: Histogram - Tip Distribution by Gender")
# Create a histogram for tips distribution by gender
fig3 = px.histogram(
    tips, x='tip', color='sex',
    title='Distribution of Tips by Gender',
    labels={'tip': 'Tip ($)', 'sex': 'Gender'},
    template='simple_white'
)
fig3.update_layout(title_font_size=18, title_x=0.5)
st.plotly_chart(fig3)

# --- Additional Notes and Footer ---
st.write("---")
st.write("Thank you for exploring this interactive visualization. For more insights, experiment with additional datasets and chart types using Plotly in Streamlit!")