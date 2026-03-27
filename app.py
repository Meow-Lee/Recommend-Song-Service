import streamlit as st

# pages
index_page = st.Page("app/pages/index_page.py", title="홈페이지", icon="🏠")
login_page = st.Page("app/pages/login_page.py", title="로그인", icon="🔒")

# navigation
pg = st.navigation([index_page, login_page])
pg.run()