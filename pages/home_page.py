
from playwright.sync_api import Page

class HomePage:
    """Page Object Model class for the Home page, using element IDs from the prompt."""
    def __init__(self, page: Page):
        self.page = page
        # Navbar
        self.navbar = page.locator('header')
        self.nav_brand = page.locator('header a[href="/"]')
        self.nav_home = page.locator('nav a[href="/"]')
        self.nav_services = page.locator('nav a[href="/services"]')
        self.nav_insights = page.locator('nav a[href="/insights"]')
        self.nav_community = page.locator('nav a[href="/community"]')
        self.nav_about = page.locator('nav a[href="/about"]')
        self.nav_contact = page.locator('nav a[href="/contact"]')
        # Prefer anchor tags for nav actions, fallback to button if present
        self.nav_login = page.locator('nav a:has-text("Login")')
        self.nav_register = page.locator('nav a:has-text("Register")')
        self.nav_logout = page.locator('nav a:has-text("Logout")')
        self.nav_login_btn = page.locator('nav button:has-text("Login")')
        self.nav_register_btn = page.locator('nav button:has-text("Register")')
        self.nav_logout_btn = page.locator('nav button:has-text("Logout")')
        self.nav_mobile_register = page.locator('.md\\:hidden a:has-text("Register")')
        self.nav_mobile_logout = page.locator('.md\\:hidden a:has-text("Logout")')
        # Hero section
        self.container = page.locator('#home-hero-section')
        self.hero_bg = page.locator('#home-hero-bg')
        self.hero_content = page.locator('#home-hero-content')
        self.hero_grid = page.locator('#home-hero-grid')
        self.hero_left = page.locator('#home-hero-left')
        self.hero_announcement = page.locator('#home-hero-announcement')
        self.hero_title = page.locator('#home-hero-title')
        self.hero_description = page.locator('#home-hero-description')
        self.hero_actions = page.locator('#home-hero-actions')
        self.explore_services_btn = page.locator('#home-explore-services-btn')
        self.contact_btn = page.locator('#home-contact-btn')
        self.hero_benefits = page.locator('#home-hero-benefits')
        self.benefit_fast = page.locator('#home-benefit-fast')
        self.benefit_scalable = page.locator('#home-benefit-scalable')
        self.benefit_ai = page.locator('#home-benefit-ai')
        self.hero_image_container = page.locator('#home-hero-image-container')
        self.hero_image = page.locator('#home-hero-image')
        # Quick actions
        self.quick_actions_section = page.locator('#home-quick-actions-section')
        self.quick_actions_container = page.locator('#home-quick-actions-container')
        self.quick_actions_header = page.locator('#home-quick-actions-header')
        self.quick_actions_header_content = page.locator('#home-quick-actions-header-content')
        self.quick_actions_title = page.locator('#home-quick-actions-title')
        self.quick_actions_desc = page.locator('#home-quick-actions-desc')
        self.quick_actions_grid = page.locator('#home-quick-actions-grid')
        # Dashboard card
        self.dashboard_link = page.locator('#home-dashboard-link')
        self.dashboard_card = page.locator('#home-dashboard-card')
        self.dashboard_card_body = page.locator('#home-dashboard-card-body')
        self.dashboard_icon = page.locator('#home-dashboard-icon')
        self.dashboard_content = page.locator('#home-dashboard-content')
        self.dashboard_title_row = page.locator('#home-dashboard-title-row')
        self.dashboard_title = page.locator('#home-dashboard-title')
        self.dashboard_arrow = page.locator('#home-dashboard-arrow')
        self.dashboard_desc = page.locator('#home-dashboard-desc')
        # Services card
        self.services_link = page.locator('#home-services-link')
        self.services_card = page.locator('#home-services-card')
        self.services_card_body = page.locator('#home-services-card-body')
        self.services_icon = page.locator('#home-services-icon')
        self.services_content = page.locator('#home-services-content')
        self.services_title_row = page.locator('#home-services-title-row')
        self.services_title = page.locator('#home-services-title')
        self.services_arrow = page.locator('#home-services-arrow')
        self.services_desc = page.locator('#home-services-desc')

    def click_my_account(self):
        # Example: click dashboard link as 'my account' for SaaS
        self.dashboard_link.click()

    def click_register(self):
        # Try known attributes first
        if hasattr(self, 'register_link'):
            try:
                if self.register_link.is_visible():
                    self.register_link.click()
                    return
            except Exception:
                pass
              # Fallback: try common selectors for register link
        selectors = [
            '#home-register-link',
            '#register',
            '.register-btn',
            'a[href*="register"]',
            'button:has-text("Register")',
            'a:has-text("Register")',
        ]
        for selector in selectors:
            locator = self.page.locator(selector)
            try:
                if locator.is_visible():
                    print(f"Clicking register using selector: {selector}")
                    locator.click()
                    return
            except Exception as e:
                print(f"Selector {selector} not clickable: {e}")
        raise Exception("No register button/link found using common selectors on HomePage.")


    def click_login(self):
        """Click on the login link/button from the home page, trying multiple selectors."""
        selectors = [
            '#home-login-link',
            '#login',
            '.login-btn',
            'a[href*="login"]',
            'button:has-text("Login")',
            'a:has-text("Login")',
        ]
        for selector in selectors:
            locator = self.page.locator(selector)
            try:
                if locator.is_visible():
                    print(f"Clicking login using selector: {selector}")
                    locator.click()
                    return
            except Exception as e:
                print(f"Selector {selector} not clickable: {e}")
        raise Exception("No login button/link found using common selectors on HomePage.")


    # Example action methods for key elements


    def get_hero_title(self):
        """Return the text content of the hero title element."""
        return self.hero_title.text_content()

    def click_explore_services(self):
        self.explore_services_btn.click()

    def click_contact(self):
        self.contact_btn.click()

    def is_hero_section_visible(self):
        return self.container.is_visible()

    def is_dashboard_card_visible(self):
        return self.dashboard_card.is_visible()

    def is_services_card_visible(self):
        return self.services_card.is_visible()

    def click_search(self):
        """Click on the search button to initiate the service search."""
        try:
            self.btn_search.click()
        except Exception as e:
            print(f" Exception while clicking 'Search' button: {e}")
            raise
