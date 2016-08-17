require "watir"
require "watir-webdriver"
# will use watir-webdriver with Chrome
 env_no_proxy = (ENV['no_proxy'] || "").split(",")
 env_no_proxy << "127.0.0.1"
 puts env_no_proxy
 ENV['no_proxy']=env_no_proxy.join(",")

@browser = Watir::Browser.new :ie
@browser.goto("https://concierge.apple.com/history/R389/zh_CN")

puts "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
