from playwright.sync_api import sync_playwright

# 目标网站（登录页，不登录也有完整HTML）
url = "https://njumatch.com"

# 模拟浏览器，自动加载所有HTML、CSS、JS
with sync_playwright() as p:
    # 无头模式（不弹出浏览器窗口）
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    
    # 等待页面加载完成 → 获取【和检查元素一模一样】的完整HTML
    page.wait_for_load_state("networkidle")
    full_html = page.content()

# 保存到文件
with open("完整页面.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("搞定！！")