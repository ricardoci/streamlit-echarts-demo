from streamlit_echarts import st_echarts


def render_basic_line_chart():
    options = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
    }
    st_echarts(
        options=options, height="400px",
    )
    st_echarts(
        options=options, height="400px", theme="dark",
    )
