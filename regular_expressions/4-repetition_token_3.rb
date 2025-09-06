#!/usr/bin/env ruby
# 4-repetition_token_3.rb

# Get the argument
str = ARGV[0].strip

# Regex without square brackets
if str.match?(/^hb?t*n$/)
  puts str
end
