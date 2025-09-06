#!/usr/bin/env ruby
# 3-repetition_token_2.rb

# Get the argument
str = ARGV[0].strip

# Regex using Oniguruma
if str.match?(/^hb?t+n$/)
  puts str
end
