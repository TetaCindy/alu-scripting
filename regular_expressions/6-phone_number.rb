#!/usr/bin/env ruby
# 6-phone_number.rb

# Get the argument
str = ARGV[0].strip

# Regex: exactly 10 digits
if str.match?(/^\d{10}$/)
  puts str
end
