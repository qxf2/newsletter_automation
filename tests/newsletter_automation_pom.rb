require 'watir'
require 'rspec'
#require 'dotenv'
require 'selenium-webdriver'

require 'headless'


user = ENV['USER_NAME']
pass = ENV['PASS_WORD']

class BrowserContainer
    def initialize(browser)
      @browser = browser
    end
end

class Newsletter < BrowserContainer
    URL = "https://newsletter-generator.qxf2.com/"
    def open
        @browser.goto URL
        try_btn = @browser.link(:text =>"Try again")
        try_btn.click
    end

    def login_as(user, pass)
        user_field.set user
        login_button.click
        password_field.set pass 
        login_button.click      
    end

    def humberger_hover
        hover_ham = @browser.svg(:class =>"svg-inline--fa fa-bars fa-2x hamburger-right")
        hover_ham.hover
    end

    def click_add_article
        @browser.link(href: /articles/).click
    end

    def pass_url(url)
        url_field.set url   
    end

    def pass_title(title)
        title_field.set title   
    end

    def pass_desc(desc)
        desc_field.set desc   
    end

    def pass_time(time)
        time_field.set time
    end

    def pass_categoryid(categoryid)
        categoryid_field.set categoryid   
    end

    def scroll_bottom
        @browser.scroll.to :bottom
    end

    def article_btn
        add_article_btn = @browser.button(id: 'submit')
        add_article_btn.click
    end

    def close
        @browser.close
    end

    def generate_code(number)
        charset = Array('A'..'Z') + Array('a'..'z')
        Array.new(number) { charset.sample }.join
    end

    private

    def user_field
      @browser.text_field(id: 'identifierId')
    end

    def password_field
      @browser.text_field(type: 'password')
    end

    def login_button
      @browser.span(:text =>"Next")
    end

    def url_field
      @browser.text_field(id: 'url')
    end

    def title_field
        @browser.text_field(id: 'title')
    end

    def desc_field
        @browser.textarea(id: 'description')
    end

    def time_field
        @browser.text_field(id: 'time')
    end

    def categoryid_field
        @browser.select(id: 'category_id')
    end
    
  end 

begin
wat = Watir::Browser.new :firefox, headless: true
rescue Net::ReadTimeout => e
    if attempts == 0
      attempts += 1
      retry
    else
      raise
    end
  end

site = Newsletter.new(wat)
client = Selenium::WebDriver::Remote::Http::Default.new
client.read_timeout = 120
site.open
client.read_timeout = 120
site.login_as(user, pass)
site.humberger_hover
site.click_add_article
locator = site.generate_code(10)
site.pass_url('https://qxf2.com/'+locator)
site.pass_title('This is a sample title for watir automation')
site.pass_desc('This is a short description for automation through watir')
site.pass_time(rand 10..40)
site.pass_categoryid('comic')
site.scroll_bottom
site.article_btn
sleep 5
site.close
