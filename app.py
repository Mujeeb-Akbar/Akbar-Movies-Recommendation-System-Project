import pandas as pd
import requests
import pickle
import streamlit as st
import base64



st.set_page_config(
    page_icon='logo_movies.png',
    page_title='Akbar Recommendation System  | App',
    layout='wide'
)

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Convert the image "img.jpg" to base64
img = get_img_as_base64("img.jpg")

# Convert the local image to base64
Background_img = get_img_as_base64("background.jpg")  # Replace with your local image path


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpeg;base64,{Background_img}");
    background-size: 180%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    # opacity: 0.3;
    # transition: opacity 2s ease-in-out; /* 2 seconds transition */
}}


# [data-testid="stAppViewContainer"] > .main:hover {{
#     opacity: 1; /* Change to desired opacity on hover */
# }}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

.st-emotion-cache-1l8x88t {{
    border: 1px solid rgba(18, 18, 18, 0.2);
    border-radius: 0.5rem;
    padding: calc(-1px + 1rem);
    background: rgb(163 168 184 / 81%);
    box-shadow: 0 4px 8px rgb(18, 18, 18);
}}
.st-emotion-cache-4uzi61 {{
    border: 1px solid rgba(18, 18, 18, 0.2);
    border-radius: 0.5rem;
    padding: calc(-1px + 1rem);
    background: rgb(163 168 184 / 81%);
    box-shadow: 0 4px 8px rgb(18, 18, 18);
}}

.st-emotion-cache-qcpnpn {{
    border: 1px solid rgba(18, 18, 18, 0.2);
    border-radius: 0.5rem;
    padding: calc(-1px + 1rem);
    background: rgb(163 168 184 / 81%);
    box-shadow: 0 4px 8px rgb(18, 18, 18);
}}

.st-bl {{
    padding-right: 0.5rem;
    background: rgb(163 168 184 / 49%);
}}

element.style {{
    position: absolute;
    left: 0px;
    top: 40px;
    height: 40px;
    background: rgb(163 168 184 / 53%);
    width: 100%;
}}

.st-emotion-cache-15hul6a {{
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: rgb(0 119 231);
    border: 1px solid rgba(250, 250, 250, 0.2);
}}

.st-emotion-cache-1mi2ry5 {{
    display: flex;
    -webkit-box-pack: justify;
    justify-content: space-between;
    -webkit-box-align: start;
    align-items: start;
    padding: 0.25rem -2.5rem 1.5rem;
}}

.st-emotion-cache-ocqkz7 {{
    display: flex;
    flex-wrap: wrap;
    -webkit-box-flex: 1;
    flex-grow: 1;
    -webkit-box-align: stretch;
    align-items: stretch;
    gap: 1rem;
    background: rgb(19, 23, 32);
    padding: 16px;
}}
.st-emotion-cache-qcpnpn {{
    border: 1px solid rgba(18, 18, 18, 0.2);
    border-radius: 0.5rem;
    /* padding: calc(-1px + 1rem); */
    background: rgb(163 168 184 / 81%);
    box-shadow: 0 4px 8px rgb(18, 18, 18);
    padding: 82px 28px;
     MARGIN-BOTTOM: 80PX;
}}


.st-emotion-cache-4uzi61 {{
    border: 1px solid rgba(18, 18, 18, 0.2);
    border-radius: 0.5rem;
    /* padding: calc(-1px + 1rem); */
    background: rgb(163 168 184 / 81%);
    box-shadow: 0 4px 8px rgb(18, 18, 18);
    padding: 82px 28px;
    MARGIN-BOTTOM: 80PX;
}}



.st-emotion-cache-ocqkz7 {{
    display: flex;
    flex-wrap: wrap;
    -webkit-box-flex: 1;
    flex-grow: 1;
    -webkit-box-align: stretch;
    align-items: stretch;
    gap: 1rem;
    background: rgb(49, 51, 63);
    padding: 16px;
    box-shadow: 0 4px 8px rgb(18, 18, 18);
}}


.st-emotion-cache-uzeiqp p {{
    word-break: break-word;
    /* background: RED; */
    /* PADDING: 18PX; */
}}




.st-emotion-cache-1vt4y43 {{
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: rgb(46, 154, 255);
    border: 1px solid rgba(49, 51, 63, 0.2);
}}

.st-emotion-cache-183lzff {{
    font-family: "Source Code Pro", monospace;
    white-space: pre;
    font-size: 11px;
    overflow-x: auto;
    COLOR: rgb(238 197 5);
}}

.st-emotion-cache-1b0udgb {{
    font-family: "Source Sans Pro", sans-serif;
    font-size: 15px;
    color: rgb(249 244 15 / 60%);
    text-align: center;
    margin-top: 0.375rem;
    overflow-wrap: break-word;
    padding: 0.125rem;
}}
</style>
"""

# Apply CSS styling
st.markdown(page_bg_img, unsafe_allow_html=True)


# Sidebar configuration
with st.sidebar:
    # Display logo image
    st.image("logo_movies.png", use_container_width=True)

    # Adding a custom style with HTML and CSS
    st.markdown("""
        <style>
            .custom-text {
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                color:#ffc107
            }
            .custom-text span {
                color: #04ECF0; /* Color for the word 'Insights' */
            }
        </style>
    """, unsafe_allow_html=True)

    # Displaying the subheader with the custom class
    st.markdown('<p class="custom-text"><span>Akbar</span> Movies <span>Recommendation</span> System</p>', unsafe_allow_html=True)

    # HTML and CSS for the button
    github_button_html = """
    <div style="text-align: center; margin-top: 50px;">
        <a class="button" href="https://github.com/Engr-Mujeeb-Rahman" target="_blank" rel="noopener noreferrer">Visit my GitHub</a>
    </div>

    <style>
        /* Button styles */
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #ffc107;
            color: black;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #000345;
            color: white;
            text-decoration: none; /* Remove underline on hover */
        }

    </style>
    """

    # Display the GitHub button in the app
    st.markdown(github_button_html, unsafe_allow_html=True)
    
    # Footer
    # HTML and CSS for the centered footer
    footer_html = """
    <div style="padding:10px; text-align:center;margin-top: 10px;">
        <p style="font-size:20px; color:#ffffff;">Made with ❤️ by Engr. Mujeeb Ur Rahman</p>
    </div>
    """

    # Display footer in the app
    st.markdown(footer_html, unsafe_allow_html=True)



def fetch_poster(movie_id):
    responce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = responce.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    
    
# Custom CSS for styling
    st.markdown("""
        <style>
        /* Center and style the heading */
        .title {
            font-family: 'Montserrat', sans-serif; /* Using Montserrat font */
            color: white;  /* Change this color to your desired one */
            font-size: 3rem;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            background: linear-gradient(to right, #6a11cb, #2575fc); /* Gradient background */
            padding: 10px; /* Optional: Add some padding */
            border-radius: 10px; /* Optional: Rounded corners */
            box-shadow: 0 4px 8px bisque; /* Add box shadow */
            margin-bottom: 62px;
        }
        .st-emotion-cache-13ln4jf {
            width: 100%;
            padding: 2rem 1rem 10rem;
            max-width: 46rem;
        }
                
        </style>
    """, unsafe_allow_html=True)

# Title of the app with custom class
    st.markdown('<h2 class="title">Movies Recommendation System</h2>', unsafe_allow_html=True)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True , key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        
        # Fetch poster from API
        poster_url = fetch_poster(movie_id)
        recommended_movies_poster.append(poster_url)
    return recommended_movies , recommended_movies_poster

movies_1 = pickle.load(open('movies.pkl' , 'rb'))
movies = pd.DataFrame(movies_1)
movies_list = movies['title'].values


similarity = pickle.load(open('similarity_matrix.pkl' , 'rb'))

st.title('Akbar Movies Recommendation system 🎥')

selected_movie_name = st.selectbox(
    'Select a movie you like',
    movies['title'].values
)


 # Adding a custom style with HTML and CSS
st.markdown("""
    <style>
        .custom-head {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color:#ffc107
        }
        .custom-head span {
            color: #04ECF0; /* Color for the word 'Insights' */
        }
    </style>
""", unsafe_allow_html=True)



if st.button('recommend'):
    # Displaying the subheader with the custom class
    st.markdown('<P class="custom-head">We Recommend <span> These Movies </span> To You</P>', unsafe_allow_html=True)
    names , posters = recommend(selected_movie_name)
    
    col1 , col2 , col3 , col4 , col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0] , caption='Top pick' , use_container_width=True)
        
    with col2:
        st.text(names[1])
        st.image(posters[1] , caption='Highly Recommended' , use_container_width=True)
        
    with col3:
        st.text(names[2])
        st.image(posters[2] , caption='Must Watch' , use_container_width=True)
        
    with col4:
        st.text(names[3])
        st.image(posters[3] , caption='Critic Choice' , use_container_width=True)
        
    with col5:
        st.text(names[4])
        st.image(posters[4] , caption='Fan Favorite' , use_container_width=True)
        
