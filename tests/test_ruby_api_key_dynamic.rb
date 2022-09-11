
require 'uri'
require 'net/http'
require 'json'
require 'test/unit/assertions'
include Test::Unit::Assertions

apikey = ENV['API_KEY']
puts "API key that I see is #{apikey}"

class Newsletter

  def set_base_uri(uri)
      @uri = uri
  end

  def set_data_url(url)
      @url = url
  end

  def generate_code(number)
    charset = Array('A'..'Z') + Array('a'..'z')
    Array.new(number) { charset.sample }.join
  end

end

if !ARGV[0]
  uri = URI('http://127.0.0.1:5000/api/articles')
else
  uri = URI(ARGV[0])
end

#Create a http object ... use SSL in case of https
http = Net::HTTP.new(uri.host, uri.port)
if uri.scheme == 'https'
    http.use_ssl = true
end

#Setup the header and parameters
site = Newsletter.new()
site.set_base_uri(uri)
locator = site.generate_code(10)
url = 'https://qxf2.com/'+locator
site.set_data_url(url)
cid = rand 1..5
header = {'x-api-key'=> apikey}
req = Net::HTTP::Post.new(uri, header)
req.set_form_data('url' => url, 'category_id' => cid, 'article_editor' => 'Ajitava')

#Make the post
res = http.request(req)

#Parse the message
message = JSON.parse(res.body)

#Assert we have what we want
assert_equal message['message'], "Record added successfully", "FAIL: API insert returned message #{message['message']}"
assert_equal res.code, "200", "FAIL: API insert returned #{res.code} instead of 200"
puts "API insert test PASSED"