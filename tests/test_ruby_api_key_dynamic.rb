
require 'uri'
require 'net/http'
#require 'json'

apikey = ENV['API_KEY']

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
  uri = ARGV[0]
end
puts uri

site = Newsletter.new()
site.set_base_uri(uri)
locator = site.generate_code(10)
url = 'https://qxf2.com/'+locator
site.set_data_url(url)
cid = rand 1..5

header = {'x-api-key'=> apikey}
req = Net::HTTP::Post.new(uri, header)
req.set_form_data('url' => url, 'category_id' => cid, 'article_editor' => 'Ajitava')

res = Net::HTTP.start(uri.hostname, uri.port) do |http|
  http.request(req)
end

case res
when Net::HTTPSuccess, Net::HTTPRedirection
  puts "Response #{res.code} #{res.message}: #{res.body}"
else
  res.value
end
