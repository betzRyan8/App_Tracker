import streamlit as st
import json
import os

DATA_FILE = 'data.json'


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"applications_sent": 0}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)


st.title("🎯 Job Application Tracker")

data = load_data()

# --- Helper function to draw counter section ---


def counter_section(label, key):
    st.subheader(f"{label}: {data[key]}")
    col1, col2 = st.columns(2)
    if col1.button(f"➕ Add {label}"):
        data[key] += 1
        save_data(data)
        st.rerun()
    if col2.button(f"➖ Remove {label}"):
        if data[key] > 0:
            data[key] -= 1
            save_data(data)
            st.rerun()


# --- Render all counters ---
counter_section("Applications Sent", "applications_sent")
st.divider()

counter_section("Rejections", "rejections")
st.divider()

counter_section("Interviews", "interviews")
st.divider()

counter_section("Offers", "offers")
