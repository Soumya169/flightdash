import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db =DB()

st.sidebar.title("✈️ Flight Analytics")
user_option = st.sidebar.selectbox("📌 Menu", ["About This Project", "Check Flights", "Analytics"])
if user_option == "Check Flights":
    st.title("🔍 Search for Flights")

    col1,col2 =st.columns(2)
    city = db.fetch_city_name()
    with col1:

       source = st.selectbox('Source',sorted(city))
    with col2:
        destination = st.selectbox("📍 Select Destination Airport", sorted(city))

    if st.button('Search'):
        result=db.fetch_all_flights(source,destination)
        st.dataframe(result)

elif user_option == 'Analytics':
    st.title("📊 Flight Data Analytics Dashboard")

    # Create columns for better layout
    col1, col2 = st.columns(2)

    # 🥧 Pie Chart: Airline Market Share
    with col1:
        airline, frequency = db.fetch_airline_freq()
        fig_pie = go.Figure(
            go.Pie(
                labels=airline,
                values=frequency,
                hoverinfo="label+percent",
                textinfo="value",
                marker=dict(colors=px.colors.qualitative.Pastel)
            ))
        st.subheader("✈️ Airline Market Share")
        st.plotly_chart(fig_pie, use_container_width=True)

    # 📊 Bar Chart: Busiest Airports
    with col2:
        city, frequency1 = db.busy_air_port()
        fig_bar = px.bar(
            x=city,
            y=frequency1,
            title="🏙️ Busiest Airports",
            labels={"x": "Airport", "y": "Number of Flights"},
            color=frequency1,
            color_continuous_scale="Blues"
        )
        st.plotly_chart(fig_bar, theme="streamlit", use_container_width=True)

    # 📈 Line Chart: Daily Flight Frequency
    date, frequency2 = db.dailyfreq()
    fig_line = px.line(
        x=date,
        y=frequency2,
        title="📅 Daily Flight Frequency",
        labels={"x": "Date", "y": "Number of Flights"},
        markers=True
    )
    st.plotly_chart(fig_line, theme="streamlit", use_container_width=True)

    # 🔥 Scatter Plot: Price Trends Over Time (Renamed from Heat Map)
    month, price = db.avg_price()
    fig_scatter = px.scatter(
        x=month,
        y=price,
        title="💰 Price Trends Over Time",
        labels={"x": "Month", "y": "Average Price"},
        color=price,
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig_scatter, theme="streamlit", use_container_width=True)

else :
    st.markdown(
        """
        <style>
        .about-container {
            background: linear-gradient(to right, #ffffff, #d9d9d9); /* White to Light Gray Gradient */
            padding: 30px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        }
        .about-title {
            color: black !important;
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            text-
        }
        .about-text {
            font-size: 18px;
            text-align: justify;
            color: #333; /* Dark Gray for Readability */
        }
        </style>
        <div class="about-container">
            <h1 class="about-title">📌 About the Project</h1>
            <p class="about-text">
            This project, <b>Flight Analytics Dashboard</b>, is designed to provide real-time insights into flight data using <b>SQL, Python, and Streamlit</b>. It allows users to <b>search for flights</b> between different cities, analyze airline trends, and visualize key statistics using <b>interactive charts</b>.
            <br><br>
            The dashboard includes a <b>Check Flights</b> feature to find available flights and an <b>Analytics</b> section to explore <b>airline market share, busiest airports, price trends, and flight frequency</b>. 
            <br><br>
            With an <b>intuitive UI</b> and <b>powerful data visualization</b>, this project aims to make flight data analysis <b>simple and efficient</b>.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )