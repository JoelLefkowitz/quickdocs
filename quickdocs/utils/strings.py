def remove_heading(html: str) -> str:
    return re.sub("<h1.*>.*?</h1>", "", html, flags=re.DOTALL)
