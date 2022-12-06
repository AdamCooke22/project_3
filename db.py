from gnews import GNews
import pandas as pd
import streamlit as st



#################################################################################
# BUSINESS
##################################################################################

google_news = GNews()
business = google_news.get_news('Business')
for item in business:
  print(item.get('title','url'))

business_df = pd.DataFrame(business)
#len(business_df)
business_df = business_df[["title", "published date", "url"]]
business_df.head()

#################################################################################
# WORLD
##################################################################################

google_news = GNews()
world = google_news.get_news('world')
print(world[0-5])

world_df = pd.DataFrame(world)
#len(world_df)
world_df = world_df[["title", "published date", "url"]]
world_df.head()

#################################################################################
# NATION
##################################################################################

google_news = GNews()
nation = google_news.get_news('nation')
print(nation[0-5])

nation_df = pd.DataFrame(nation)
#len(nation_df)
nation_df = nation_df[["title", "published date", "url"]]
nation_df.head()

#################################################################################
# TECHNOLOGY
##################################################################################

google_news = GNews()
technology = google_news.get_news('technology')
print(technology[0-5])

technology_df = pd.DataFrame(technology)
#len(technology_df)
technology_df = technology_df[["title", "published date", "url"]]
technology_df.head()

#################################################################################
# STREAMLIT FRONT END
##################################################################################

st.title("Ez As Py News Articles")

tab1, tab2, tab3, tab4 = st.tabs(["Business", "World", "Nation", "Technology"])


tab1.subheader("Ez As Py News : Business")
with tab1:
    st.dataframe(business_df)

tab2.subheader("Ez As Py News : World")
with tab2:
    st.dataframe(world_df)

tab3.subheader("Ez As Py News : Nation")
with tab3:
    st.dataframe(nation_df)

tab4.subheader("Ez As Py News : Technology")
with tab4:
    st.dataframe(technology_df)
