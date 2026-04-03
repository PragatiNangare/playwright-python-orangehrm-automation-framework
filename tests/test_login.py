
def test_dashboard(login_page):
   assert login_page.page.locator("h6:has-text('Dashboard')").is_visible()
   print(login_page.page.title())