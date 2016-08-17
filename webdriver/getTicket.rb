require 'selenium-webdriver'
    env_no_proxy = (ENV['no_proxy'] || "").split(",")
    env_no_proxy << "127.0.0.1"
    ENV['no_proxy']=env_no_proxy.join(",")

    puts ENV['no_proxy']
browser = Selenium::WebDriver.for :firefox
browser.get "https://concierge.apple.com/history/R389/zh_CN"

