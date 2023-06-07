from PIL import Image
import streamlit as st
import webbrowser
import requests
from streamlit_lottie import st_lottie



st.set_page_config(page_title="Road accident map", page_icon=":imp:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_map = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_c7xcgjbt.json")
img_points = Image.open("C:/Users/Venux/PycharmProjects/Map_Try_1/images/points.png")
img_info = Image.open("C:/Users/Venux/PycharmProjects/Map_Try_1/images/info.png")
img_panel = Image.open("C:/Users/Venux/PycharmProjects/Map_Try_1/images/panel.png")
def open_html_file():

    file_path = "C:/Users/Venux/PycharmProjects/Map_Try_1/Map.html"
    webbrowser.open_new_tab(file_path)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("C:/Users/Venux/PycharmProjects/Map_Try_1/style/style.css")


with st.container():
    st.markdown("""
    <h1 style="text-align: center;font-size: 80px;">Road accident map</h1>
    """, unsafe_allow_html=True)
    st.markdown("""
        <h1 style="text-align: center; font-size: 36px;"><b>Зробимо Ваші подорожі безпечнішими!<b></h1>
        """, unsafe_allow_html=True)


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:

        st.write("##")
        st.markdown("""
                <h1 style="text-align: left; font-size: 27px;">З кожним днем авто стає все більшою частиною нашого життя. Паралельно з цим все актуальнішим стає питання безпеки на дорозі. За допомогою даного сервісу Ви зможете не тільки переглянути запланований маршрут, а й відслідкувати ділянки дороги з підвищеною небезпекою.</h1>
                """, unsafe_allow_html=True)



    with right_column:
        st_lottie(lottie_map, height = 300, key = "map")

with st.container():
    st.write("---")
    st.header("Довідка користувача:")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_points)
    with text_column:
        st.write("##")
        st.write("##")
        st.subheader("Усі випадки зображені окремо і тільки для візуальної зручності зібрані в окремі точки з підписом кількості дорожньо-транспортних пригод на певній ділянці дороги.")
        st.write("##")
        st.write("##")
        st.write("##")

    with image_column:
        st.image(img_info)
    with text_column:
        st.subheader("Натиснувши на конкретний маркер, Ви можете переглянути детальну інформацію щодо ДТП на даному місці. Зауважте, що фото не відповідають справжнім ДТП, а використані для кращого розуміння та сприймання інформації.")
        st.write("##")
        st.write("##")
        st.write("##")
        st.write("##")


    with image_column:
        st.image(img_panel)
    with text_column:
        st.subheader("Також Ви можете скористатись дано панелю управління розмітками. Ви маєте змогу прокласти маршрут, виділити певну область карти та ставити мітки. Після цього є можливість зберегти дану карту для користування надалі. ")




    if st.button("Переглянути мапу"):
        open_html_file()
    st.container()

with st.container():
    st.write("---")
    st.markdown("""
            <h1 style="text-align: left; font-size: 23px;"><b>Якщо Ви бажаєте додати мітку, що пов'язана з недавнім ДТП — пишіть на нашу електронну пошту та вказуйте деталі у форматі, як на мапі.<b></h1>
            """, unsafe_allow_html=True)
    st.write("##")

    contact_form  = """<form action="https://formsubmit.co/brolalala93@gmail.com.com" method="POST">
    <input type = "hidden" name = "_captcha" value = "false">
    <input type="text" name="name" placeholder = "Your name" required>
    <input type="email" name="email" placeholder = "Your email" required>
    <textarea name = "message" placeholder = "Your message here" required></textarea>
    <button type="submit">Send</button>
    </form> """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()